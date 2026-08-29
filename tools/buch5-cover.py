# -*- coding: utf-8 -*-
"""Druckfertiges Full-Wrap-Cover fuer Buch 5 "Deine Reaktion gehoert dir.
Nicht mir." Rein typografisch, Kintsugi-Anmutung (dunkles Petrol, feine
Goldadern), passend zur bereits fuer dieses Buch gewaehlten Farbrichtung
"Petrol & Gold". Kein Foto noetig."""
import math
from reportlab.pdfgen import canvas as rl
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config

OUT = '/home/user/FEMCODE-Gehirn/outputs/buch-reaktion/buch5-Cover-FullWrap.pdf'
BILD = '/home/user/FEMCODE-Gehirn/outputs/buch-reaktion/buch5-cover-front-source.png'

SEITEN = 100
TRIM_B = 139.7 * mm
TRIM_H = 215.9 * mm
RUECKEN = SEITEN * 0.0025 * 25.4 * mm
BLEED = 3.2 * mm
W = BLEED + TRIM_B + RUECKEN + TRIM_B + BLEED
H = BLEED + TRIM_H + BLEED

RUECK_X = BLEED
SPINE_X = BLEED + TRIM_B
FRONT_X = SPINE_X + RUECKEN
SAFE = 6 * mm

PETROL = colors.HexColor('#0E2B2E')
PETROL_TIEF = colors.HexColor('#081A1C')
CREME = colors.HexColor('#FAF6F0')
GOLD = colors.HexColor('#C99A43')
GOLD_H = colors.HexColor('#E8C877')
ROSE = colors.HexColor('#D9B48A')
GRAU = colors.HexColor('#8FA3A0')

F = '/usr/share/fonts/truetype/liberation/'
pdfmetrics.registerFont(TTFont('Sans', F + 'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SansB', F + 'LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Serif', F + 'LiberationSerif-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SerifI', F + 'LiberationSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('SerifB', F + 'LiberationSerif-Bold.ttf'))
rl_config.canvas_basefontname = 'Sans'

c = rl.Canvas(OUT, pagesize=(W, H))

c.setFillColor(PETROL)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(PETROL_TIEF)
c.rect(0, 0, SPINE_X, H, fill=1, stroke=0)

if BILD:
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


if not BILD:
    c.saveState()
    p = c.beginPath()
    p.rect(FRONT_X, 0, TRIM_B + BLEED, H)
    c.clipPath(p, stroke=0)
    c.setStrokeAlpha(0.85)
    ader(FRONT_X + TRIM_B - 14 * mm, H - BLEED + 2 * mm, 128 * mm, math.radians(252),
         breite=2.2, seed=7)
    c.setStrokeAlpha(0.35)
    ader(FRONT_X + TRIM_B - 36 * mm, BLEED - 3 * mm, 46 * mm, math.radians(70),
         breite=0.9, seed=21)
    c.restoreState()


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


# ═══════════════ VORDERSEITE ═══════════════
# Bei BILD ist Titel + Autor schon im Bild enthalten, keine eigene
# Typografie mehr noetig.
fx = FRONT_X + SAFE + 4 * mm
fm = FRONT_X + TRIM_B / 2
innen = TRIM_B - (SAFE + 4 * mm) - (SAFE + 3 * mm)

def gruppe(zeilen, breite, farbe, ty, durchschuss=1.03):
    g = min(fit(t, 'SansB', breite) for t in zeilen)
    for t in zeilen:
        zeile(fx, ty, t, 'SansB', g, farbe)
        ty -= g * durchschuss
    return ty

if not BILD:
    ty = H - BLEED - 32 * mm
    ty = gruppe(['DEINE REAKTION'], innen * 0.92, CREME, ty, 1.02)
    ty -= 6 * mm
    ty = gruppe(['GEHÖRT DIR.', 'NICHT MIR.'], innen * 0.80, GOLD_H, ty, 1.06)

    ty -= 9 * mm
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.0)
    c.line(fx, ty, fx + 30 * mm, ty)

    ty -= 12.5 * mm
    block(fx, ty, ['Warum du aufhören darfst, für die',
                   'Gefühle anderer verantwortlich zu sein'],
          'Serif', 12.6, CREME, 6.4 * mm)

    sy = BLEED + 20 * mm
    gesperrt(fm, sy, 'PETRA TANNER', 'SansB', 13.5, CREME, 3.6, mitte=True)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.7)
    c.line(fm - 26 * mm, sy - 5.2 * mm, fm + 26 * mm, sy - 5.2 * mm)
    gesperrt(fm, sy - 11.5 * mm, 'SAFE TO THRIVE', 'Sans', 8.2, GOLD, 3.8, mitte=True)

