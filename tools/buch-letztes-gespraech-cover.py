# -*- coding: utf-8 -*-
"""Druckfertiges Full-Wrap-Cover fuer KDP: 'Du brauchst kein letztes Gespraech'.

Rein typografisch in Kintsugi-Anmutung: dunkler Duesterblau-Grund, feine
Goldadern, kein Foto. Exakte Masse fuer 159 Seiten auf Cremepapier.
"""
import math
from reportlab.pdfgen import canvas as rl
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config

OUT = '/home/user/FEMCODE-Gehirn/outputs/buch-letztes-gespraech/buch-Cover-FullWrap.pdf'

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

# ─── Farben: Duesterblau / Gold / Terracotta ───────────────────────────────
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

for i in range(140):
    t = i / 140.0
    c.setFillColorRGB(0.102 + 0.05 * (1 - t), 0.129 + 0.045 * (1 - t),
                      0.216 + 0.04 * (1 - t))
    c.rect(FRONT_X, H - (i + 1) * H / 140, TRIM_B + BLEED, H / 140 + 0.6,
           fill=1, stroke=0)

c.setFillColor(TIEFE)
c.rect(0, 0, SPINE_X, H, fill=1, stroke=0)


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
c.setStrokeAlpha(0.5)
ader(FRONT_X + TRIM_B - 5 * mm, H - BLEED + 2 * mm, 105 * mm, math.radians(268),
     breite=1.3, seed=7)
c.setStrokeAlpha(0.24)
ader(FRONT_X + TRIM_B - 8 * mm, BLEED - 3 * mm, 40 * mm, math.radians(96),
     breite=0.75, seed=21)
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


ty = H - BLEED - 34 * mm
ty = gruppe(['DU BRAUCHST', 'KEIN LETZTES'], innen * 0.90, CREME, ty, 1.02)
ty -= 6 * mm
ty = gruppe(['GESPRÄCH'], innen * 0.90, TERRA_H, ty, 1.02)

ty -= 9 * mm
c.setStrokeColor(GOLD); c.setLineWidth(1.0)
c.line(fx, ty, fx + 30 * mm, ty)

ty -= 12.5 * mm
block(fx, ty, ['Wie du innerlich frei wirst,',
               'auch wenn die Entschuldigung', 'nie kommt'],
      'Serif', 12.6, GOLD_H, 6.4 * mm)

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
