# -*- coding: utf-8 -*-
"""Nimmt das regelmässige Netzmuster aus KI-erzeugter Gesichtshaut.

    python3 tools/haut-entrastern.py <bild.png> <ergebnis.png> [staerke]

Bildgeneratoren legen auf Haut oft eine gleichmässige feine Struktur, die aus
der Nähe wie Stoff oder Reptilhaut aussieht. Das Skript dämpft genau diese
hochfrequente Schicht, lässt Falten, Poren und Formen stehen und schützt
Augen, Brauen, Lippen, Haare und die Goldadern über eine Kantenmaske.
Zum Schluss feines Filmkorn, sonst wirkt die Fläche tot.
"""
import sys

import cv2
import numpy as np

SRC = sys.argv[1]
DST = sys.argv[2]
STAERKE = float(sys.argv[3]) if len(sys.argv) > 3 else 0.85

img = cv2.imread(SRC, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
h, w = img.shape[:2]
u8 = (img * 255).astype(np.uint8)

# ─── Hautmaske ──────────────────────────────────────────────────────────────
hsv = cv2.cvtColor(u8, cv2.COLOR_BGR2HSV)
H, S, V = [hsv[..., i].astype(np.float32) for i in range(3)]

haut = ((H >= 3) & (H <= 22) & (S >= 85) & (S <= 205) &
        (V >= 45) & (V <= 240)).astype(np.float32)

# Nur oben rechts, dort sitzt das Gesicht. Schützt die Typografie links.
box = np.zeros((h, w), np.float32)
box[int(h * 0.02):int(h * 0.47), int(w * 0.46):] = 1.0
haut *= box

haut = cv2.morphologyEx(haut, cv2.MORPH_CLOSE, np.ones((21, 21), np.uint8))
haut = cv2.morphologyEx(haut, cv2.MORPH_OPEN, np.ones((11, 11), np.uint8))

# grösste zusammenhängende Fläche behalten, das ist Gesicht und Hals
n, lab, stats, _ = cv2.connectedComponentsWithStats((haut > 0.5).astype(np.uint8))
if n > 1:
    haut = (lab == 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))).astype(np.float32)
haut = cv2.GaussianBlur(haut, (0, 0), 12)

# ─── Kanten schützen: Augen, Brauen, Lippen, Nasenlöcher, Goldadern ─────────
grau = cv2.cvtColor(u8, cv2.COLOR_BGR2GRAY).astype(np.float32)
kante = np.abs(cv2.Laplacian(cv2.GaussianBlur(grau, (0, 0), 2.0), cv2.CV_32F))
kante = cv2.GaussianBlur(kante, (0, 0), 5)
kante /= (np.percentile(kante, 99.5) + 1e-6)
schutz = np.clip(kante * 1.9, 0, 1)

# helle Goldpartien zusätzlich schützen
gold = np.clip((V - 195) / 40.0, 0, 1)
schutz = np.maximum(schutz, cv2.GaussianBlur(gold, (0, 0), 4))

maske = haut * (1 - schutz) * STAERKE
print('bearbeitete Fläche: %.1f %% des Bildes' % (100 * maske.mean()))

# ─── Netzmuster dämpfen ─────────────────────────────────────────────────────
glatt = img.copy()
for sc, ss in ((0.10, 11), (0.07, 9)):
    glatt = cv2.bilateralFilter(glatt, 9, sc, ss)

# nur die feinste Schicht ersetzen, mittlere Hauttextur bleibt erhalten
tief = cv2.GaussianBlur(img, (0, 0), 2.6)
fein_orig = img - tief
fein_glatt = glatt - cv2.GaussianBlur(glatt, (0, 0), 2.6)
ergebnis = tief + fein_orig * 0.22 + fein_glatt * 0.78

# ─── Filmkorn ───────────────────────────────────────────────────────────────
rng = np.random.default_rng(7)
korn = rng.normal(0, 0.014, (h, w)).astype(np.float32)
korn = cv2.GaussianBlur(korn, (0, 0), 0.6)[..., None]
ergebnis = ergebnis + korn

m = maske[..., None]
out = img * (1 - m) + np.clip(ergebnis, 0, 1) * m
cv2.imwrite(DST, np.clip(out * 255, 0, 255).astype(np.uint8))
print('geschrieben:', DST)