# ═══════════════ BUCHRÜCKEN ═══════════════
c.saveState()
c.translate(SPINE_X + RUECKEN / 2, H / 2)
c.rotate(-90)
zeile(-H / 2 + 30 * mm, -2.4, 'DEINE REAKTION GEHÖRT DIR. NICHT MIR.', 'SansB', 8.0, CREME)
zeile(H / 2 - 30 * mm, -2.4, 'PETRA TANNER', 'Sans', 7.4, GOLD, rechts=True)
c.restoreState()

# ═══════════════ RÜCKSEITE ═══════════════
rx = RUECK_X + SAFE + 7 * mm
y = H - BLEED - 18 * mm
BARCODE_H = 32 * mm

gesperrt(rx, y, 'FÜR DIE, DIE JEDE STIMMUNG IM RAUM SPÜREN.', 'SansB', 7.4, GOLD, 1.2)
y -= 4.8 * mm
gesperrt(rx, y, 'BEVOR SIE WISSEN, WIE ES IHNEN SELBST GEHT.', 'SansB', 7.4, GOLD, 1.2)
y -= 13 * mm

y = block(rx, y, [
    'Du spürst die Stille im Raum, bevor jemand',
    'etwas sagt. Du erklärst dich, bevor dich',
    'jemand gefragt hat. Und wenn ein anderer',
    'schlecht gelaunt ist, fühlt es sich an wie',
    'deine Schuld.'], 'Serif', 11.2, CREME, 5.9 * mm)

y -= 9 * mm
zeile(rx, y, 'Das hat einen Namen.', 'Serif', 11.6, CREME)
y -= 7.4 * mm
zeile(rx, y, 'Die Reaktionsübernahme.', 'SerifB', 13, GOLD_H)

y -= 10 * mm
c.setStrokeColor(GOLD)
c.setLineWidth(0.6)
c.line(rx, y, rx + 28 * mm, y)
y -= 9.5 * mm

zeile(rx, y, 'Dieses Buch zeigt dir, wie du aufhörst,', 'SerifB', 11.2, CREME)
y -= 6.0 * mm
zeile(rx, y, 'für Gefühle zu sorgen, die nicht deine sind.', 'SerifB', 11.2, CREME)
y -= 9 * mm

for t in ['Woher die Reaktionsübernahme wirklich kommt',
          'Der Unterschied zwischen Empathie und Verschmelzung',
          'Grenzen setzen, ohne dich zu erklären',
          'Was passiert, wenn du aufhörst zu retten',
          'Ein Kapitel für den Tag, an dem du zurückfällst']:
    c.setFillColor(GOLD)
    c.circle(rx + 1.3 * mm, y + 1.2 * mm, 0.85 * mm, fill=1, stroke=0)
    zeile(rx + 5.4 * mm, y, t, 'Serif', 10.0, CREME)
    y -= 5.7 * mm

y -= 5 * mm
gesperrt(rx, y, 'SEHEN · VERSTEHEN · LOSLASSEN · WERDEN', 'Sans', 7.7, GOLD, 0.8)

y -= 11 * mm
for t in ('Ihre Reaktion gehört ihr.', 'Deine gehört dir.'):
    zeile(rx, y, t, 'SerifB', 11.8, ROSE)
    y -= 6.2 * mm

vy = BLEED + SAFE + 12 * mm
block(rx, vy, ['Petra Tanner, Coachin.',
               'Safe to Thrive.'], 'SerifI', 9.2, GRAU, 5.0 * mm)

c.setFillColor(colors.white)
c.rect(RUECK_X + TRIM_B - SAFE - 52 * mm, BLEED + SAFE, 52 * mm, BARCODE_H,
       fill=1, stroke=0)

c.showPage()
c.save()

print(f'Cover erstellt: {OUT}')
print(f'  Seiten {SEITEN} | Rücken {RUECKEN/mm:.2f} mm')
print(f'  Gesamt {W/mm:.2f} x {H/mm:.2f} mm')
