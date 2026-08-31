# -*- coding: utf-8 -*-
"""Baut ein Journal-Taschenbuch-PDF aus einer Word-Datei: Kapitel-
Ueberschriften, Zwischenueberschriften in Akzentfarbe, Schreiblinien nach
Fragen/Uebungen (Marker "SCHREIBLINIEN·N" im Docx), Herzen beidseitig im
Fuss.

    python3 tools/journal-word2pdf.py <manuskript.docx> <ausgabe.pdf> "<Titel>" "<Autor>" [#HEXFARBE]
"""
import sys, re

DOCX = sys.argv[1]
OUT = sys.argv[2]
TITEL = sys.argv[3] if len(sys.argv) > 3 else ''
AUTOR = sys.argv[4] if len(sys.argv) > 4 else 'Petra Tanner'
AKZENT_HEX = sys.argv[5] if len(sys.argv) > 5 else '#C99A43'

from reportlab import rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

_FONTDIR = '/usr/share/fonts/truetype/liberation/'
for _name, _datei in (('Times-Roman', 'LiberationSerif-Regular.ttf'),
                      ('Times-Bold', 'LiberationSerif-Bold.ttf'),
                      ('Times-Italic', 'LiberationSerif-Italic.ttf'),
                      ('Times-BoldItalic', 'LiberationSerif-BoldItalic.ttf')):
    pdfmetrics.registerFont(TTFont(_name, _FONTDIR + _datei))
pdfmetrics.registerFontFamily('Times-Roman', normal='Times-Roman', bold='Times-Bold',
                              italic='Times-Italic', boldItalic='Times-BoldItalic')
for _i, _b, _n in ((0, 0, 'Times-Roman'), (1, 0, 'Times-Bold'),
                   (0, 1, 'Times-Italic'), (1, 1, 'Times-BoldItalic')):
    addMapping('Times-Roman', _i, _b, _n)
rl_config.canvas_basefontname = 'Times-Roman'

from docx import Document
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, PageBreak, KeepTogether, NextPageTemplate,
                                Flowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

AKZENT = colors.HexColor(AKZENT_HEX)
GRAU_LINIE = colors.HexColor('#c9c2b8')
FUSS_GRAU = colors.HexColor('#555555')

SEITE = (5.5 * inch, 8.5 * inch)
W, H = SEITE
LM = RM = 1.9 * cm
TM = BM = 2.2 * cm


def plain_page(canvas, doc):
    pass


def draw_heart(canvas, x, y, s, farbe):
    p = canvas.beginPath()
    p.moveTo(x, y)
    p.curveTo(x - 1.45 * s, y + 1.05 * s, x - 0.80 * s, y + 2.15 * s, x, y + 1.35 * s)
    p.curveTo(x + 0.80 * s, y + 2.15 * s, x + 1.45 * s, y + 1.05 * s, x, y)
    p.close()
    canvas.setFillColor(farbe)
    canvas.setStrokeColor(farbe)
    canvas.drawPath(p, fill=1, stroke=0)


def numbered_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.setFillColor(FUSS_GRAU)
    canvas.drawCentredString(W / 2, 1.4 * cm, str(doc.page))
    draw_heart(canvas, LM + 0.10 * cm, 1.37 * cm, 0.105 * cm, AKZENT)
    draw_heart(canvas, W - RM - 0.10 * cm, 1.37 * cm, 0.105 * cm, AKZENT)
    canvas.restoreState()


class BookDoc(BaseDocTemplate):
    def __init__(self, filename):
        BaseDocTemplate.__init__(
            self, filename, pagesize=SEITE,
            leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
            title=TITEL, author=AUTOR)
        self.addPageTemplates([
            PageTemplate(id='Plain', frames=Frame(LM, BM, W - LM - RM, H - TM - BM),
                         onPage=plain_page),
            PageTemplate(id='Numbered',
                         frames=Frame(LM, BM + .5 * cm, W - LM - RM,
                                      H - TM - BM - .5 * cm),
                         onPage=numbered_page),
        ])


def ps(name, **kw):
    return ParagraphStyle(name, **kw)


