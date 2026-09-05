# -*- coding: utf-8 -*-
"""Freebie-PDF 'Sieben Saetze, die dich zurueck zu dir bringen'.
Hochformat A4, zehn Seiten, viel Weissraum, wenig Text pro Seite,
lieblich-warme Typografie (Creme/Rose/Gold, Herz-Trenner, sanfte
Rosé-Karten hinter den Saetzen) - passend zur Buchreihen-Bildsprache."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
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

OUT = "/home/user/FEMCODE-Gehirn/outputs/freebie-7-saetze/7-saetze-zurueck-zu-dir.pdf"
QR_PFAD = "/home/user/FEMCODE-Gehirn/outputs/freebie-7-saetze/autorenseite-qr.png"

W, H = A4
MARGIN = 30 * mm
CX = W / 2

CREME = HexColor('#FBF3EC')
ROSE_HELL = HexColor('#F3DCD3')
ROSE = HexColor('#C98B78')
ANTHRAZIT = HexColor('#4A3B34')
GOLD = HexColor('#C08A4E')
GRAU = HexColor('#9C8579')

c = canvas.Canvas(OUT, pagesize=A4)


GRAD_TOP = HexColor('#F6E1D7')
GRAD_BOTTOM = HexColor('#FCF5EF')


def _mix(c1, c2, t):
    return (c1[0] + (c2[0] - c1[0]) * t,
            c1[1] + (c2[1] - c1[1]) * t,
            c1[2] + (c2[2] - c1[2]) * t)


def bg():
    top = (GRAD_TOP.red, GRAD_TOP.green, GRAD_TOP.blue)
    bottom = (GRAD_BOTTOM.red, GRAD_BOTTOM.green, GRAD_BOTTOM.blue)
    bands = 140
    band_h = H / bands
    for i in range(bands):
        t = i / (bands - 1)
        r, g, b = _mix(top, bottom, t)
        c.setFillColorRGB(r, g, b)
        c.rect(0, H - (i + 1) * band_h, W, band_h + 0.6, fill=1, stroke=0)


def herz(x, y, s, color=ROSE):
    c.saveState()
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x - 1.45 * s, y + 1.05 * s, x - 0.80 * s, y + 2.15 * s, x, y + 1.35 * s)
    p.curveTo(x + 0.80 * s, y + 2.15 * s, x + 1.45 * s, y + 1.05 * s, x, y)
    p.close()
    c.setFillColor(color)
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()


def rule(y, width=26 * mm, color=GOLD, lw=0.9, mit_herz=True):
    if mit_herz:
        herz(CX, y - 1.1 * mm, 1.15 * mm)
        return
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(CX - width / 2, y, CX + width / 2, y)


def centered(text, y, font, size, color, leading=None):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawCentredString(CX, y, text)
    return y - (leading or size * 1.3)


def centered_block(lines, y, font, size, color, leading):
    for line in lines:
        y = centered(line, y, font, size, color, leading)
    return y


def wrapped_centered(text, y, font, size, color, leading, max_w=None):
    max_w = max_w or (W - 2 * MARGIN)
    lines = simpleSplit(text, font, size, max_w)
    return centered_block(lines, y, font, size, color, leading)


def rose_karte(text, y_top, font, size, color, leading, max_w, pad=9 * mm):
    """Zeichnet eine sanft gerundete Rosé-Karte hinter dem Satz und
    gibt die y-Position unterhalb der Karte zurueck."""
    lines = simpleSplit(text, font, size, max_w)
    block_h = len(lines) * leading
    box_w = max_w + 2 * pad
    box_h = block_h + 2 * pad
    box_y = y_top - box_h
    c.saveState()
    c.setFillColor(ROSE_HELL)
    c.roundRect(CX - box_w / 2, box_y, box_w, box_h, 6 * mm, fill=1, stroke=0)
    c.restoreState()
    text_y = y_top - pad - size * 0.92
    for line in lines:
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawCentredString(CX, text_y, line)
        text_y -= leading
    return box_y - 0


def eyebrow(text, y, size=12):
    c.setFont('Sans-Bold', size)
    c.setFillColor(ROSE)
    letters = list(text.upper())
    spacing = 3.0
    total_w = sum(pdfmetrics.stringWidth(ch, 'Sans-Bold', size) + spacing for ch in letters) - spacing
    x = CX - total_w / 2
    for ch in letters:
        c.drawString(x, y, ch)
        x += pdfmetrics.stringWidth(ch, 'Sans-Bold', size) + spacing
    return y


def new_page():
    c.showPage()
    bg()


# ─── Seite 1: Titelseite ────────────────────────────────────────────────
bg()
y = H - 100 * mm
y = wrapped_centered('7 Sätze, die dich zurück zu dir bringen',
                      y, 'Serif-Bold', 32, ANTHRAZIT, 40, max_w=125 * mm)
y -= 10 * mm
rule(y)
y -= 15 * mm
y = wrapped_centered('Für die Momente, in denen du für alle da bist – '
                      'nur nicht mehr für dich',
                      y, 'Serif-It', 16, GRAU, 22, max_w=120 * mm)
y = 40 * mm
centered('PETRA TANNER', y, 'Sans-Bold', 13, ANTHRAZIT, 0)

# ─── Seite 2: Einleitung ────────────────────────────────────────────────
new_page()
y = H - 105 * mm
y = wrapped_centered('Du musst nicht erst zusammenbrechen, um zu erkennen, '
                      'dass es zu viel ist.',
                      y, 'Serif-Bold', 19, ANTHRAZIT, 26, max_w=120 * mm)
y -= 13 * mm
y = wrapped_centered('Manchmal reicht ein Satz, der dich mitten im '
                      'Funktionieren stoppt. Ein Satz, der dich daran '
                      'erinnert, dass auch du in deinem eigenen Leben '
                      'vorkommen darfst.',
                      y, 'Serif', 14.5, ANTHRAZIT, 21, max_w=118 * mm)
y -= 11 * mm
y = wrapped_centered('Lies diese Seiten langsam. Bleib bei dem Satz hängen, '
                      'der etwas in dir auslöst. Genau dort beginnt deine '
                      'Veränderung.',
                      y, 'Serif', 14.5, ANTHRAZIT, 21, max_w=118 * mm)

# ─── Saetze ──────────────────────────────────────────────────────────────
SAETZE = [
    ("SATZ 1",
     "Ich darf mich wichtig nehmen, ohne jemandem etwas wegzunehmen",
     ["Du hast gelernt, zuerst zu schauen, was andere brauchen. Deshalb "
      "fühlt es sich ungewohnt an, dich selbst einzubeziehen.",
      "Doch deine Bedürfnisse machen dich nicht egoistisch. Sie zeigen "
      "dir, wo du dich selbst zu lange übergangen hast."],
     "Was brauche ich gerade wirklich?"),
    ("SATZ 2",
     "Ich bin nicht für die Gefühle anderer verantwortlich",
     ["Du darfst mitfühlen, ohne alles zu übernehmen.",
      "Die Enttäuschung, Wut oder Unruhe eines anderen gehört nicht "
      "automatisch dir. Du musst sie nicht beseitigen, damit wieder "
      "Frieden herrscht."],
     "Heute lasse ich bei anderen, was zu ihnen gehört."),
    ("SATZ 3",
     "Mein Nein ist kein Angriff",
     ["Ein Nein bedeutet nicht, dass du lieblos bist. Es bedeutet, dass "
      "du deine Grenze ernst nimmst.",
      "Menschen, die davon profitiert haben, dass du keine Grenzen "
      "hattest, werden sich daran gewöhnen müssen. Deine Aufgabe ist "
      "es, dir treu zu bleiben."],
     "Heute sage ich einmal ehrlich Nein."),
    ("SATZ 4",
     "Ich muss nicht erst völlig erschöpft sein, um eine Pause zu verdienen",
     ["Du brauchst keinen Zusammenbruch als Erlaubnis, stehen zu bleiben.",
      "Müdigkeit ist kein Zeichen dafür, dass du dich noch mehr "
      "anstrengen musst. Sie zeigt dir, dass du zu lange über deine "
      "eigenen Signale hinweggegangen bist."],
     "Heute gönne ich mir Ruhe, bevor mein Körper sie erzwingen muss."),
    ("SATZ 5",
     "Ein schlechtes Gewissen bedeutet nicht automatisch, dass ich "
     "etwas falsch gemacht habe",
     ["Manchmal meldet sich dein schlechtes Gewissen nur deshalb, weil "
      "du dich anders verhältst als früher.",
      "Du setzt eine Grenze. Du sagst Nein. Du entscheidest dich für "
      "dich. Das kann sich zunächst falsch anfühlen und trotzdem "
      "richtig sein."],
     "Habe ich wirklich jemanden verletzt – oder habe ich nur "
     "aufgehört, mich selbst zu übergehen?"),
    ("SATZ 6",
     "Ich darf gehen, wenn mich etwas dauerhaft erschöpft",
     ["Du musst nicht bleiben, bis gar nichts mehr von dir übrig ist.",
      "Eine Beziehung darf schwierig sein. Sie darf dich aber nicht "
      "ständig deine Kraft, deinen Selbstwert und deinen inneren "
      "Frieden kosten."],
     "Heute schaue ich auf das, was tatsächlich passiert – nicht auf "
     "das, was ich mir weiterhin erhoffe."),
    ("SATZ 7",
     "Ich komme zurück zu mir – eine Entscheidung nach der anderen",
     ["Du musst heute nicht dein ganzes Leben verändern.",
      "Aber du kannst bei der nächsten Entscheidung aufhören, dich "
      "wieder zu verlassen. Du kannst dich fragen, was für dich "
      "stimmt, und danach handeln."],
     "Heute entscheide ich mich an einer Stelle für mich."),
]

for label, satz, absaetze, tages_impuls in SAETZE:
    new_page()
    y = H - 52 * mm
    eyebrow(label, y)
    y -= 18 * mm
    y = rose_karte(satz, y, 'Serif-Bold', 21, ANTHRAZIT, 29, max_w=108 * mm,
                   pad=10 * mm)
    y -= 17 * mm
    for absatz in absaetze:
        y = wrapped_centered(absatz, y, 'Serif', 14, ANTHRAZIT, 20,
                              max_w=118 * mm)
        y -= 7 * mm
    y -= 6 * mm
    herz(CX, y - 1.3 * mm, 1.3 * mm)
    y -= 12 * mm
    wrapped_centered(tages_impuls, y, 'Serif-It', 14, ROSE, 19.5,
                      max_w=112 * mm)

# ─── Seite 10: Abschluss ────────────────────────────────────────────────
new_page()
y = H - 42 * mm
y = wrapped_centered('Welcher Satz ist bei dir hängen geblieben?',
                      y, 'Serif-Bold', 20, ANTHRAZIT, 26, max_w=120 * mm)
y -= 9 * mm
y = wrapped_centered('Meist ist es genau der Satz, bei dem du kurz still '
                      'wirst. Weil du längst spürst, dass sich dort etwas '
                      'verändern darf.',
                      y, 'Serif', 13.5, ANTHRAZIT, 19, max_w=112 * mm)
y -= 9 * mm
rule(y, width=18 * mm)
y -= 10 * mm

EMPFEHLUNGEN = [
    ("Wenn dich Beziehungen erschöpfen:", "Wenn Beziehungen erschöpfen"),
    ("Wenn Schuldgefühle dich festhalten:", "Das schlechte Gewissen"),
    ("Wenn du nur noch funktionierst:", "Ich bin so müde und niemand fragt mich warum"),
    ("Wenn du ständig zuletzt kommst:", "Ich stand nie auf meiner eigenen Liste"),
    ("Wenn du die Gefühle und Reaktionen anderer trägst:", "Deine Reaktion gehört dir. Nicht mir."),
]
for bedingung, titel in EMPFEHLUNGEN:
    y = wrapped_centered(bedingung, y, 'Sans', 11, GRAU, 15, max_w=120 * mm)
    y = wrapped_centered('„%s“' % titel, y, 'Serif-Bold', 14, ANTHRAZIT,
                          19, max_w=120 * mm)
    y -= 4 * mm

y -= 5 * mm
rule(y, width=18 * mm)
y -= 10 * mm
y = wrapped_centered('Alle Bücher findest du hier:', y, 'Serif', 13,
                      ANTHRAZIT, 18, max_w=115 * mm)
y = wrapped_centered('amazon.de/stores/Petra-Tanner/author/B0H9FG6CJ7',
                      y, 'Sans-Bold', 12, GOLD, 16, max_w=118 * mm)
y -= 7 * mm
QR_SIZE = 26 * mm
c.drawImage(QR_PFAD, CX - QR_SIZE / 2, y - QR_SIZE, QR_SIZE, QR_SIZE,
            mask='auto')
y -= QR_SIZE + 9 * mm
y = wrapped_centered('Folge mir auf Amazon', y, 'Serif-Bold', 15,
                      ANTHRAZIT, 20, max_w=115 * mm)
y = wrapped_centered('Öffne meine Autorenseite und klicke auf „Folgen“. '
                      'So kann Amazon dich informieren, sobald ein neues '
                      'Buch von mir erscheint.',
                      y, 'Serif', 12.5, GRAU, 17.5, max_w=108 * mm)
y -= 10 * mm
centered('Herzlichst', y, 'Serif-It', 14, ANTHRAZIT, 19)
centered('Petra Tanner', y - 19, 'Serif-Bold', 15, ANTHRAZIT, 0)

c.save()
print('PDF erstellt:', OUT)

import fitz
d = fitz.open(OUT)
print('Seiten:', d.page_count)
