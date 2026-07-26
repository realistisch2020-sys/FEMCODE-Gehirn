# -*- coding: utf-8 -*-
"""Druckfertiges Full-Wrap-Cover fuer KDP.

Rein typografisch in Kintsugi-Anmutung: dunkler Grund, feine Goldadern,
kein Foto. Exakte Masse fuer 121 Seiten auf Cremepapier.
"""
import math, sys, os
from reportlab.pdfgen import canvas as rl
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = '/home/user/FEMCODE-Gehirn/outputs/buch6/buch6-Cover-FullWrap.pdf'
# Optional: fertiges Vorderseiten-Bild als Argument. Dann entfaellt meine Typografie.
BILD = sys.argv[1] if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else None

# ─── Masse ──────────────────────────────────────────────────────────────────
SEITEN   = 126
TRIM_B   = 139.7 * mm     # 5,5 Zoll
TRIM_H   = 215.9 * mm     # 8,5 Zoll
RUECKEN  = SEITEN * 0.0025 * 25.4 * mm     # Creme
BLEED    = 3.2 * mm
W = BLEED + TRIM_B + RUECKEN + TRIM_B + BLEED
H = BLEED + TRIM_H + BLEED

# Nullpunkte
RUECK_X  = BLEED                 # Rueckseite links
SPINE_X  = BLEED + TRIM_B
FRONT_X  = SPINE_X + RUECKEN
SAFE     = 6 * mm                # Sicherheitsabstand zur Schnittkante

# ─── Farben ─────────────────────────────────────────────────────────────────
NACHT  = colors.HexColor('#14100E')
TIEFE  = colors.HexColor('#0C0908')
CREME  = colors.HexColor('#F4EFE8')
ROSE   = colors.HexColor('#E8B49B')
GOLD   = colors.HexColor('#C9A227')
GOLD_H = colors.HexColor('#E3C766')
GRAU   = colors.HexColor('#9A8F8A')

