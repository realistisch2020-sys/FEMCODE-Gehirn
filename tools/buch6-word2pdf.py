# -*- coding: utf-8 -*-
"""Baut das Taschenbuch-PDF aus der korrigierten Word-Datei.

Ab jetzt ist die Word-Datei die Quelle. Petra korrigiert dort,
dieses Skript setzt daraus das druckfertige PDF.
"""
import re, sys

DOCX = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/user/FEMCODE-Gehirn/outputs/buch6/buch6-MANUSKRIPT.docx"
OUT = "/home/user/FEMCODE-Gehirn/outputs/buch6/buch6-Taschenbuch.pdf"

# ─── Schriften einbetten ─────────────────────────────────────────────────────
# KDP lehnt PDFs ab, in denen Schriften nicht eingebettet sind. Die eingebauten
# Times-Schriften von ReportLab werden nur referenziert, nicht eingebettet.
# Liberation Serif ist masshaltig zu Times, der Satz bleibt also gleich.

from reportlab import rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

_FONTDIR = '/usr/share/fonts/truetype/liberation/'
for _name, _datei in (('Times-Roman',      'LiberationSerif-Regular.ttf'),
                      ('Times-Bold',       'LiberationSerif-Bold.ttf'),
                      ('Times-Italic',     'LiberationSerif-Italic.ttf'),
                      ('Times-BoldItalic', 'LiberationSerif-BoldItalic.ttf')):
    pdfmetrics.registerFont(TTFont(_name, _FONTDIR + _datei))
pdfmetrics.registerFontFamily('Times-Roman', normal='Times-Roman', bold='Times-Bold',
                              italic='Times-Italic', boldItalic='Times-BoldItalic')
for _i, _b, _n in ((0, 0, 'Times-Roman'), (1, 0, 'Times-Bold'),
                   (0, 1, 'Times-Italic'), (1, 1, 'Times-BoldItalic')):
    addMapping('Times-Roman', _i, _b, _n)

# Grundschrift der Leinwand, sonst landet Helvetica als tote Referenz auf jeder Seite
rl_config.canvas_basefontname = 'Times-Roman'

from docx import Document
from docx.shared import Pt
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, PageBreak, HRFlowable, KeepTogether,
                                NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import inch

# 5,5 x 8,5 Zoll = 139,7 x 215,9 mm. Standardformat bei KDP und das Format
# der ganzen Reihe. A5 steht bei KDP nicht zur Auswahl.
SEITE = (5.5 * inch, 8.5 * inch)
W, H = SEITE
LM = RM = 1.9 * cm
TM = BM = 2.2 * cm

# ─── Seitenvorlagen ──────────────────────────────────────────────────────────

def plain_page(canvas, doc):
    pass

def draw_heart(canvas, x, y, s, farbe):
    """Kleines Herz aus zwei Bezierkurven. x,y ist die untere Spitze."""
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
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawCentredString(W / 2, 0.9 * cm, str(doc.page))
    draw_heart(canvas, W - RM - 0.10 * cm, 0.87 * cm, 0.105 * cm,
               colors.HexColor('#9a8f8a'))
    canvas.restoreState()


class BookDoc(BaseDocTemplate):
    def __init__(self, filename):
        BaseDocTemplate.__init__(
            self, filename, pagesize=SEITE,
            leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
            title="Ich bin so muede. Und niemand fragt mich warum",
            author="Petra Tanner")
        self.addPageTemplates([
            PageTemplate(id='Plain',
                         frames=Frame(LM, BM, W - LM - RM, H - TM - BM),
                         onPage=plain_page),
            PageTemplate(id='Numbered',
                         frames=Frame(LM, BM + .5 * cm, W - LM - RM,
                                      H - TM - BM - .5 * cm),
                         onPage=numbered_page),
        ])

    def afterFlowable(self, fl):
        if not hasattr(fl, 'style'):
            return
        n, t = fl.style.name, fl.getPlainText()
        if t == 'Inhaltsverzeichnis':
            return
        if n in ('PartTitle', 'SectionTitle'):
            self.notify('TOCEntry', (0, t, self.page, None))
        elif n == 'ChapterTitle':
            self.notify('TOCEntry', (1, t, self.page, None))


# ─── Stile ───────────────────────────────────────────────────────────────────
S = getSampleStyleSheet()
def ps(name, **kw):
    return ParagraphStyle(name, parent=S['Normal'], **kw)

