# -*- coding: utf-8 -*-
"""Ersetzt künstliche KI-Haut durch aufgebaute, echte Hautstruktur.

    python3 tools/haut-entrastern.py <roh.png> <ergebnis.png> [staerke]

Bildgeneratoren legen auf Haut ein gleichmässiges Gitter, das aus der Nähe wie
Stoff aussieht. Dämpfen reicht nicht, weil Muster und Falten gleich stark sind.
Deshalb wird die feine Schicht entfernt und neu aufgebaut, aus vier Teilen:

1. Poren       runde Vertiefungen in zufälligen Grössen, wie in echter Haut
2. Pigment     unregelmässige Farbflecken, ganz schwach
3. Sprenkel    einzelne dunklere Punkte, Sommersprossen und kleine Male
4. Glanz       leichter Schimmer dort, wo das Licht auf die Haut trifft

Erhalten bleiben Gesichtsform, grosse Falten, Rötungen, Licht und Schatten.
Geschützt: Augen, Brauen, Lippen, Nasenlöcher, Haare und die Goldadern.
"""
import sys

import cv2
import numpy as np

SRC, DST = sys.argv[1], sys.argv[2]
STAERKE = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0

img = cv2.imread(SRC, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
h, w = img.shape[:2]
u8 = (img * 255).astype(np.uint8)
rng = np.random.default_rng(23)

# ─── Hautmaske ──────────────────────────────────────────────────────────────
hsv = cv2.cvtColor(u8, cv2.COLOR_BGR2HSV)
H, S, V = [hsv[..., i].astype(np.float32) for i in range(3)]

haut = ((H >= 3) & (H <= 22) & (S >= 85) & (S <= 205) &
        (V >= 45) & (V <= 240)).astype(np.float32)
box = np.zeros((h, w), np.float32)
box[int(h * 0.02):int(h * 0.47), int(w * 0.46):] = 1.0
haut *= box
haut = cv2.morphologyEx(haut, cv2.MORPH_CLOSE, np.ones((21, 21), np.uint8))
haut = cv2.morphologyEx(haut, cv2.MORPH_OPEN, np.ones((11, 11), np.uint8))
n, lab, stats, _ = cv2.connectedComponentsWithStats((haut > 0.5).astype(np.uint8))
if n > 1:
    haut = (lab == 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))).astype(np.float32)
haut = cv2.GaussianBlur(haut, (0, 0), 12)

grau = cv2.cvtColor(u8, cv2.COLOR_BGR2GRAY).astype(np.float32)
kante = np.abs(cv2.Laplacian(cv2.GaussianBlur(grau, (0, 0), 2.0), cv2.CV_32F))
kante = cv2.GaussianBlur(kante, (0, 0), 5)
kante /= (np.percentile(kante, 99.5) + 1e-6)
schutz = np.clip(kante * 1.9, 0, 1)
schutz = np.maximum(schutz, cv2.GaussianBlur(np.clip((V - 195) / 40.0, 0, 1), (0, 0), 4))

maske = haut * (1 - schutz) * STAERKE
flaeche = maske > 0.05
print('bearbeitete Fläche: %.1f %% des Bildes' % (100 * maske.mean()))

# ─── Altes Muster weg, Falten behalten ──────────────────────────────────────
glatt = img.copy()
for sc, ss in ((0.11, 25), (0.09, 21), (0.07, 17)):
    glatt = cv2.bilateralFilter(glatt, 13, sc, ss)
falten = cv2.GaussianBlur(img, (0, 0), 3.2) - cv2.GaussianBlur(img, (0, 0), 11.0)
basis = glatt + falten * 1.05

# ─── 1. Poren, in drei Grössen überlagert ──────────────────────────────────
# Bandbegrenztes Rauschen statt einzelner Punkte. Punkte werden im Druck zu
# schwarzem Pfeffer, überlagerte Bänder ergeben organische Struktur.
def band(sig_klein, sig_gross, seed):
    r = np.random.default_rng(seed).normal(0, 1, (h, w)).astype(np.float32)
    b = cv2.GaussianBlur(r, (0, 0), sig_klein) - cv2.GaussianBlur(r, (0, 0), sig_gross)
    return b / (b.std() + 1e-6)

poren = (band(0.7, 1.5, 31) * 0.55
         + band(1.2, 2.6, 37) * 0.30
         + band(2.2, 4.8, 41) * 0.15)
poren = np.clip(poren, -2.2, 2.2)
poren /= (poren.std() + 1e-6)

# ─── 2. Pigment: unregelmässige Farbflecken ─────────────────────────────────
pigment = np.clip(band(9.0, 26.0, 53), -2.5, 2.5)

# ─── 3. Sprenkel: ganz wenige, weiche dunklere Stellen ─────────────────────
fleck = band(2.6, 7.0, 67)
sprenkel = -np.clip(fleck - 1.35, 0, None)      # nur die stärksten Ausschläge
sprenkel = cv2.GaussianBlur(sprenkel, (0, 0), 1.6)
sprenkel /= (np.abs(sprenkel).max() + 1e-6)

# ─── 4. Glanz dort, wo Licht auf die Haut trifft ────────────────────────────
lum = cv2.GaussianBlur(grau / 255.0, (0, 0), 7)
licht = np.clip((lum - 0.30) / 0.45, 0, 1) ** 1.6
glanzrausch = cv2.GaussianBlur(rng.normal(0, 1, (h, w)).astype(np.float32), (0, 0), 3.5)
glanzrausch /= (glanzrausch.std() + 1e-6)
glanz = np.clip(glanzrausch, 0, None) * licht * 0.030

# ─── Zusammensetzen ─────────────────────────────────────────────────────────
# Struktur folgt dem Licht: im Schatten sieht man kaum Poren
sichtbar = np.clip((lum - 0.06) * 1.7, 0, 1.3)
struktur = (poren * 0.0130 + pigment * 0.0060 + sprenkel * 0.030) * sichtbar

lab_img = cv2.cvtColor(np.clip(basis, 0, 1), cv2.COLOR_BGR2LAB)
lab_img[..., 0] = np.clip(lab_img[..., 0] + (struktur + glanz) * 255 * 0.9, 0, 255)
# Pigment leicht ins Rötliche, sonst wirken die Flecken grau
lab_img[..., 1] = np.clip(lab_img[..., 1] + pigment * sichtbar * 1.7, 0, 255)
ergebnis = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)

m = maske[..., None]
out = img * (1 - m) + np.clip(ergebnis, 0, 1) * m
cv2.imwrite(DST, np.clip(out * 255, 0, 255).astype(np.uint8))
print('geschrieben:', DST)