# ─── Schriften ──────────────────────────────────────────────────────────────
F = '/usr/share/fonts/truetype/liberation/'
from reportlab import rl_config
pdfmetrics.registerFont(TTFont('Sans',   F + 'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SansB',  F + 'LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Serif',  F + 'LiberationSerif-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SerifI', F + 'LiberationSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('SerifB', F + 'LiberationSerif-Bold.ttf'))

# Grundschrift setzen, sonst schreibt ReportLab eine tote Helvetica-Referenz
# in die Datei und KDP meldet eine nicht eingebettete Schrift
rl_config.canvas_basefontname = 'Sans'

c = rl.Canvas(OUT, pagesize=(W, H))

# ─── Hintergrund ────────────────────────────────────────────────────────────
c.setFillColor(NACHT)
c.rect(0, 0, W, H, fill=1, stroke=0)

# leichter Lichtverlauf hinter dem Titelbereich
for i in range(140):
    t = i / 140.0
    c.setFillColorRGB(0.078 + 0.055 * (1 - t), 0.063 + 0.045 * (1 - t),
                      0.055 + 0.040 * (1 - t))
    c.rect(FRONT_X, H - (i + 1) * H / 140, TRIM_B + BLEED, H / 140 + 0.6,
           fill=1, stroke=0)

# Rueckseite minimal dunkler, damit sie ruhig bleibt
c.setFillColor(TIEFE)
c.rect(0, 0, SPINE_X, H, fill=1, stroke=0)


# ─── Goldadern (Kintsugi) ───────────────────────────────────────────────────
def ader(x, y, laenge, winkel, tiefe=0, breite=1.0, seed=0):
    """Kantiger Riss mit Gold gefuellt. Gerade Teilstuecke, harte Knicke."""
    if tiefe > 2 or laenge < 9 * mm:
        return
    schritte = 7
    px, py = x, y
    c.setLineCap(0)
    c.setLineJoin(0)
    for s in range(schritte):
        # harte, unregelmaessige Richtungswechsel statt weicher Kurve
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
c.setStrokeAlpha(0.0 if BILD else 0.55)
# ein durchgehender Bruch von oben rechts nach unten, mit wenigen Abzweigen
ader(FRONT_X + TRIM_B + 2 * mm, H - 8 * mm, 60 * mm, math.radians(249),
     breite=1.15, seed=3)
c.setStrokeAlpha(0.34)
ader(FRONT_X + TRIM_B + 2 * mm, H * 0.42, 42 * mm, math.radians(205),
     breite=0.85, seed=17)
c.setStrokeAlpha(0.22)
ader(FRONT_X + TRIM_B * 0.62, BLEED - 2 * mm, 34 * mm, math.radians(78),
     breite=0.7, seed=29)
c.restoreState()


# ─── Hilfsfunktionen ────────────────────────────────────────────────────────
def sperr(text, abstand):
    return (' ' * 0).join(text)  # Platzhalter, echte Sperrung unten


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
# VORDERSEITE
# ════════════════════════════════════════════════════════════════════════════
if BILD:
    # Fertiges Cover randlos einsetzen, mittig beschnitten
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
    dpi = iw / (fw / 72 / 25.4 * 25.4 / 25.4) if False else iw / (fw / mm / 25.4)
    print(f'  Bild eingesetzt: {iw}x{ih} px  ->  {dpi:.0f} dpi'
          + ('' if dpi >= 300 else '   ACHTUNG: unter 300 dpi'))

fx = FRONT_X + SAFE + 4 * mm
fm = FRONT_X + TRIM_B / 2          # Mitte der Vorderseite

if not BILD:
    # Kopfzeile: Marke
    gesperrt(fx, H - BLEED - 20 * mm, 'SAFE TO THRIVE', 'Sans', 8.6, GOLD, 3.4)
    gesperrt(fx, H - BLEED - 26.5 * mm, 'PETRA TANNER', 'Sans', 6.6, GRAU, 2.6)

    # Titel
    ty = H - BLEED - 46 * mm
    for t in ('ICH BIN', 'SO MÜDE.'):
        zeile(fx, ty, t, 'SansB', 40, CREME)
        ty -= 13.6 * mm
    for t in ('UND NIEMAND', 'FRAGT MICH', 'WARUM.'):
        zeile(fx, ty, t, 'SansB', 29, ROSE)
        ty -= 10.2 * mm

    # Goldlinie
    ty -= 5 * mm
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.9)
    c.line(fx, ty, fx + 34 * mm, ty)

    # Konzept
    ty -= 11 * mm
    zeile(fx, ty, 'Das Funktions-Ich', 'SerifB', 21, GOLD_H)
    ty -= 8.6 * mm
    block(fx, ty, ['Wenn du für alle stark bist',
                   'und dich dabei selbst verlierst'], 'Serif', 12.6, CREME, 6.2 * mm)

    # Autorin unten
    zeile(fx, BLEED + 17 * mm, 'PETRA TANNER', 'SansB', 15, CREME)

    # Störer: das Alleinstellungsmerkmal
    bx, by, br = FRONT_X + TRIM_B - 29 * mm, BLEED + 40 * mm, 19.5 * mm
    c.setFillColor(ROSE)
    c.circle(bx, by, br, fill=1, stroke=0)
    c.setStrokeColor(NACHT); c.setLineWidth(0.7)
    c.circle(bx, by, br - 2.2 * mm, fill=0, stroke=1)
    for i, t in enumerate(['MIT SELBSTTEST', 'UND DEN SÄTZEN,', 'DIE DU WIRKLICH', 'SAGST']):
        gesperrt(bx, by + 5.8 * mm - i * 4.1 * mm, t, 'SansB', 6.6, NACHT, 0.4, mitte=True)


# ════════════════════════════════════════════════════════════════════════════
# BUCHRÜCKEN
# ════════════════════════════════════════════════════════════════════════════
c.saveState()
c.translate(SPINE_X + RUECKEN / 2, H / 2)
c.rotate(-90)
zeile(-H / 2 + 30 * mm, -2.4, 'ICH BIN SO MÜDE. UND NIEMAND FRAGT MICH WARUM',
      'SansB', 8.4, CREME)
zeile(H / 2 - 30 * mm, -2.4, 'PETRA TANNER', 'Sans', 7.4, GOLD, rechts=True)
c.restoreState()


# ════════════════════════════════════════════════════════════════════════════
# RÜCKSEITE
# ════════════════════════════════════════════════════════════════════════════
rx = RUECK_X + SAFE + 7 * mm
y  = H - BLEED - 18 * mm
BARCODE_H = 32 * mm          # unten rechts fuer KDP freihalten

# Kopfzeile
gesperrt(rx, y, 'FÜR FRAUEN, DIE FÜR ALLE DA SIND.', 'SansB', 7.8, GOLD, 1.4)
y -= 4.8 * mm
gesperrt(rx, y, 'NUR NICHT FÜR SICH.', 'SansB', 7.8, GOLD, 1.4)
y -= 13 * mm

y = block(rx, y, [
 'Du funktionierst.',
 'Du bist für alle da.',
 'Und irgendwann sitzt du nachts da und denkst:',
 'Wie lange noch, bis ich nicht mehr kann?'], 'Serif', 11.6, CREME, 6.0 * mm)

y -= 9 * mm
zeile(rx, y, 'Es gibt einen Namen dafür.', 'Serif', 11.6, CREME)
y -= 7.4 * mm
zeile(rx, y, 'Das Funktions-Ich.', 'SerifB', 13, GOLD_H)

y -= 10 * mm
c.setStrokeColor(GOLD); c.setLineWidth(0.6)
c.line(rx, y, rx + 28 * mm, y)
y -= 9.5 * mm

zeile(rx, y, 'Dieses Buch funktioniert auch an dem Tag,', 'SerifB', 11.4, CREME)
y -= 6.0 * mm
zeile(rx, y, 'an dem du gar nichts kannst.', 'SerifB', 11.4, CREME)
y -= 9 * mm

for t in ['Ein Selbsttest, der dir in zwei Minuten sagt, wo du stehst',
          'Notfall-Seiten für nachts um drei und für das Auto',
          'Die Sätze zum Nachschlagen, wörtlich, für neun Situationen',
          'Was du sagst, wenn der andere nicht mitmacht',
          'Ein Kapitel für den Tag, an dem du zurückfällst']:
    c.setFillColor(GOLD)
    c.circle(rx + 1.3 * mm, y + 1.2 * mm, 0.85 * mm, fill=1, stroke=0)
    zeile(rx + 5.4 * mm, y, t, 'Serif', 10.4, CREME)
    y -= 5.9 * mm

y -= 5 * mm
gesperrt(rx, y, 'SEHEN · VERSTEHEN · ERLAUBEN · LERNEN · WERDEN',
         'Sans', 7.7, GOLD, 0.8)

y -= 11 * mm
for t in ('Du darfst aufhören.', 'Du darfst müde sein.', 'Du darfst du sein.'):
    zeile(rx, y, t, 'SerifB', 11.8, ROSE)
    y -= 6.2 * mm

# Vita unten links, neben dem Barcodefeld
vy = BLEED + SAFE + 12 * mm
block(rx, vy, ['Petra Tanner, Coachin.',
               'Seit 26 Jahren in eigener Praxis.'], 'SerifI', 9.2, GRAU, 5.0 * mm)

# Barcodefeld freihalten (KDP druckt ihn selbst)
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