body     = ps('Body',  fontName='Times-Roman', fontSize=11.5, leading=19.5, alignment=TA_JUSTIFY, spaceAfter=5)
body_c   = ps('BodyC', fontName='Times-Roman', fontSize=11.5, leading=19.5, alignment=TA_CENTER,  spaceAfter=5)
ital     = ps('Ital',  fontName='Times-Italic',fontSize=11.5, leading=19.5, alignment=TA_LEFT,    spaceAfter=5)
tp_title = ps('TpTitle', fontName='Times-Roman', fontSize=20, leading=26, alignment=TA_CENTER, spaceAfter=4)
tp_sub   = ps('TpSub',   fontName='Times-Italic',fontSize=11, leading=17, alignment=TA_CENTER, spaceAfter=20)
tp_auth  = ps('TpAuth',  fontName='Times-Roman', fontSize=11, leading=16, alignment=TA_CENTER, spaceAfter=4)
part_t   = ps('PartTitle', fontName='Times-Bold',   fontSize=14, leading=20, alignment=TA_CENTER, spaceBefore=12, spaceAfter=4)
part_s   = ps('PartSub',   fontName='Times-Italic', fontSize=10, leading=14, alignment=TA_CENTER, spaceAfter=20)
part_ch  = ps('PartCh',    fontName='Times-Roman',  fontSize=11, leading=19, alignment=TA_CENTER, spaceAfter=3)
chap_t   = ps('ChapterTitle', fontName='Times-Bold', fontSize=14, leading=20, spaceBefore=6, spaceAfter=8, keepWithNext=1)
sect_t   = ps('SectionTitle', fontName='Times-Bold', fontSize=13, leading=18, spaceBefore=6, spaceAfter=6, keepWithNext=1)
tiktok_s = ps('TikTok', fontName='Times-BoldItalic', fontSize=11.5, leading=18,
              alignment=TA_CENTER, spaceBefore=8, spaceAfter=16,
              leftIndent=12, rightIndent=12,
              backColor=colors.HexColor('#f0f0f0'), borderPadding=(6, 10, 6, 10))
refl_s   = ps('Refl', fontName='Times-Italic', fontSize=10.5, leading=15.5,
              alignment=TA_LEFT, spaceBefore=8, spaceAfter=4, leftIndent=18, rightIndent=18)
imp_s    = ps('Imp',     fontName='Times-Roman', fontSize=8.5, leading=12.5, spaceAfter=2)
imp_bold = ps('ImpBold', fontName='Times-Bold',  fontSize=8.5, leading=12.5, spaceAfter=6)
toc_l0   = ps('TOC0', fontName='Times-Bold',  fontSize=10.5, leading=16, spaceAfter=2)
toc_l1   = ps('TOC1', fontName='Times-Roman', fontSize=9.3, leading=14.5, spaceAfter=1, leftIndent=12)

esc = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def richtext(p):
    """Word-Absatz nach ReportLab-Markup, mit Fett und Kursiv je Textlauf."""
    teile = []
    for r in p.runs:
        t = esc(r.text).replace('\n', '<br/>')
        if not t:
            continue
        if r.bold:
            t = '<b>' + t + '</b>'
        if r.italic:
            t = '<i>' + t + '</i>'
        teile.append(t)
    return ''.join(teile) or esc(p.text.strip())

# ─── Word einlesen ───────────────────────────────────────────────────────────
docx = Document(DOCX)
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def has_pagebreak(p):
    return any(br.get(NS + 'type') == 'page' for br in p._p.iter(NS + 'br'))

def is_shaded(p):
    pr = p._p.find(NS + 'pPr')
    if pr is None: return False
    shd = pr.find(NS + 'shd')
    return shd is not None and (shd.get(NS + 'fill') or '').upper() == 'F0F0F0'

def has_border(p):
    pr = p._p.find(NS + 'pPr')
    return pr is not None and pr.find(NS + 'pBdr') is not None

def fontsize(p):
    for r in p.runs:
        if r.font.size:
            return r.font.size.pt
    return None

TOC_ROW = re.compile(r'.+\t\d+\s*$')

story = [NextPageTemplate('Plain')]
seen_toc = False
after_part = False
numbered = False

