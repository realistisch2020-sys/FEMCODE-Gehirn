# -*- coding: utf-8 -*-
"""Baut ein Taschenbuch-PDF direkt aus einer Word-Datei, ohne LibreOffice.

Fuer Manuskripte, die (anders als Buch 6) keine Word-Formatvorlagen wie
"Heading 1/2" verwenden, sondern nur direkte Formatierung (Schriftgroesse,
Ausrichtung) plus "Seitenumbruch davor" auf den Kapitel-Absaetzen. Die
Zuordnung Titel/Ueberschrift/Fliesstext laeuft deshalb ueber die
Schriftgroesse, nicht ueber Formatvorlagen.

    python3 tools/manuskript-word2pdf.py <manuskript.docx> <ausgabe.pdf> "<Titel>" "<Autor>"
"""
import sys

DOCX = sys.argv[1]
OUT = sys.argv[2]
TITEL = sys.argv[3] if len(sys.argv) > 3 else ''
AUTOR = sys.argv[4] if len(sys.argv) > 4 else 'Petra Tanner'

# ─── Schriften einbetten ─────────────────────────────────────────────────────
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
                                Table, TableStyle, Image)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import io


def eingebettetes_bild(p):
    """Findet ein inline eingefuegtes Bild (z.B. QR-Code) in einem Absatz und
    gibt es als zentriertes reportlab-Image zurueck, sonst None."""
    ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
          'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
    for blip in p._p.findall('.//a:blip', ns):
        rId = blip.get('{%s}embed' % ns['r'])
        if not rId:
            continue
        image_part = p.part.related_parts[rId]
        img = Image(io.BytesIO(image_part.blob))
        max_w = 4.2 * cm
        scale = max_w / img.imageWidth
        img.drawWidth = max_w
        img.drawHeight = img.imageHeight * scale
        img.hAlign = 'CENTER'
        return img
    return None
from reportlab.lib.pagesizes import inch

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
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawCentredString(W / 2, 1.4 * cm, str(doc.page))
    draw_heart(canvas, W - RM - 0.10 * cm, 1.37 * cm, 0.105 * cm,
               colors.HexColor('#9a8f8a'))
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


title_s = ps('Title', fontName='Times-Roman', fontSize=20, leading=26,
             alignment=TA_CENTER, spaceAfter=4)
sub_s = ps('Sub', fontName='Times-Italic', fontSize=12, leading=17,
           alignment=TA_CENTER, spaceAfter=10)
heading_s = ps('Heading', fontName='Times-Bold', fontSize=13.5, leading=19,
               alignment=TA_LEFT, spaceBefore=0, spaceAfter=8, keepWithNext=1)
body_s = ps('Body', fontName='Times-Roman', fontSize=11.5, leading=19.5,
            alignment=TA_JUSTIFY, spaceAfter=5)
body_c_s = ps('BodyC', fontName='Times-Roman', fontSize=11.5, leading=19.5,
              alignment=TA_CENTER, spaceAfter=5)
small_s = ps('Small', fontName='Times-Roman', fontSize=9, leading=13, spaceAfter=2)
toc_s = ps('Toc', fontName='Times-Roman', fontSize=10, leading=13.5, spaceAfter=1)
mini_head_s = ps('MiniHead', fontName='Times-Bold', fontSize=11.5, leading=19.5,
                  alignment=TA_JUSTIFY, spaceBefore=10, spaceAfter=5, keepWithNext=1)
tiktok_s = ps('TikTok', fontName='Times-Italic', fontSize=11, leading=15.5,
              alignment=TA_CENTER)


import re as _re
# Kein '^'-Anker: der Text kommt aus richtext() und kann mit einem
# HTML-Tag beginnen (z.B. '<i>'), wenn der Absatz kursiv formatiert ist.
# Das Praefix steht dann nicht am Stringanfang, sondern direkt danach.
_TIKTOK_PREFIX = _re.compile(r'TikTok\s*(?:&#183;|·)?\s*', _re.IGNORECASE)


