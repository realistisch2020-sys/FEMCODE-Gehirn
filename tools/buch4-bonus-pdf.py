# -*- coding: utf-8 -*-
"""Huebsches, farbiges Bonus-PDF (Freebie) fuer Buch 4, A4, fuer Tentary."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

FD = '/usr/share/fonts/truetype/liberation/'
pdfmetrics.registerFont(TTFont('Serif', FD + 'LiberationSerif-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Serif-Bold', FD + 'LiberationSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Serif-It', FD + 'LiberationSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Sans', FD + 'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Sans-Bold', FD + 'LiberationSans-Bold.ttf'))

W, H = A4
OUT = "/home/user/FEMCODE-Gehirn/outputs/buch-an-mich-denken/buch4-Bonus-PDF.pdf"

# --- Palette: warm, weich, modern ---
CREAM = HexColor('#FBF3EC')
ROSE = HexColor('#CC8577')
ROSE_DARK = HexColor('#B36657')
ROSE_LIGHT = HexColor('#F3DCD3')
SAGE = HexColor('#7C9A76')
SAGE_DARK = HexColor('#5F7C59')
SAGE_LIGHT = HexColor('#E4EAE0')
PLUM = HexColor('#4A3538')
WHITE = HexColor('#FFFFFF')
LINE = HexColor('#D8C3B9')

MARGIN = 22 * mm

def heart(c, x, y, s, color):
    c.saveState()
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x - 1.45 * s, y + 1.05 * s, x - 0.80 * s, y + 2.15 * s, x, y + 1.35 * s)
    p.curveTo(x + 0.80 * s, y + 2.15 * s, x + 1.45 * s, y + 1.05 * s, x, y)
    p.close()
    c.setFillColor(color)
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()

def rounded(c, x, y, w, h, r, fill, stroke=None):
    c.saveState()
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(1)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)
    c.restoreState()

def bg(c, color=CREAM):
    c.setFillColor(color)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def footer(c, page_no, label, color=ROSE_DARK):
    c.saveState()
    c.setFont('Sans', 8.5)
    c.setFillColor(color)
    c.drawString(MARGIN, 14 * mm, label)
    c.drawRightString(W - MARGIN, 14 * mm, str(page_no))
    heart(c, W / 2, 12.7 * mm, 1.6, SAGE)
    c.restoreState()

def wrapped(c, text, x, y, width, font, size, leading, color=PLUM, align='left'):
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

def blank_line(c, x, y, w, color=LINE):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(1.1)
    c.setDash(1, 2)
    c.line(x, y, x + w, y)
    c.restoreState()

def number_badge(c, x, y, r, num, color=ROSE):
    c.saveState()
    c.setFillColor(color)
    c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont('Serif-Bold', r * 1.15)
    c.drawCentredString(x, y - r * 0.38, str(num))
    c.restoreState()

def section_header(c, num, title_text, note, color, tint):
    bg(c)
    rounded(c, MARGIN, H - 46 * mm, W - 2 * MARGIN, 28 * mm, 6 * mm, tint)
    number_badge(c, MARGIN + 18 * mm, H - 32 * mm, 9 * mm, num, color)
    c.setFont('Serif-Bold', 17)
    c.setFillColor(PLUM)
    c.drawString(MARGIN + 34 * mm, H - 29 * mm, title_text)
    y0 = H - 60 * mm
    y0 = wrapped(c, note, MARGIN, y0, W - 2 * MARGIN, 'Sans', 11.5, 16.5)
    return y0 - 8 * mm


c = canvas.Canvas(OUT, pagesize=A4)

# ============ Seite 1: Cover ============
bg(c)
rounded(c, 0, H - 118 * mm, W, 118 * mm, 0, ROSE)
heart(c, W / 2, H - 40 * mm, 4.2, WHITE)
c.setFont('Sans-Bold', 13)
c.setFillColor(HexColor('#FBEDE7'))
c.drawCentredString(W / 2, H - 58 * mm, "D E I N   B O N U S")
c.setFont('Serif-Bold', 28)
c.setFillColor(WHITE)
c.drawCentredString(W / 2, H - 75 * mm, "Vertiefende Übungen zu")
c.setFont('Serif-Bold', 25)
yy = H - 92 * mm
for l in ['„Ich stand nie auf', 'meiner eigenen Liste“']:
    c.drawCentredString(W / 2, yy, l)
    yy -= 10 * mm

rounded(c, W / 2 - 48 * mm, H - 152 * mm, 96 * mm, 17 * mm, 8 * mm, SAGE_LIGHT, stroke=SAGE)
c.setFont('Sans', 11.5)
c.setFillColor(PLUM)
c.drawCentredString(W / 2, H - 145.5 * mm, "Sechs kurze Übungen für die Zeit")
c.drawCentredString(W / 2, H - 150.5 * mm, "nach dem Buch")

c.setFont('Serif-It', 15)
c.setFillColor(ROSE_DARK)
c.drawCentredString(W / 2, 55 * mm, "Petra Tanner")
c.setFont('Sans-Bold', 11)
c.setFillColor(SAGE_DARK)
c.drawCentredString(W / 2, 47 * mm, "SAFE TO THRIVE")
footer(c, 1, "Bonus-PDF")
c.showPage()

# ============ Seite 2: Willkommen ============
bg(c)
rounded(c, MARGIN, H - 62 * mm, W - 2 * MARGIN, 34 * mm, 6 * mm, ROSE_LIGHT)
c.setFont('Serif-Bold', 19)
c.setFillColor(ROSE_DARK)
c.drawCentredString(W / 2, H - 40 * mm, "Danke, dass du dieses Buch")
c.drawCentredString(W / 2, H - 48 * mm, "gelesen hast")
y = H - 76 * mm
intro = ("Dieses Bonus-PDF ist keine Fortsetzung, sondern eine Vertiefung. Sechs "
         "kurze Übungen, die du direkt ausfüllen kannst, für die Wochen nach dem "
         "Buch, wenn der erste Schwung nachlässt und die eigentliche Arbeit beginnt.")
y = wrapped(c, intro, MARGIN, y, W - 2 * MARGIN, 'Sans', 12, 17)
y -= 5 * mm
intro2 = ("Nimm dir für jede Übung so viel Zeit, wie du brauchst. Es gibt keine "
          "feste Reihenfolge und kein Richtig oder Falsch.")
y = wrapped(c, intro2, MARGIN, y, W - 2 * MARGIN, 'Sans', 12, 17)

y -= 12 * mm
box_h = 58 * mm
rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, SAGE_LIGHT)
c.setFont('Serif-Bold', 13.5)
c.setFillColor(SAGE_DARK)
c.drawString(MARGIN + 8 * mm, y - 10 * mm, "Was dich erwartet")
items = [
    "1.  Deine Liste, neu geschrieben",
    "2.  Der Pflicht-oder-Liebe-Check",
    "3.  Dein persönlicher Satz-Baukasten",
    "4.  Der Rückfall-Notfallplan",
    "5.  Die Drei-Monats-Standortbestimmung",
    "6.  Ein Satz an dich, drei Monate später",
]
yy = y - 19 * mm
c.setFont('Sans', 11.5)
c.setFillColor(PLUM)
for it in items:
    c.drawString(MARGIN + 8 * mm, yy, it)
    yy -= 6.6 * mm
footer(c, 2, "Bonus-PDF · Ich stand nie auf meiner eigenen Liste")
c.showPage()

# ============ Seite 3: Uebung 1 ============
y = section_header(c, 1, "Deine Liste, neu geschrieben",
    "Aus Kapitel 2 kennst du die Liste, die nie leer wird, weil sie fast "
    "ausschliesslich die Bedürfnisse anderer enthält. Diese Übung dreht das um: "
    "Schreib mindestens fünf Punkte auf, die ausschliesslich dich betreffen.",
    ROSE, ROSE_LIGHT)
box_h = 70 * mm
rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
yy = y - 15 * mm
for i in range(5):
    blank_line(c, MARGIN + 10 * mm, yy, W - 2 * MARGIN - 20 * mm)
    yy -= 11.5 * mm
note = ("Wiederhole diese Übung einmal im Monat. Vergleiche nach einem halben "
        "Jahr die erste mit der letzten Liste.")
wrapped(c, note, MARGIN, y - box_h - 10 * mm, W - 2 * MARGIN, 'Serif-It', 10.5, 14, color=ROSE_DARK)
footer(c, 3, "Übung 1", ROSE_DARK)
c.showPage()

# ============ Seite 4: Uebung 2 ============
y = section_header(c, 2, "Der Pflicht-oder-Liebe-Check",
    "Aus Kapitel 21: Nicht jede Handlung, die sich nach Liebe anfühlen soll, ist "
    "es auch. Nutze diese Tabelle eine Woche lang, für jede grössere Handlung, "
    "die du für jemand anderen tust.",
    SAGE, SAGE_LIGHT)
rows_h = 22 * mm
for i in range(3):
    top = y - i * (rows_h + 4 * mm)
    rounded(c, MARGIN, top - rows_h, W - 2 * MARGIN, rows_h, 5 * mm, WHITE, stroke=LINE)
    c.setFont('Sans-Bold', 10.5)
    c.setFillColor(SAGE_DARK)
    c.drawString(MARGIN + 7 * mm, top - 7 * mm, "Was ich getan habe")
    blank_line(c, MARGIN + 55 * mm, top - 8 * mm, W - 2 * MARGIN - 63 * mm)
    c.drawString(MARGIN + 7 * mm, top - 14 * mm, "Pflicht oder Liebe?")
    blank_line(c, MARGIN + 55 * mm, top - 15 * mm, 40 * mm)
    c.setFont('Sans', 9.5)
    c.setFillColor(PLUM)
    c.drawString(MARGIN + 100 * mm, top - 14 * mm, "Hätte ich es auch getan, wenn")
    c.drawString(MARGIN + 100 * mm, top - 18.5 * mm, "niemand es je erfahren hätte?  ja / nein")
footer(c, 4, "Übung 2", SAGE_DARK)
c.showPage()

# ============ Seite 5: Uebung 3 ============
y = section_header(c, 3, "Dein persönlicher Satz-Baukasten",
    "Die Satz-Sammlung am Ende des Buches enthält Sätze, die für viele "
    "funktionieren. Diese Übung ist deine eigene, private Version davon: drei "
    "Sätze, die dir schwerfallen, die du aber gerne öfter sagen würdest.",
    ROSE, ROSE_LIGHT)
box_h = 55 * mm
rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
yy = y - 16 * mm
for i in range(1, 4):
    number_badge(c, MARGIN + 12 * mm, yy - 3.5*mm, 5 * mm, i, ROSE)
    blank_line(c, MARGIN + 22 * mm, yy, W - 2 * MARGIN - 32 * mm)
    yy -= 15 * mm
note = ("Häng den Zettel irgendwo hin, wo du ihn zufällig siehst. Nicht um ihn "
        "auswendig zu lernen, sondern um ihn mit der Zeit vertraut werden zu lassen.")
wrapped(c, note, MARGIN, y - box_h - 10 * mm, W - 2 * MARGIN, 'Serif-It', 10.5, 14, color=ROSE_DARK)
footer(c, 5, "Übung 3", ROSE_DARK)
c.showPage()

# ============ Seite 6: Uebung 4 ============
y = section_header(c, 4, "Der Rückfall-Notfallplan",
    "Aus Kapitel 19: Ein Rückfall fühlt sich meistens schlimmer an, als er ist. "
    "Bereite dich jetzt schon vor, für den Tag, an dem das alte Muster wieder "
    "lauter wird als das neue.",
    SAGE, SAGE_LIGHT)
box_h = 76 * mm
rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
c.setFont('Sans-Bold', 11)
c.setFillColor(SAGE_DARK)
c.drawString(MARGIN + 8 * mm, y - 10 * mm, "Drei Dinge, die mir in guten Wochen helfen")
c.drawString(MARGIN + 8 * mm, y - 15 * mm, "und die ich auch in einer schlechten Woche noch schaffe:")
yy = y - 24 * mm
for i in range(1, 4):
    number_badge(c, MARGIN + 12 * mm, yy - 3.5*mm, 5 * mm, i, SAGE)
    blank_line(c, MARGIN + 22 * mm, yy, W - 2 * MARGIN - 32 * mm)
    yy -= 11 * mm
c.setFont('Sans-Bold', 11)
c.setFillColor(SAGE_DARK)
c.drawString(MARGIN + 8 * mm, yy - 3 * mm, "Eine Person, die ich anrufen kann, ohne mich zu rechtfertigen:")
blank_line(c, MARGIN + 8 * mm, yy - 13 * mm, W - 2 * MARGIN - 16 * mm)
note = "Häng diesen Zettel an den Kühlschrank oder speichere ihn als Foto auf deinem Handy, bevor du ihn brauchst."
wrapped(c, note, MARGIN, y - box_h - 10 * mm, W - 2 * MARGIN, 'Serif-It', 10.5, 14, color=SAGE_DARK)
footer(c, 6, "Übung 4", SAGE_DARK)
c.showPage()

# ============ Seite 7: Uebung 5 ============
y = section_header(c, 5, "Die Drei-Monats-Standortbestimmung",
    "Komm nach drei Monaten zu dieser Seite zurück, mit etwas Abstand zum Buch, "
    "und beantworte die folgenden Fragen ehrlich, nicht wie du gerne wärst.",
    ROSE, ROSE_LIGHT)
qs = [
    "Was hat sich in den letzten drei Monaten spürbar verändert, auch wenn es klein ist?",
    "Welche Übung aus dem Buch hast du am konsequentesten gemacht?",
    "Welches Kapitel würdest du heute nochmal lesen, wenn du nur eines auswählen könntest?",
]
yy = y
for q in qs:
    box_h = 26 * mm
    rounded(c, MARGIN, yy - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
    wrapped(c, q, MARGIN + 7 * mm, yy - 8 * mm, W - 2 * MARGIN - 14 * mm, 'Sans-Bold', 10.5, 13, color=ROSE_DARK)
    blank_line(c, MARGIN + 7 * mm, yy - box_h + 7 * mm, W - 2 * MARGIN - 14 * mm)
    yy -= box_h + 6 * mm
footer(c, 7, "Übung 5", ROSE_DARK)
c.showPage()

# ============ Seite 8: Uebung 6 ============
y = section_header(c, 6, "Ein Satz an dich, drei Monate später",
    "Schreib dir jetzt, direkt nach dem Buch, einen einzigen Satz auf, den du in "
    "drei Monaten wiederlesen sollst. Keinen Plan, keine Liste. Nur einen Satz, "
    "der dich heute trägt.",
    SAGE, SAGE_LIGHT)
box_h = 34 * mm
rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
blank_line(c, MARGIN + 10 * mm, y - 14 * mm, W - 2 * MARGIN - 20 * mm)
blank_line(c, MARGIN + 10 * mm, y - 24 * mm, W - 2 * MARGIN - 20 * mm)
y2 = y - box_h - 12 * mm
rounded(c, MARGIN, y2 - 26 * mm, W - 2 * MARGIN, 26 * mm, 6 * mm, SAGE_LIGHT)
note = ("Und wenn du magst, schreib mir, was sich bei dir seit dem Buch "
        "verändert hat. Ich lese jede Nachricht:")
wrapped(c, note, MARGIN + 8 * mm, y2 - 9 * mm, W - 2 * MARGIN - 16 * mm, 'Sans', 11, 15, color=PLUM)
c.setFont('Sans-Bold', 12)
c.setFillColor(SAGE_DARK)
c.drawCentredString(W / 2, y2 - 21 * mm, "info.safetothrive@gmail.com")
footer(c, 8, "Übung 6", SAGE_DARK)
c.showPage()

# ============ Seite 9: Zum Schluss / rechtliches ============
bg(c)
rounded(c, 0, H - 60 * mm, W, 60 * mm, 0, ROSE)
heart(c, W / 2, H - 26 * mm, 3.4, WHITE)
c.setFont('Serif-Bold', 20)
c.setFillColor(WHITE)
c.drawCentredString(W / 2, H - 40 * mm, "Zum Schluss")

y = H - 78 * mm
disclaimer = ("Dieses Bonus-PDF ersetzt keine medizinische, psychologische oder "
    "psychotherapeutische Beratung, Diagnose oder Behandlung. Es stellt keine "
    "Diagnose und gibt keine Heilversprechen. Du handelst auf eigene "
    "Verantwortung. Bei anhaltenden Beschwerden wende dich bitte an eine "
    "Ärztin, einen Arzt, eine Therapeutin oder eine andere Fachperson.")
y = wrapped(c, disclaimer, MARGIN, y, W - 2 * MARGIN, 'Sans', 10.5, 15)

y -= 10 * mm
rounded(c, MARGIN, y - 24 * mm, W - 2 * MARGIN, 24 * mm, 6 * mm, ROSE_LIGHT)
c.setFont('Sans-Bold', 11.5)
c.setFillColor(ROSE_DARK)
c.drawCentredString(W / 2, y - 10 * mm, "Bei einer akuten Krise")
c.setFont('Sans', 11)
c.setFillColor(PLUM)
c.drawCentredString(W / 2, y - 17 * mm, "Schweiz 143 · Deutschland 0800 111 0 111 · Österreich 142")
c.setFont('Sans', 9)
c.drawCentredString(W / 2, y - 21.5 * mm, "Kostenlos, anonym, Tag und Nacht.")

y -= 38 * mm
copyright_txt = ("© Petra Tanner, Safe to Thrive. Alle Rechte vorbehalten. Nur für den "
    "persönlichen Gebrauch, nicht zur Weitergabe oder Veröffentlichung bestimmt.")
y = wrapped(c, copyright_txt, MARGIN, y, W - 2 * MARGIN, 'Sans', 9.5, 13, color=HexColor('#7A6A66'), align='center')
c.setFont('Sans-Bold', 10.5)
c.setFillColor(SAGE_DARK)
c.drawCentredString(W / 2, y - 6 * mm, "info.safetothrive@gmail.com")
footer(c, 9, "Safe to Thrive")
c.showPage()

c.save()
print("Bonus-PDF erstellt:", OUT)
