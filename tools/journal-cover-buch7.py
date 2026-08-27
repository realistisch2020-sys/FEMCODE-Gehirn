# -*- coding: utf-8 -*-
"""Baut den Journal-Vollwrap im gleichen Stil wie die Journal-Cover der
anderen 3 Buecher: Vorderseite ein sauberes Typo-Layout (Titel, Trennlinie
mit Oval, 'Das Journal', Untertitel, Autor), Ruecken ohne Text (bei so
schmalem Ruecken sonst Kollision mit der KDP-Beschnittlinie), Rueckseite
mit Blurb. Ruecken auf 79 Seiten kalibriert."""
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

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

INK = HexColor('#150F1A')
GOLD = HexColor('#C99A43')
CREAM = HexColor('#F5EFE3')
WHITE = HexColor('#FFFFFF')

c = canvas.Canvas(OUT_PDF, pagesize=(TOTAL_W * mm, TOTAL_H * mm))
W = TOTAL_W * mm
H = TOTAL_H * mm

c.setFillColor(INK)
c.rect(0, 0, W, H, fill=1, stroke=0)

back_w = PANEL_W * mm
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

# ============ Rueckseite (links) ============
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

# ============ Ruecken (Mitte) -- bewusst ohne Text ============
# Bei nur ~5mm Ruecken kollidiert jeder Text mit der KDP-Beschnittlinie.
# Die Journal-Cover der anderen Buecher lassen den Ruecken deshalb leer.
spine_x = back_w
spine_w = SPINE_MM * mm
c.setFillColor(INK)
c.rect(spine_x, 0, spine_w, H, fill=1, stroke=0)

# ============ Vorderseite (rechts): sauberes Typo-Cover ============
front_x = spine_x + spine_w
front_w = PANEL_W * mm
fmargin = (BLEED + 14) * mm
fw = front_w - 2 * fmargin
fcenter = front_x + front_w / 2

y = H - (BLEED + 34) * mm
c.setFont('Serif-Bold', 21)
c.setFillColor(CREAM)
for line in ["Ich stand nie auf", "meiner eigenen Liste"]:
    c.drawCentredString(fcenter, y, line)
    y -= 9.5 * mm

y -= 10 * mm
line_w = 30 * mm
c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(fcenter - line_w - 6 * mm, y, fcenter - 6 * mm, y)
c.line(fcenter + 6 * mm, y, fcenter + line_w + 6 * mm, y)
c.setStrokeColor(GOLD)
c.ellipse(fcenter - 4 * mm, y - 2 * mm, fcenter + 4 * mm, y + 2 * mm, fill=0, stroke=1)

y -= 16 * mm
c.setFont('Serif-Bold', 30)
c.setFillColor(GOLD)
c.drawCentredString(fcenter, y, "Das Journal")

y -= 12 * mm
c.setFont('Serif', 13)
c.setFillColor(WHITE)
c.drawCentredString(fcenter, y, "Dein Arbeitsbuch zum Buch")

c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(fcenter - 14 * mm, (BLEED + 18) * mm, fcenter + 14 * mm, (BLEED + 18) * mm)
c.setFont('Serif-Bold', 13)
c.setFillColor(WHITE)
c.drawCentredString(fcenter, (BLEED + 12) * mm, "PETRA TANNER")
c.setFont('Sans', 10)
c.setFillColor(GOLD)
c.drawCentredString(fcenter, (BLEED + 7) * mm, "SAFE TO THRIVE")

c.save()
print("Journal-Cover PDF erstellt:", OUT_PDF)
print("Masse:", TOTAL_W, "x", TOTAL_H, "mm, Ruecken", SPINE_MM, "mm")

import pymupdf
d = pymupdf.open(OUT_PDF)
pix = d[0].get_pixmap(matrix=pymupdf.Matrix(300 / 72, 300 / 72))
pix.save(OUT_PNG)
print("PNG gespeichert:", OUT_PNG, pix.width, pix.height)