for p in docx.paragraphs:
    raw = p.text
    text = raw.strip()
    style = p.style.name
    size = fontsize(p)

    if has_pagebreak(p):
        # Leerraum direkt vor einem Umbruch wegwerfen, sonst rutscht er auf die
        # neue Seite und erzeugt eine leere Seite
        while story and isinstance(story[-1], Spacer):
            story.pop()
        story.append(PageBreak())
        if not text:
            continue

    if not text:
        if has_border(p):
            story.append(HRFlowable(width='100%', thickness=0.5,
                                    color=colors.HexColor('#aaaaaa'),
                                    spaceBefore=4, spaceAfter=8))
        else:
            sa = p.paragraph_format.space_after
            story.append(Spacer(1, (sa.pt / 0.5 if sa else 7) / 28.35 * cm))
        continue

    # Von Word erzeugte Inhaltsverzeichnis-Zeilen ueberspringen
    if TOC_ROW.match(raw):
        if not seen_toc:
            seen_toc = True
            toc = TableOfContents()
            toc.levelStyles = [toc_l0, toc_l1]
            toc.dotsMinLevel = 0
            story.append(toc)
        continue

    t = esc(text).replace('\n', '<br/>')
    r0 = p.runs[0] if p.runs else None
    bold = bool(r0 and r0.bold)
    italic = bool(r0 and r0.italic)
    centered = p.alignment is not None and 'CENTER' in str(p.alignment)

    if style == 'Heading 1':
        if centered:
            story.append(Paragraph(t, part_t)); after_part = True
        else:
            if text == 'Einleitung' and not numbered:
                story.insert(len(story), NextPageTemplate('Numbered'))
                numbered = True
            story.append(Spacer(1, 1.9 * cm))
            story.append(Paragraph(t, sect_t)); after_part = False
        continue
    if style == 'Heading 2':
        story.append(Spacer(1, 1.9 * cm))
        story.append(Paragraph(t, chap_t)); after_part = False
        continue
    if is_shaded(p):
        story.append(KeepTogether([Spacer(1, .2 * cm),
                                   Paragraph(t, tiktok_s), Spacer(1, .2 * cm)]))
        continue
    if italic and p.paragraph_format.left_indent and not centered:
        block = [Paragraph(t, refl_s)]
        # vorangehende Leerraeume und die Zeile "Reflexion" mitnehmen
        while story and isinstance(story[-1], Spacer):
            story.pop()
        if story and isinstance(story[-1], Paragraph) \
           and story[-1].getPlainText().strip() == 'Reflexion':
            block.insert(0, story.pop())
        block.insert(0, Spacer(1, .45 * cm))
        story.append(KeepTogether(block))
        continue
    if size and size <= 9.5:
        story.append(Paragraph(richtext(p), imp_bold if bold else imp_s));  continue
    if size and size >= 20:
        story.append(Paragraph(t, tp_title));  continue
    if centered:
        if italic and size and size <= 12.5:
            story.append(Paragraph(t, part_s if after_part else tp_sub))
        elif after_part:
            story.append(Paragraph(t, part_ch))
        elif size and size <= 11.5 and not numbered:
            story.append(Paragraph(t, tp_auth))
        else:
            story.append(Paragraph(t, body_c))
        continue
    story.append(Paragraph(richtext(p), ital if italic else body))

# Fette Zwischentitel duerfen nie allein am Seitenfuss stehen
def titel_binden(st):
    raus, i = [], 0
    while i < len(st):
        f = st[i]
        istTitel = (isinstance(f, Paragraph) and f.style.name == 'Body'
                    and f.text.startswith('<b>') and f.text.rstrip().endswith('</b>'))
        if not istTitel:
            raus.append(f); i += 1; continue
        # Titel mit den naechsten zwei Inhaltszeilen zusammenbinden
        block, j, inhalt = [f], i + 1, 0
        while j < len(st) and inhalt < 2:
            g = st[j]
            if not isinstance(g, (Paragraph, Spacer)):
                break
            block.append(g)
            if isinstance(g, Paragraph):
                inhalt += 1
            j += 1
        raus.append(KeepTogether(block))
        i = j
    return raus


story = titel_binden(story)

# Zusammenhaengende kurze Zeilen nicht ueber den Seitenrand reissen
def bloecke_binden(st):
    raus, puffer = [], []
    def leeren():
        if len(puffer) > 1:
            raus.append(KeepTogether(list(puffer)))
        else:
            raus.extend(puffer)
        puffer.clear()
    for f in st:
        if isinstance(f, Paragraph) and f.style.name in ('Body', 'Ital') \
           and len(puffer) < 4:
            puffer.append(f)
        else:
            leeren()
            raus.append(f)
    leeren()
    return raus

story = bloecke_binden(story)

# Impressum am Schluss ohne Seitenzahl
for i in range(len(story) - 1, -1, -1):
    f = story[i]
    if isinstance(f, Paragraph) and f.style.name == 'ImpBold' \
       and '2026' in f.getPlainText():
        story.insert(i, NextPageTemplate('Plain'))
        break

doc = BookDoc(OUT)
doc.multiBuild(story)
print("PDF erstellt:", OUT)
