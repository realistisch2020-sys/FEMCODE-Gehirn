# -*- coding: utf-8 -*-
"""Druckfertiges Full-Wrap-Cover fuer KDP: "Ich stand nie auf meiner eigenen Liste".

Rein typografisch in Kintsugi-Anmutung (gleiches Grundgeruest wie
tools/buch6-cover.py und tools/buch3-cover.py), Wein/Gold-Palette passend
zum Bonus-PDF (tools/buch4-bonus-pdf.py). Ersetzt das alte, flach
gerasterte Cover ohne bearbeitbare Ebenen.

    python3 tools/buch4-cover.py
"""
import math, sys, os
from reportlab.pdfgen import canvas as rl
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = '/home/user/FEMCODE-Gehirn/outputs/buch-an-mich-denken/buch4-Cover-Print-FullWrap.pdf'
# Optional: Petras eigenes, fertiges Vorderseitenbild als Argument.
# Dann entfaellt meine Typografie, nur Rueckseite/Ruecken bleiben wie gehabt.
BILD = sys.argv[1] if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else None

# ─── Masse ──────────────────────────────────────────────────────────────────
SEITEN  = 119
TRIM_B  = 139.7 * mm
TRIM_H  = 215.9 * mm
RUECKEN = SEITEN * 0.0025 * 25.4 * mm
BLEED   = 3.2 * mm
W = BLEED + TRIM_B + RUECKEN + TRIM_B + BLEED
H = BLEED + TRIM_H + BLEED

RUECK_X = BLEED
SPINE_X = BLEED + TRIM_B
FRONT_X = SPINE_X + RUECKEN
SAFE    = 6 * mm

# ─── Farben: Wein/Ink / Gold, wie das Bonus-PDF dieses Buches ──────────────
NACHT  = colors.HexColor('#2A0E1E')
TIEFE  = colors.HexColor('#1C0914')
CREME  = colors.HexColor('#FAF3E6')
GOLD   = colors.HexColor('#C99A43')
GOLD_H = colors.HexColor('#E6C06B')
WEIN   = colors.HexColor('#E8A9C4')
GRAU   = colors.HexColor('#A8938E')

