# -*- coding: utf-8 -*-
"""Ersetzt das künstliche Netzmuster auf KI-Haut durch echte Hautstruktur.

    python3 tools/haut-entrastern.py <roh.png> <ergebnis.png> [staerke]

Bildgeneratoren legen auf Haut ein gleichmässiges Gitter, das aus der Nähe wie
Stoff oder Reptilhaut aussieht. Dämpfen allein reicht nicht, weil Muster und
Falten die gleiche Amplitude haben. Deshalb wird die feine Schicht ganz
entfernt und durch unregelmässiges Porenrauschen ersetzt.

Erhalten bleiben: Gesichtsform, grosse Falten, Rötungen, Licht und Schatten.
Geschützt über eine Kanten- und Helligkeitsmaske: Augen, Brauen, Lippen,
Nasenlöcher, Haare und die Goldadern.
"""
import sys

import cv2
import numpy as np

SRC, DST = sys.argv[1], sys.argv[2]
STAERKE = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0

img = cv2.imread(SRC, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
h, w = img.shape[:2]
u8 = (img * 255).astype(np.uint8)

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
print('bearbeitete Fläche: %.1f %% des Bildes' % (100 * maske.mean()))

# ─── Feine Schicht entfernen, mittlere Falten behalten ──────────────────────
# kräftig kantenerhaltend glätten, das nimmt das Gitter vollständig weg
glatt = img.copy()
for sc, ss in ((0.11, 25), (0.09, 21), (0.07, 17)):
    glatt = cv2.bilateralFilter(glatt, 13, sc, ss)

# Falten im Bereich von etwa 6 bis 30 Pixeln wieder dazugeben
falten = cv2.GaussianBlur(img, (0, 0), 3.2) - cv2.GaussianBlur(img, (0, 0), 11.0)
ergebnis = glatt + falten * 1.05

# ─── Echte Hautstruktur erzeugen ───────────────────────────────────────────
# unregelmässiges Rauschen in zwei Grössen: feine Poren und gröbere Unruhe
rng = np.random.default_rng(11)
r = rng.normal(0, 1, (h, w)).astype(np.float32)
poren = cv2.GaussianBlur(r, (0, 0), 0.8) - cv2.GaussianBlur(r, (0, 0), 1.9)
unruhe = cv2.GaussianBlur(r, (0, 0), 2.6) - cv2.GaussianBlur(r, (0, 0), 6.0)
poren /= (poren.std() + 1e-6)
unruhe /= (unruhe.std() + 1e-6)
struktur = poren * 0.0145 + unruhe * 0.0085

# in den Lichtern kräftiger, in tiefen Schatten fast nichts, wie in echt
lum = cv2.GaussianBlur(grau / 255.0, (0, 0), 8)
struktur = struktur * np.clip((lum - 0.08) * 1.8, 0, 1.25)

ergebnis = ergebnis + struktur[..., None]

m = maske[..., None]
out = img * (1 - m) + np.clip(ergebnis, 0, 1) * m
cv2.imwrite(DST, np.clip(out * 255, 0, 255).astype(np.uint8))
print('geschrieben:', DST)