title_s = ps('Title', fontName='Times-Bold', fontSize=19, leading=25,
             alignment=TA_CENTER, spaceAfter=4)
sub_s = ps('Sub', fontName='Times-Italic', fontSize=13, leading=18,
           alignment=TA_CENTER, spaceAfter=10)
author_s = ps('Author', fontName='Times-Bold', fontSize=13, leading=17,
              alignment=TA_CENTER, spaceAfter=2)
publisher_s = ps('Publisher', fontName='Times-Roman', fontSize=11, leading=15,
                  alignment=TA_CENTER, spaceAfter=6)
heading_s = ps('Heading', fontName='Times-Bold', fontSize=14.5, leading=19,
               alignment=TA_LEFT, spaceBefore=0, spaceAfter=10, keepWithNext=1,
               textColor=colors.HexColor('#1a1a1a'))
body_s = ps('Body', fontName='Times-Roman', fontSize=11.3, leading=17.5,
            alignment=TA_JUSTIFY, spaceAfter=7)
mini_s = ps('Mini', fontName='Times-Bold', fontSize=12.5, leading=17,
            alignment=TA_LEFT, spaceBefore=8, spaceAfter=6, keepWithNext=1,
            textColor=AKZENT)
frage_s = ps('Frage', fontName='Times-Bold', fontSize=11.3, leading=15.5,
             alignment=TA_LEFT, spaceBefore=4, spaceAfter=6, keepWithNext=1)

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
_SCHREIB = re.compile(r'^SCHREIBLINIEN·(\d+)$')


class Schreiblinien(Flowable):
    """Flowable: N duenne horizontale Linien mit Abstand, zum Reinschreiben."""
    def __init__(self, anzahl):
        Flowable.__init__(self)
        self.anzahl = anzahl
        self.abstand = 1.05 * cm
        self.width = W - LM - RM
        self.height = anzahl * self.abstand

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setStrokeColor(GRAU_LINIE)
        canvas.setLineWidth(0.6)
        for i in range(self.anzahl):
            ly = self.height - (i + 1) * self.abstand + 0.3 * cm
            canvas.line(0, ly, self.width, ly)
        canvas.restoreState()


def hat_inline_umbruch(p):
    for br in p._p.iter(NS + 'br'):
        if br.get(NS + 'type') == 'page':
            return True
    return False


def baue():
    docx = Document(DOCX)
    story = [NextPageTemplate('Plain')]
    numbered = False

    for p in docx.paragraphs:
        text = p.text.strip()
        umbruch = p.paragraph_format.page_break_before or hat_inline_umbruch(p)

        m = _SCHREIB.match(text)
        if m:
            story.append(Schreiblinien(int(m.group(1))))
            continue

        if umbruch:
            while story and isinstance(story[-1], Spacer):
                story.pop()
            story.append(PageBreak())
            if not numbered:
                story.append(NextPageTemplate('Numbered'))
                numbered = True

        if not text:
            continue

        size = None
        for r in p.runs:
            if r.text.strip():
                size = r.font.size.pt if r.font.size else None
                break
        textruns = [r for r in p.runs if r.text.strip()]
        ganz_fett = bool(textruns) and all(r.bold for r in textruns)
        centered = p.alignment is not None and 'CENTER' in str(p.alignment)

        if size and size >= 18:
            story.append(Paragraph(text, title_s))
        elif size and 14 <= size < 18:
            story.append(Paragraph(text, heading_s))
        elif centered and ganz_fett:
            story.append(Paragraph(text, author_s))
        elif centered and size and size >= 13:
            story.append(Paragraph(text, sub_s))
        elif centered:
            story.append(Paragraph(text, publisher_s))
        elif ganz_fett and not centered and text in ('Zum Reflektieren', 'Kleine Übung'):
            story.append(Paragraph(text, mini_s))
        elif text.endswith('?') and not centered:
            story.append(Paragraph(text, frage_s))
        else:
            story.append(Paragraph(text, body_s))

    doc = BookDoc(OUT)
    doc.build(story)
    print('PDF erstellt:', OUT)


if __name__ == '__main__':
    baue()
