# -*- coding: utf-8 -*-
"""Druckfertiges Full-Wrap-Cover fuer KDP: 'Meine Lust ist nicht weg.
Nur DU erreichst mich nicht mehr.', mit fertigem Vorderseiten-Bild.
Rueckseite und Ruecken typografisch, Terracotta/Rose-Palette passend
zum Vorderseiten-Foto.

    python3 tools/buch7-cover-foto.py <bild.png> [seitenzahl]
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

OUT = '/home/user/FEMCODE-Gehirn/outputs/buch7/buch7-Cover-FullWrap.pdf'
BILD = sys.argv[1] if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else None
if not BILD:
    raise SystemExit('Bilddatei als Argument angeben.')

# ─── Masse ──────────────────────────────────────────────────────────────────
SEITEN  = int(sys.argv[2]) if len(sys.argv) > 2 else 130   # Platzhalter bis Manuskript steht
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

# ─── Farben: Nacht / Terracotta / Rose (wie Vorderseiten-Foto) ──────────────
NACHT   = colors.HexColor('#1A1512')
TIEFE   = colors.HexColor('#100D0B')
CREME   = colors.HexColor('#FAF3EC')
TERRA   = colors.HexColor('#C97B5A')
TERRA_H = colors.HexColor('#E8A98A')
ROSE    = colors.HexColor('#E8C4B0')
GRAU    = colors.HexColor('#A89A90')

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
# Titel/Untertitel sind bereits im Bild eingebrannt -> keine eigene
# Typografie dafuer. Autorinnen-Signatur (Markenzeichen der Reihe) fehlt
# im Bild und wird hier ergaenzt, kompakt ganz unten, unterhalb des im
# Bild bereits vorhandenen Untertitels.
fm = FRONT_X + TRIM_B / 2
sy = BLEED + 10 * mm
gesperrt(fm, sy, 'PETRA TANNER', 'SansB', 10.5, CREME, 2.6, mitte=True)
gesperrt(fm, sy - 5.5 * mm, 'SAFE TO THRIVE', 'Sans', 7.0, TERRA_H, 3.0, mitte=True)

# ════════════════════════════════════════════════════════════════════════════
# BUCHRÜCKEN
# ════════════════════════════════════════════════════════════════════════════
c.saveState()
c.translate(SPINE_X + RUECKEN / 2, H / 2)
c.rotate(-90)
zeile(-H / 2 + 30 * mm, -2.4, 'MEINE LUST IST NICHT WEG. NUR DU ERREICHST MICH NICHT MEHR.',
      'SansB', 7.6, CREME)
zeile(H / 2 - 30 * mm, -2.4, 'PETRA TANNER', 'Sans', 7.4, TERRA_H, rechts=True)
c.restoreState()

# ════════════════════════════════════════════════════════════════════════════
# RÜCKSEITE
# ════════════════════════════════════════════════════════════════════════════
rx = RUECK_X + SAFE + 7 * mm
y  = H - BLEED - 18 * mm
BARCODE_H = 32 * mm

gesperrt(rx, y, 'FÜR FRAUEN, DIE SICH VERSTEHEN WOLLEN.', 'SansB', 7.6, TERRA_H, 1.0)
y -= 5 * mm
gesperrt(rx, y, 'FÜR MÄNNER, DIE SIE VERSTEHEN WOLLEN.', 'SansB', 7.6, TERRA_H, 1.0)
y -= 13 * mm

y = block(rx, y, [
    'Du liebst ihn noch. Aber dein Körper sagt manchmal Nein.',
    'Und du weisst nicht mehr, ob das an dir liegt,',
    'an ihm, oder an allem, was dazwischen liegt.'], 'Serif', 11.4, CREME, 6.0 * mm)

y -= 9 * mm
zeile(rx, y, 'Deine Lust ist nicht weg.', 'SerifB', 13, TERRA_H)
y -= 7.2 * mm
zeile(rx, y, 'Sie hat nur aufgehört, ihn zu erreichen.', 'SerifB', 13, TERRA_H)

y -= 10 * mm
c.setStrokeColor(TERRA); c.setLineWidth(0.6)
c.line(rx, y, rx + 28 * mm, y)
y -= 9.5 * mm

zeile(rx, y, 'Petra Tanner zeigt dir, was Erschöpfung,', 'SerifB', 11.2, CREME)
y -= 6.0 * mm
zeile(rx, y, 'Mental Load und Nähe wirklich miteinander zu tun haben.', 'SerifB', 11.2, CREME)
y -= 9 * mm

for t in ['Warum Begehren oft partnerspezifisch verschwindet, nicht generell',
          'Was Berührung zu einer weiteren Aufgabe macht, statt zu Nähe',
          'Ein eigenes Kapitel für ihn: was du tun kannst, und was nicht',
          'Konkrete Übungen statt vager Ratschläge',
          'Kein Sex-Ratgeber. Ein Buch über Nähe, Erschöpfung und dich']:
    c.setFillColor(TERRA)
    c.circle(rx + 1.3 * mm, y + 1.2 * mm, 0.85 * mm, fill=1, stroke=0)
    zeile(rx + 5.4 * mm, y, t, 'Serif', 10.0, CREME)
    y -= 5.9 * mm

y -= 5 * mm
gesperrt(rx, y, 'NÄHE · ERSCHÖPFUNG · BEGEHREN · VERSTEHEN',
         'Sans', 7.2, TERRA_H, 0.6)

y -= 11 * mm
for t in ('Du bist nicht unattraktiv geworden.', 'Du bist erschöpft geworden.'):
    zeile(rx, y, t, 'SerifB', 11.6, ROSE)
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