# ─── Schriften ──────────────────────────────────────────────────────────────
F = '/usr/share/fonts/truetype/liberation/'
from reportlab import rl_config
pdfmetrics.registerFont(TTFont('Sans',   F + 'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SansB',  F + 'LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Serif',  F + 'LiberationSerif-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SerifI', F + 'LiberationSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('SerifB', F + 'LiberationSerif-Bold.ttf'))
rl_config.canvas_basefontname = 'Sans'

c = rl.Canvas(OUT, pagesize=(W, H))

# ─── Hintergrund ────────────────────────────────────────────────────────────
c.setFillColor(NACHT)
c.rect(0, 0, W, H, fill=1, stroke=0)

for i in range(140):
    t = i / 140.0
    c.setFillColorRGB(0.165 + 0.055 * (1 - t), 0.055 + 0.035 * (1 - t),
                      0.118 + 0.045 * (1 - t))
    c.rect(FRONT_X, H - (i + 1) * H / 140, TRIM_B + BLEED, H / 140 + 0.6,
           fill=1, stroke=0)

c.setFillColor(TIEFE)
c.rect(0, 0, SPINE_X, H, fill=1, stroke=0)


# ─── Goldadern (Kintsugi) ───────────────────────────────────────────────────
def ader(x, y, laenge, winkel, tiefe=0, breite=1.0, seed=0):
    if tiefe > 2 or laenge < 9 * mm:
        return
    schritte = 7
    px, py = x, y
    c.setLineCap(0)
    c.setLineJoin(0)
    for s in range(schritte):
        knick = ((seed * 37 + s * 53 + tiefe * 91) % 100 / 100.0 - 0.5) * 0.55
        w = winkel + knick
        d = laenge / schritte * (0.6 + ((seed + s * 7) % 10) / 12.0)
        nx, ny = px + math.cos(w) * d, py + math.sin(w) * d
        c.setStrokeColor(GOLD_H if s % 3 == 1 else GOLD)
        c.setLineWidth(max(0.28, breite * (1 - s / (schritte + 3.0))))
        c.line(px, py, nx, ny)
        px, py = nx, ny
        if s == 3:
            ader(px, py, laenge * 0.40, winkel + 0.95, tiefe + 1,
                 breite * 0.5, seed + 11)
    ader(px, py, laenge * 0.34, winkel - 0.85, tiefe + 1, breite * 0.5, seed + 5)


c.saveState()
p = c.beginPath()
p.rect(FRONT_X, 0, TRIM_B + BLEED, H)
c.clipPath(p, stroke=0)
c.setStrokeAlpha(0.0 if BILD else 0.6)
ader(FRONT_X + TRIM_B - 15 * mm, H - BLEED + 2 * mm, 122 * mm, math.radians(252),
     breite=1.3, seed=6)
c.setStrokeAlpha(0.0 if BILD else 0.3)
ader(FRONT_X + TRIM_B - 36 * mm, BLEED - 3 * mm, 50 * mm, math.radians(68),
     breite=0.8, seed=21)
c.restoreState()


# ─── Hilfsfunktionen ────────────────────────────────────────────────────────
def gesperrt(x, y, text, font, groesse, farbe, sperrung, mitte=False):
    c.setFont(font, groesse)
    c.setFillColor(farbe)
    breite = sum(pdfmetrics.stringWidth(z, font, groesse) + sperrung
                 for z in text) - sperrung
    cx = x - breite / 2 if mitte else x
    for z in text:
        c.drawString(cx, y, z)
        cx += pdfmetrics.stringWidth(z, font, groesse) + sperrung
    return breite


def zeile(x, y, text, font, groesse, farbe, mitte=False, rechts=False):
    c.setFont(font, groesse)
    c.setFillColor(farbe)
    if mitte:
        c.drawCentredString(x, y, text)
    elif rechts:
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)


def block(x, y, zeilen, font, groesse, farbe, durchschuss, mitte=False):
    for i, t in enumerate(zeilen):
        zeile(x, y - i * durchschuss, t, font, groesse, farbe, mitte=mitte)
    return y - (len(zeilen) - 1) * durchschuss


def fit(text, font, breite, max_pt=200):
    g = 10.0
    w = pdfmetrics.stringWidth(text, font, g)
    return min(max_pt, g * breite / max(w, 0.01))


# ════════════════════════════════════════════════════════════════════════════
# VORDERSEITE
# ════════════════════════════════════════════════════════════════════════════
fx = FRONT_X + SAFE + 4 * mm
fm = FRONT_X + TRIM_B / 2
innen = TRIM_B - (SAFE + 4 * mm) - (SAFE + 3 * mm)


def gruppe(zeilen, breite, farbe, ty, durchschuss=1.03):
    g = min(fit(t, 'SansB', breite) for t in zeilen)
    for t in zeilen:
        zeile(fx, ty, t, 'SansB', g, farbe)
        ty -= g * durchschuss
    return ty


if BILD:
    # Petras fertiges Vorderseitenbild randlos einsetzen, mittig beschnitten
    from reportlab.lib.utils import ImageReader
    from PIL import Image as PILImage
    iw, ih = PILImage.open(BILD).size
    fw, fh = TRIM_B + BLEED, H
    skala = max(fw / iw, fh / ih)
    zw, zh = iw * skala, ih * skala
    c.saveState()
    pfad = c.beginPath(); pfad.rect(FRONT_X, 0, fw, H); c.clipPath(pfad, stroke=0)
    c.drawImage(ImageReader(BILD), FRONT_X - (zw - fw) / 2, -(zh - fh) / 2,
                width=zw, height=zh, mask='auto')
    c.restoreState()
    dpi = iw / (fw / mm / 25.4)
    print(f'  Bild eingesetzt: {iw}x{ih} px  ->  {dpi:.0f} dpi'
          + ('' if dpi >= 300 else '   ACHTUNG: unter 300 dpi'))
else:
    ty = H - BLEED - 30 * mm
    ty = gruppe(['ICH STAND', 'NIE AUF'], innen * 0.90, CREME, ty, 1.02)
    ty -= 6 * mm
    ty = gruppe(['MEINER', 'EIGENEN LISTE'], innen * 0.96, GOLD_H, ty, 1.06)

    ty -= 9 * mm
    c.setStrokeColor(GOLD); c.setLineWidth(1.0)
    c.line(fx, ty, fx + 30 * mm, ty)

    ty -= 12.5 * mm
    block(fx, ty, ['Du hast an alle gedacht.', 'Nur nicht an dich.'],
          'SerifB', 15.5, CREME, 7.6 * mm)
    ty -= 17.5 * mm
    block(fx, ty, ['Mit dem Pflicht-oder-Liebe-Check:',
                   'war das wirklich Liebe, oder nur Pflicht?'],
          'Serif', 11.6, WEIN, 6.0 * mm)

    sy = BLEED + 20 * mm
    gesperrt(fm, sy, 'PETRA TANNER', 'SansB', 13.5, CREME, 3.6, mitte=True)
    c.setStrokeColor(GOLD); c.setLineWidth(0.7)
    c.line(fm - 26 * mm, sy - 5.2 * mm, fm + 26 * mm, sy - 5.2 * mm)
    gesperrt(fm, sy - 11.5 * mm, 'SAFE TO THRIVE', 'Sans', 8.2, GOLD, 3.8, mitte=True)


# ════════════════════════════════════════════════════════════════════════════
# BUCHRÜCKEN
# ════════════════════════════════════════════════════════════════════════════
c.saveState()
c.translate(SPINE_X + RUECKEN / 2, H / 2)
c.rotate(-90)
zeile(-H / 2 + 30 * mm, -2.4, 'ICH STAND NIE AUF MEINER EIGENEN LISTE', 'SansB', 8.2, CREME)
zeile(H / 2 - 30 * mm, -2.4, 'PETRA TANNER', 'Sans', 7.4, GOLD, rechts=True)
c.restoreState()


# ════════════════════════════════════════════════════════════════════════════
# RÜCKSEITE
# ════════════════════════════════════════════════════════════════════════════
rx = RUECK_X + SAFE + 7 * mm
y  = H - BLEED - 18 * mm
BARCODE_H = 32 * mm

gesperrt(rx, y, 'FÜR FRAUEN, DIE WISSEN,', 'SansB', 7.8, GOLD, 1.4)
y -= 4.8 * mm
gesperrt(rx, y, 'WAS ALLE ANDEREN BRAUCHEN.', 'SansB', 7.8, GOLD, 1.4)
y -= 13 * mm

y = block(rx, y, [
 'Du weisst genau, was alle anderen brauchen.',
 'Aber wann hast du dich das letzte Mal',
 'selbst gefragt, was du eigentlich willst?'], 'Serif', 11.6, CREME, 6.0 * mm)

y -= 9 * mm
zeile(rx, y, 'Es gibt einen Unterschied zwischen', 'Serif', 11.6, CREME)
y -= 7.0 * mm
zeile(rx, y, 'Pflicht und Liebe.', 'SerifB', 13, GOLD_H)

y -= 10 * mm
c.setStrokeColor(GOLD); c.setLineWidth(0.6)
c.line(rx, y, rx + 28 * mm, y)
y -= 9.5 * mm

zeile(rx, y, 'Dieses Buch funktioniert auch an dem Tag,', 'SerifB', 11.4, CREME)
y -= 6.0 * mm
zeile(rx, y, 'an dem du selbst ganz unten auf der Liste stehst.', 'SerifB', 11.4, CREME)
y -= 9 * mm

for t in ['Ein Selbsttest, der dir in zwei Minuten sagt, wo du stehst',
          'Notfall-Seiten für Tage, an denen gar nichts geht',
          'Der Pflicht-oder-Liebe-Check für jede Entscheidung',
          'Dein persönlicher Satz-Baukasten zum Nachschlagen',
          'Ein Rückfall-Notfallplan für den Tag, an dem das alte Muster zurückkommt']:
    c.setFillColor(GOLD)
    c.circle(rx + 1.3 * mm, y + 1.2 * mm, 0.85 * mm, fill=1, stroke=0)
    zeile(rx + 5.4 * mm, y, t, 'Serif', 10.2, CREME)
    y -= 5.9 * mm

y -= 5 * mm
gesperrt(rx, y, 'SEHEN · WÄHLEN · GRENZEN · RÜCKKEHR ZU DIR',
         'Sans', 7.6, GOLD, 0.8)

y -= 11 * mm
for t in ('Du darfst an dich denken.', 'Du darfst Erste sein.', 'Du darfst du sein.'):
    zeile(rx, y, t, 'SerifB', 11.8, WEIN)
    y -= 6.2 * mm

vy = BLEED + SAFE + 12 * mm
block(rx, vy, ['Petra Tanner, Coachin.',
               'Safe to Thrive, Schweiz.'], 'SerifI', 9.2, GRAU, 5.0 * mm)

c.setFillColor(colors.white)
c.rect(RUECK_X + TRIM_B - SAFE - 52 * mm, BLEED + SAFE, 52 * mm, BARCODE_H,
       fill=1, stroke=0)

print(f'  Rueckseite endet bei {(y)/mm:.1f} mm, Barcodezone ab '
      f'{(BLEED + SAFE + BARCODE_H)/mm:.1f} mm')

c.showPage()
c.save()

print(f'Cover erstellt: {OUT}')
print(f'  Seiten {SEITEN} | Rücken {RUECKEN/mm:.2f} mm')
print(f'  Gesamt {W/mm:.2f} x {H/mm:.2f} mm')