def tiktok_box(text):
    """Kurze Merksaetze als grau hinterlegter Kasten, wie bei Buch 6.
    Das interne 'TikTok'-Praefix (nur zur Erkennung im Quelltext) wird
    hier entfernt, es darf nicht im gedruckten Buch erscheinen."""
    text = _TIKTOK_PREFIX.sub('', text, count=1)
    p = Paragraph(text, tiktok_s)
    t = Table([[p]], colWidths=[W - LM - RM])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#efece6')),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t

def esc(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Liberation Serif hat kein Kaestchen-Glyph (U+2610); als Checkbox-Ersatz
    return s.replace('☐', '[ ]')


def richtext(p):
    teile = []
    for r in p.runs:
        t = esc(r.text).replace('\n', '<br/>')
        if not t:
            continue
        if r.bold:
            t = '<b>%s</b>' % t
        if r.italic:
            t = '<i>%s</i>' % t
        teile.append(t)
    return ''.join(teile) if teile else esc(p.text)


def mit_vorlauf(par, extra_pt):
    if extra_pt and hasattr(par, 'style'):
        par.style = ParagraphStyle('vorlauf_%d' % id(par), parent=par.style,
                                    spaceBefore=(par.style.spaceBefore or 0) + extra_pt)
    # Objekte ohne .style (z.B. eine Table/TikTok-Kasten) haben schon eigenes
    # Padding - zusaetzlicher Vorlauf wird hier bewusst ignoriert, statt das
    # Layout durch ein KeepTogether auf eine neue Seite zu zwingen.
    return par


NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def hat_inline_umbruch(p):
    for br in p._p.iter(NS + 'br'):
        if br.get(NS + 'type') == 'page':
            return True
    return False


def baue():
    docx = Document(DOCX)
    story = [NextPageTemplate('Plain')]
    pending_space = 0.0
    numbered = False
    in_toc = False
    pending_mini = None
    letzter_war_merge = False

    def anhaengen(flowable, gruppieren, quelltext='', max_merge_len=70):
        # gruppieren=True: Absatz darf nie mitten im Satz auf die naechste
        # Seite gerissen werden. Eine offene fette Zwischenzeile (z.B.
        # "Schritt 1: ...") wird mit diesem Absatz zusammen gehalten, damit
        # sie nie allein als letzte Zeile einer Seite steht.
        nonlocal pending_mini, letzter_war_merge
        if pending_mini is not None:
            story.append(KeepTogether([pending_mini, flowable]))
            pending_mini = None
            letzter_war_merge = False
        elif gruppieren:
            # Kurze Pointe-Saetze (ein Satz, keine Ueberschrift) sollen nie
            # allein am Anfang einer neuen Seite landen, sondern beim
            # vorherigen Absatz bleiben, zu dem sie inhaltlich gehoeren.
            # Hoechstens ein Absatz wird so angehaengt, sonst koennten sich
            # viele kurze Saetze hintereinander (z.B. eine Aufzaehlung) zu
            # einem einzigen, zu grossen Block verketten.
            if (len(quelltext) <= max_merge_len and not letzter_war_merge
                    and story and isinstance(story[-1], KeepTogether)):
                vorheriges = story.pop()
                story.append(KeepTogether(list(vorheriges._content) + [flowable]))
                letzter_war_merge = True
            else:
                story.append(KeepTogether([flowable]))
                letzter_war_merge = False
        else:
            story.append(flowable)

    def mini_offen(flowable):
        nonlocal pending_mini
        if pending_mini is not None:
            # zwei fette Kurzzeilen direkt hintereinander: die erste einzeln
            # ausgeben, damit nichts verloren geht.
            story.append(pending_mini)
        pending_mini = flowable

    for p in docx.paragraphs:
        text = p.text.strip()
        if text.startswith('EBOOKONLY'):
            # Absatz ist nur fuer das eBook gedacht (z.B. Text-Fallback-Link
            # fuer den QR-Code), im Taschenbuch komplett weglassen.
            continue
        bild = eingebettetes_bild(p)
        if bild is not None:
            absatz = mit_vorlauf(bild, pending_space)
            pending_space = 0.0
            anhaengen(absatz, True)
            continue
        centered = p.alignment is not None and 'CENTER' in str(p.alignment)
        size = None
        for r in p.runs:
            if r.text.strip():
                size = r.font.size.pt if r.font.size else None
                break
        textruns = [r for r in p.runs if r.text.strip()]
        ganz_fett = bool(textruns) and all(r.bold for r in textruns)
        # Manche Absaetze tragen fehlerhaft verzehnfachte Schriftgroessen
        # (z.B. 220pt statt 22pt) aus einer frueheren Bearbeitung. Fuer die
        # Stil-Erkennung auf plausible Buchgroessen zurueckrechnen.
        if size and size > 40:
            size = size / 10.0

        umbruch = p.paragraph_format.page_break_before or hat_inline_umbruch(p)
        if umbruch:
            while story and isinstance(story[-1], Spacer):
                story.pop()
            if pending_mini is not None:
                story.append(pending_mini)
                pending_mini = None
            story.append(PageBreak())
            if not numbered:
                story.append(NextPageTemplate('Numbered'))
                numbered = True
            pending_space = 0.0
            in_toc = False

        if not text:
            sa = p.paragraph_format.space_after
            pending_space += (sa.pt / 0.5 if sa else 7)
            continue

        if text == 'Inhalt' and size and 15 <= size < 20:
            in_toc = True
            absatz = Paragraph(esc(text), heading_s)
            pending_space = 0.0
            anhaengen(absatz, False)
            continue

        if in_toc:
            absatz = mit_vorlauf(Paragraph(esc(text), toc_s), pending_space)
            pending_space = 0.0
            anhaengen(absatz, False)
            continue

        if text.startswith('TikTok'):
            absatz = mit_vorlauf(tiktok_box(richtext(p)), pending_space)
            pending_space = 0.0
            # Fuer die Merge-Entscheidung (Absatz bleibt beim vorherigen
            # Block statt allein auf einer neuen Seite zu landen) zaehlt nur
            # das eigentliche Zitat, nicht das interne "TikTok "-Praefix.
            # Grosszuegigere Laengengrenze als bei normalen Pointe-Saetzen,
            # damit ein Zitat nie allein auf einer fast leeren Seite landet.
            anhaengen(absatz, True, _TIKTOK_PREFIX.sub('', text, count=1),
                      max_merge_len=140)
        elif size and size >= 20:
            absatz = Paragraph(esc(text), title_s)
            anhaengen(absatz, False)
        elif size and 15 <= size < 20:
            absatz = Paragraph(esc(text), heading_s)
            pending_space = 0.0
            anhaengen(absatz, False)
        elif centered and size and 12 <= size < 15:
            absatz = Paragraph(esc(text), sub_s)
            anhaengen(absatz, False)
        elif size and size <= 10:
            absatz = mit_vorlauf(Paragraph(richtext(p), small_s), pending_space)
            pending_space = 0.0
            # Absatz bleibt als Ganzes auf einer Seite, wird nie mitten im
            # Satz auf die naechste Seite gerissen.
            anhaengen(absatz, True, text)
        elif ganz_fett and not centered:
            # Ganz fett gesetzte Kurzzeile mitten im Fliesstext (z.B. "Schritt
            # 1: ..."). Das ist eine Zwischenueberschrift ohne eigene
            # Schriftgroesse. Darf nie als letzte Zeile einer Seite allein
            # stehen bleiben, deshalb wird sie mit dem naechsten Absatz
            # zusammen gehalten statt sofort ausgegeben.
            absatz = mit_vorlauf(Paragraph(richtext(p), mini_head_s), pending_space)
            pending_space = 0.0
            mini_offen(absatz)
        else:
            stil = body_c_s if centered else body_s
            absatz = mit_vorlauf(Paragraph(richtext(p), stil), pending_space)
            pending_space = 0.0
            anhaengen(absatz, True)

    if pending_mini is not None:
        story.append(pending_mini)

    doc = BookDoc(OUT)
    doc.build(story)
    print('PDF erstellt:', OUT)
    print('  Seiten:', end=' ')


if __name__ == '__main__':
    baue()
