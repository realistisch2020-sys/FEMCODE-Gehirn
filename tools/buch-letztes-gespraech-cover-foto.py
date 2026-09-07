# -*- coding: utf-8 -*-
"""Druckfertiges Full-Wrap-Cover fuer KDP: 'Du brauchst kein letztes Gespraech',
mit fertigem Vorderseiten-Bild (Foto statt reiner Typografie). Rueckseite und
Ruecken wie im typografischen Cover, nur die Vorderseite kommt aus der Bilddatei.

    python3 tools/buch-letztes-gespraech-cover-foto.py <bild.png>
"""
import sys, os
from reportlab.pdfgen import canvas as rl
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
from reportlab import rl_config

OUT = '/home/user/FEMCODE-Gehirn/outputs/buch-letztes-gespraech/buch-Cover-FullWrap-Foto.pdf'
BILD = sys.argv[1] if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else None
if not BILD:
    raise SystemExit('Bilddatei als Argument angeben.')

# ─── Masse ──────────────────────────────────────────────────────────────────
SEITEN  = 113
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

# ─── Farben: Duesterblau / Gold / Terracotta (wie typografisches Cover) ─────
NACHT   = colors.HexColor('#1A2137')
TIEFE   = colors.HexColor('#10152A')
CREME   = colors.HexColor('#FAF6F0')
GOLD    = colors.HexColor('#C9A24A')
GOLD_H  = colors.HexColor('#E8C877')
TERRA   = colors.HexColor('#C97B5A')
TERRA_H = colors.HexColor('#DFA083')
GRAU    = colors.HexColor('#8A93A8')

F = '/usr/share/fonts/truetype/liberation/'
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
c.setFillColor(TIEFE)
c.rect(0, 0, SPINE_X, H, fill=1, stroke=0)


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


# ════════════════════════════════════════════════════════════════════════════
# VORDERSEITE: fertiges Bild, randlos, mittig beschnitten
# ════════════════════════════════════════════════════════════════════════════
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
      + ('' if dpi >= 300 else '   ACHTUNG: unter 300 dpi, im Druck evtl. unscharf'))

# ════════════════════════════════════════════════════════════════════════════
# BUCHRÜCKEN
# ════════════════════════════════════════════════════════════════════════════
c.saveState()
c.translate(SPINE_X + RUECKEN / 2, H / 2)
c.rotate(-90)
zeile(-H / 2 + 30 * mm, -2.4, 'DU BRAUCHST KEIN LETZTES GESPRÄCH', 'SansB', 8.2, CREME)
zeile(H / 2 - 30 * mm, -2.4, 'PETRA TANNER', 'Sans', 7.4, GOLD, rechts=True)
c.restoreState()

# ════════════════════════════════════════════════════════════════════════════
# RÜCKSEITE
# ════════════════════════════════════════════════════════════════════════════
rx = RUECK_X + SAFE + 7 * mm
y  = H - BLEED - 18 * mm
BARCODE_H = 32 * mm

gesperrt(rx, y, 'FÜR ALLE, DIE NOCH AUF EINE ANTWORT WARTEN.', 'SansB', 7.6, GOLD, 1.2)
y -= 12 * mm

y = block(rx, y, [
    'Vielleicht wartest du seit Jahren auf eine Erklärung.',
    'Auf eine Entschuldigung. Auf das eine Gespräch,',
    'das alles klären würde.',
    'Es kommt vielleicht nie.'], 'Serif', 11.4, CREME, 6.0 * mm)

y -= 9 * mm
zeile(rx, y, 'Und trotzdem darfst du frei werden.', 'SerifB', 13, TERRA_H)

y -= 10 * mm
c.setStrokeColor(GOLD); c.setLineWidth(0.6)
c.line(rx, y, rx + 28 * mm, y)
y -= 9.5 * mm

zeile(rx, y, 'Petra Tanner zeigt dir vier Schritte zurück zu dir,', 'SerifB', 11.2, CREME)
y -= 6.0 * mm
zeile(rx, y, 'ganz ohne das Gespräch, auf das du wartest.', 'SerifB', 11.2, CREME)
y -= 9 * mm

for t in ['Warum das Verhalten der anderen Person bereits eine Antwort war',
          'Wie du deiner eigenen Wahrnehmung wieder vertraust',
          'Ein Zwölf-Wochen-Plan, ein Schritt pro Woche',
          'Über dreissig Geschichten von Menschen, die diesen Weg gegangen sind',
          'Übungen für Familie, Freundschaft, Trennung und Trauer']:
    c.setFillColor(GOLD)
    c.circle(rx + 1.3 * mm, y + 1.2 * mm, 0.85 * mm, fill=1, stroke=0)
    zeile(rx + 5.4 * mm, y, t, 'Serif', 10.2, CREME)
    y -= 5.9 * mm

y -= 5 * mm
gesperrt(rx, y, 'REALITÄT · VERANTWORTUNG · ABSCHLUSS · RÜCKKEHR ZU DIR',
         'Sans', 7.2, GOLD, 0.6)

y -= 11 * mm
for t in ('Du musst nicht verstehen, warum.', 'Du darfst trotzdem gehen.'):
    zeile(rx, y, t, 'SerifB', 11.6, TERRA_H)
    y -= 6.2 * mm

vy = BLEED + SAFE + 12 * mm
block(rx, vy, ['Petra Tanner, Autorin und Mentorin.',
               'Seit 26 Jahren in eigener Praxis.'], 'SerifI', 9.2, GRAU, 5.0 * mm)

c.setFillColor(colors.white)
c.rect(RUECK_X + TRIM_B - SAFE - 52 * mm, BLEED + SAFE, 52 * mm, BARCODE_H,
       fill=1, stroke=0)

c.showPage()
c.save()

print(f'Cover erstellt: {OUT}')
print(f'  Seiten {SEITEN} | Rücken {RUECKEN/mm:.2f} mm')
print(f'  Gesamt {W/mm:.2f} x {H/mm:.2f} mm')
