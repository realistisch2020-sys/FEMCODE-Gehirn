# -*- coding: utf-8 -*-
"""Baut den Journal-Vollwrap neu: Vorderseite = das aktuelle Buchcover
(korrekter Titel schon drin) + 'Das Journal'-Abzeichen, Rueckseite neu
gestaltet passend dazu, Ruecken auf 79 Seiten kalibriert."""
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit, ImageReader
from PIL import Image

FD = '/usr/share/fonts/truetype/liberation/'
for name, fn in [('Serif', 'LiberationSerif-Regular.ttf'),
                  ('Serif-Bold', 'LiberationSerif-Bold.ttf'),
                  ('Serif-It', 'LiberationSerif-Italic.ttf'),
                  ('Sans', 'LiberationSans-Regular.ttf'),
                  ('Sans-Bold', 'LiberationSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, FD + fn))

PAGES = 79
SPINE_MM = PAGES * 0.0025 * 25.4
BLEED = 3.2
TRIM_W, TRIM_H = 139.7, 215.9
PANEL_W = BLEED + TRIM_W  # 142.9mm
TOTAL_W = PANEL_W * 2 + SPINE_MM
TOTAL_H = TRIM_H + 2 * BLEED

OUT_PDF = "/home/user/FEMCODE-Gehirn/outputs/buch-an-mich-denken/journal-Cover-Print-FullWrap.pdf"
OUT_PNG = "/home/user/FEMCODE-Gehirn/outputs/buch-an-mich-denken/journal-Cover-Print-FullWrap.png"
FRONT_ART = "/home/user/FEMCODE-Gehirn/outputs/buch-an-mich-denken/buch4-eBook-Cover.jpg"

INK = HexColor('#150F1A')
GOLD = HexColor('#C99A43')
WINE = HexColor('#8C3563')
CREAM = HexColor('#F5EFE3')
WHITE = HexColor('#FFFFFF')

c = canvas.Canvas(OUT_PDF, pagesize=(TOTAL_W * mm, TOTAL_H * mm))
W = TOTAL_W * mm
H = TOTAL_H * mm

# --- Hintergrund fuellen (Ink, damit Rand/Bleed nie weiss ist) ---
c.setFillColor(INK)
c.rect(0, 0, W, H, fill=1, stroke=0)

# --- Rueckseite (links): Panel von x=0 bis PANEL_W ---
back_w = PANEL_W * mm
c.setFillColor(INK)
c.rect(0, 0, back_w, H, fill=1, stroke=0)

margin = (BLEED + 12) * mm
text_w = back_w - 2 * margin

def wrapped(text, x, y, width, font, size, leading, color, align='left'):
    lines = simpleSplit(text, font, size, width)
    c.setFont(font, size)
    c.setFillColor(color)
    for line in lines:
        if align == 'center':
            c.drawCentredString(x + width / 2, y, line)
        else:
            c.drawString(x, y, line)
        y -= leading
    return y

y = H - (BLEED + 30) * mm
c.setFont('Serif-Bold', 20)
c.setFillColor(CREAM)
for line in ["Ich stand nie auf", "meiner eigenen Liste", "— Das Journal"]:
    c.drawString(margin, y, line)
    y -= 9 * mm
y -= 6 * mm
y = wrapped("Ein Buch kann dir zeigen, woher dein Selbstvergessen kommt. "
            "Aber verändern tut sich etwas erst dort, wo du selbst schreibst.",
            margin, y, text_w, 'Sans', 11, 5.2 * mm, WHITE)
y -= 5 * mm
y = wrapped("Zu jedem der über 30 Kapitel findest du eine kurze Einordnung, "
            "Reflexionsfragen mit Schreibraum und eine kleine Übung — dazu "
            "eine Checkliste, drei Schritte durch den Prozess und eine "
            "Standortbestimmung am Ende.",
            margin, y, text_w, 'Sans', 11, 5.2 * mm, WHITE)
y -= 5 * mm
y = wrapped("Kein Test. Keine Hausaufgabe. Ein Ort, an dem deine eigenen "
            "Antworten stehen dürfen.",
            margin, y, text_w, 'Serif-It', 10.5, 5.0 * mm, GOLD)

c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(margin, (BLEED + 18) * mm, margin + 28 * mm, (BLEED + 18) * mm)
c.setFont('Serif-Bold', 12)
c.setFillColor(GOLD)
c.drawString(margin, (BLEED + 12) * mm, "PETRA TANNER")
c.setFont('Sans', 9.5)
c.setFillColor(WHITE)
c.drawString(margin, (BLEED + 7) * mm, "SAFE TO THRIVE")

# --- Ruecken (Mitte) ---
spine_x = back_w
spine_w = SPINE_MM * mm
c.setFillColor(INK)
c.rect(spine_x, 0, spine_w, H, fill=1, stroke=0)
c.saveState()
c.translate(spine_x + spine_w / 2, H / 2)
c.rotate(90)
c.setFont('Serif-Bold', 8.2)
c.setFillColor(CREAM)
c.drawCentredString(0, -2.6, "Ich stand nie auf meiner eigenen Liste  ·  Das Journal  ·  Petra Tanner")
c.restoreState()

# --- Vorderseite (rechts): vorhandenes Buchcover + Journal-Abzeichen ---
front_x = spine_x + spine_w
front_w = PANEL_W * mm
img = Image.open(FRONT_ART)
iw, ih = img.size
target_ratio = PANEL_W / TOTAL_H
src_ratio = iw / ih
if src_ratio > target_ratio:
    new_w = int(ih * target_ratio)
    left = (iw - new_w) // 2
    img = img.crop((left, 0, left + new_w, ih))
else:
    new_h = int(iw / target_ratio)
    top = (ih - new_h) // 2
    img = img.crop((0, top, iw, top + new_h))
tmp_path = "/tmp/claude-0/-home-user-FEMCODE-Gehirn/30ffe3fe-b993-5341-8e2e-05e8f5ff8752/scratchpad/_front_fit.jpg"
img.save(tmp_path, quality=95)
c.drawImage(ImageReader(tmp_path), front_x, 0, width=front_w, height=H)

# Journal-Abzeichen im freien Raum zwischen Untertitel und Autorenzeile
# (Untertitel liegt bei ca. 52-64mm von unten, Autorenzeile bei ca. 15-25mm
# von unten, im Original-Coverbild -- Luecke dazwischen nutzen)
badge_cx = front_x + front_w / 2
badge_cy = 38 * mm
badge_r = 11 * mm
c.setFillColor(INK)
c.circle(badge_cx, badge_cy, badge_r, fill=1, stroke=0)
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.circle(badge_cx, badge_cy, badge_r, fill=0, stroke=1)
c.setFont('Sans-Bold', 6.4)
c.setFillColor(GOLD)
for i, line in enumerate(["DAS", "JOURNAL", "ZUM BUCH"]):
    c.drawCentredString(badge_cx, badge_cy + (1 - i) * 3.0 * mm - 1.0 * mm, line)

c.save()
print("Journal-Cover PDF erstellt:", OUT_PDF)
print("Masse:", TOTAL_W, "x", TOTAL_H, "mm, Ruecken", SPINE_MM, "mm")

# PNG-Export fuer Kontrolle
import pymupdf
d = pymupdf.open(OUT_PDF)
pix = d[0].get_pixmap(matrix=pymupdf.Matrix(300 / 72, 300 / 72))
pix.save(OUT_PNG)
print("PNG gespeichert:", OUT_PNG, pix.width, pix.height)
