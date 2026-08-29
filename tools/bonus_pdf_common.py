# -*- coding: utf-8 -*-
"""Gemeinsames Layout-Modul fuer die farbigen Bonus-PDFs (Freebies) aller
Buecher. Jedes Buch ruft render(config) mit seiner eigenen Cover-Farbpalette
und seinen eigenen sechs Uebungen auf. Siehe tools/buch*-bonus-pdf.py fuer
Beispiel-Konfigurationen.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

FD = '/usr/share/fonts/truetype/liberation/'
for _name, _file in [
    ('Serif', 'LiberationSerif-Regular.ttf'),
    ('Serif-Bold', 'LiberationSerif-Bold.ttf'),
    ('Serif-It', 'LiberationSerif-Italic.ttf'),
    ('Sans', 'LiberationSans-Regular.ttf'),
    ('Sans-Bold', 'LiberationSans-Bold.ttf'),
]:
    try:
        pdfmetrics.registerFont(TTFont(_name, FD + _file))
    except Exception:
        pass

W, H = A4
MARGIN = 22 * mm


def _hex(c):
    return c if isinstance(c, type(HexColor('#000000'))) else HexColor(c)


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


def bg(c, color):
    c.setFillColor(color)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def wrapped(c, text, x, y, width, font, size, leading, color, align='left'):
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


def blank_line(c, x, y, w, color):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(1.1)
    c.setDash(1, 2)
    c.line(x, y, x + w, y)
    c.restoreState()


def number_badge(c, x, y, r, num, color, white):
    c.saveState()
    c.setFillColor(color)
    c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Serif-Bold', r * 1.15)
    c.drawCentredString(x, y - r * 0.38, str(num))
    c.restoreState()


def number_badge_soft(c, x, y, r, num, color, tint):
    c.saveState()
    c.setFillColor(tint)
    c.setStrokeColor(color)
    c.setLineWidth(1)
    c.circle(x, y, r, fill=1, stroke=1)
    c.setFillColor(color)
    c.setFont('Serif-Bold', r * 1.25)
    c.drawCentredString(x, y - r * 0.36, str(num))
    c.restoreState()


def render(cfg):
    """cfg: dict, siehe die drei buchX-bonus-pdf.py Skripte fuer Beispiele."""
    P = cfg['palette']
    CREAM = P['CREAM']
    COVER_BG = P['COVER_BG']
    ACCENT = P['ACCENT']
    ACCENT_DARK = P['ACCENT_DARK']
    ACCENT_LIGHT = P['ACCENT_LIGHT']
    ACCENT2 = P['ACCENT2']
    ACCENT2_DARK = P['ACCENT2_DARK']
    ACCENT2_LIGHT = P['ACCENT2_LIGHT']
    PLUM = P['PLUM']
    WHITE = P['WHITE']
    LINE = P['LINE']
    COVER_TEXT = P['COVER_TEXT']

    OUT = cfg['out']
    c = canvas.Canvas(OUT, pagesize=A4)

    def footer(page_no, label, color=ACCENT_DARK, heart_color=None):
        c.saveState()
        c.setFont('Sans', 8.5)
        c.setFillColor(color)
        c.drawString(MARGIN, 14 * mm, label)
        c.drawRightString(W - MARGIN, 14 * mm, str(page_no))
        heart(c, W / 2, 12.7 * mm, 1.6, heart_color or ACCENT2)
        c.restoreState()

    def section_header(num, title_text, note, color, tint):
        bg(c, CREAM)
        rounded(c, MARGIN, H - 46 * mm, W - 2 * MARGIN, 28 * mm, 6 * mm, tint)
        number_badge(c, MARGIN + 18 * mm, H - 32 * mm, 9 * mm, num, color, WHITE)
        c.setFont('Serif-Bold', 17)
        c.setFillColor(PLUM)
        c.drawString(MARGIN + 34 * mm, H - 29 * mm, title_text)
        y0 = H - 60 * mm
        y0 = wrapped(c, note, MARGIN, y0, W - 2 * MARGIN, 'Sans', 11.5, 16.5, PLUM)
        return y0 - 8 * mm

    # ============ Seite 1: Cover ============
    bg(c, COVER_BG)
    c.setStrokeColor(ACCENT2)
    c.setLineWidth(1.4)
    c.line(MARGIN, H - 116 * mm, W - MARGIN, H - 116 * mm)
    heart(c, W / 2, H - 40 * mm, 4.2, ACCENT2)
    c.setFont('Sans-Bold', 13)
    c.setFillColor(ACCENT2)
    c.drawCentredString(W / 2, H - 58 * mm, "D E I N   B O N U S")
    c.setFont('Serif-Bold', 26)
    c.setFillColor(COVER_TEXT)
    c.drawCentredString(W / 2, H - 75 * mm, "Vertiefende Übungen zu")
    c.setFont('Serif-Bold', cfg.get('title_size', 24))
    yy = H - 92 * mm
    for l in cfg['title_lines']:
        c.setFillColor(ACCENT2)
        c.drawCentredString(W / 2, yy, l)
        yy -= cfg.get('title_leading', 10) * mm

    pill_w = cfg.get('pill_w', 96) * mm
    rounded(c, W / 2 - pill_w / 2, H - 152 * mm, pill_w, 17 * mm, 8 * mm, ACCENT, stroke=None)
    c.setFont('Sans', 11.5)
    c.setFillColor(WHITE)
    c.drawCentredString(W / 2, H - 142 * mm, cfg['pill_line1'])
    c.drawCentredString(W / 2, H - 147 * mm, cfg['pill_line2'])

    c.setFont('Serif-It', 15)
    c.setFillColor(COVER_TEXT)
    c.drawCentredString(W / 2, 55 * mm, "Petra Tanner")
    c.setFont('Sans-Bold', 11)
    c.setFillColor(ACCENT2)
    c.drawCentredString(W / 2, 47 * mm, "SAFE TO THRIVE")
    footer(1, "Bonus-PDF", ACCENT2)
    c.showPage()

    # ============ Seite 2: Willkommen ============
    bg(c, CREAM)
    rounded(c, MARGIN, H - 62 * mm, W - 2 * MARGIN, 34 * mm, 6 * mm, ACCENT_LIGHT)
    c.setFont('Serif-Bold', 19)
    c.setFillColor(ACCENT_DARK)
    c.drawCentredString(W / 2, H - 43 * mm, cfg['welcome_title1'])
    c.drawCentredString(W / 2, H - 51 * mm, cfg['welcome_title2'])
    y = H - 76 * mm
    y = wrapped(c, cfg['welcome_intro1'], MARGIN, y, W - 2 * MARGIN, 'Sans', 12, 17, PLUM)
    y -= 5 * mm
    y = wrapped(c, cfg['welcome_intro2'], MARGIN, y, W - 2 * MARGIN, 'Sans', 12, 17, PLUM)

    y -= 12 * mm
    box_h = 58 * mm
    rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, ACCENT2_LIGHT)
    c.setFont('Serif-Bold', 13.5)
    c.setFillColor(ACCENT2_DARK)
    c.drawString(MARGIN + 8 * mm, y - 10 * mm, "Was dich erwartet")
    yy = y - 19 * mm
    c.setFont('Sans', 11.5)
    c.setFillColor(PLUM)
    for i, ex in enumerate(cfg['exercises'], 1):
        c.drawString(MARGIN + 8 * mm, yy, f"{i}.  {ex['title']}")
        yy -= 6.6 * mm
    footer(2, f"Bonus-PDF · {cfg['book_title_short']}", ACCENT_DARK)
    c.showPage()

    # ============ Uebungsseiten ============
    for i, ex in enumerate(cfg['exercises'], 1):
        track = ex.get('track', 'A')
        color, dark, tint = ((ACCENT, ACCENT_DARK, ACCENT_LIGHT) if track == 'A'
                              else (ACCENT2, ACCENT2_DARK, ACCENT2_LIGHT))
        y = section_header(i, ex['title'], ex['intro'], color, tint)
        kind = ex['kind']

        if kind == 'lines':
            box_h = ex.get('box_h', 70) * mm
            rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
            yy = y - 15 * mm
            for _ in range(ex.get('n_lines', 5)):
                blank_line(c, MARGIN + 10 * mm, yy, W - 2 * MARGIN - 20 * mm, LINE)
                yy -= 11.5 * mm
            if ex.get('note'):
                wrapped(c, ex['note'], MARGIN, y - box_h - 10 * mm, W - 2 * MARGIN,
                        'Serif-It', 10.5, 14, dark)

        elif kind == 'numbered':
            box_h = ex.get('box_h', 55) * mm
            rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
            head_off = 0
            if ex.get('heading'):
                c.setFont('Sans-Bold', 11)
                c.setFillColor(dark)
                hy = y - 10 * mm
                for hl in ex['heading']:
                    c.drawString(MARGIN + 8 * mm, hy, hl)
                    hy -= 5 * mm
                head_off = 5 * mm * len(ex['heading']) + 4 * mm
            yy = y - 16 * mm - head_off
            for i2 in range(1, ex.get('n_items', 3) + 1):
                number_badge_soft(c, MARGIN + 16 * mm, yy + 1.6 * mm, 4 * mm, i2, dark, tint)
                blank_line(c, MARGIN + 26 * mm, yy, W - 2 * MARGIN - 36 * mm, LINE)
                yy -= ex.get('item_gap', 15) * mm
            if ex.get('extra_label'):
                c.setFont('Sans-Bold', 11)
                c.setFillColor(dark)
                c.drawString(MARGIN + 8 * mm, yy - 3 * mm, ex['extra_label'])
                blank_line(c, MARGIN + 8 * mm, yy - 13 * mm, W - 2 * MARGIN - 16 * mm, LINE)
            if ex.get('note'):
                wrapped(c, ex['note'], MARGIN, y - box_h - 10 * mm, W - 2 * MARGIN,
                        'Serif-It', 10.5, 14, dark)

        elif kind == 'table':
            rows_h = ex.get('row_h', 22) * mm
            for r in range(ex.get('n_rows', 3)):
                top = y - r * (rows_h + 4 * mm)
                rounded(c, MARGIN, top - rows_h, W - 2 * MARGIN, rows_h, 5 * mm, WHITE, stroke=LINE)
                c.setFont('Sans-Bold', 10.5)
                c.setFillColor(dark)
                c.drawString(MARGIN + 7 * mm, top - 7 * mm, ex['field1'])
                blank_line(c, MARGIN + 55 * mm, top - 8 * mm, W - 2 * MARGIN - 63 * mm, LINE)
                c.drawString(MARGIN + 7 * mm, top - 14 * mm, ex['field2'])
                blank_line(c, MARGIN + 55 * mm, top - 15 * mm, 40 * mm, LINE)
                c.setFont('Sans', 9.5)
                c.setFillColor(PLUM)
                for li, extra_line in enumerate(ex.get('field3_lines', [])):
                    c.drawString(MARGIN + 100 * mm, top - 14 * mm - li * 4.5 * mm, extra_line)

        elif kind == 'qa':
            yy = y
            for q in ex['questions']:
                box_h = ex.get('box_h', 26) * mm
                rounded(c, MARGIN, yy - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
                wrapped(c, q, MARGIN + 7 * mm, yy - 8 * mm, W - 2 * MARGIN - 14 * mm,
                        'Sans-Bold', 10.5, 13, dark)
                blank_line(c, MARGIN + 7 * mm, yy - box_h + 7 * mm, W - 2 * MARGIN - 14 * mm, LINE)
                yy -= box_h + 6 * mm

        elif kind == 'closing_note':
            box_h = ex.get('box_h', 34) * mm
            rounded(c, MARGIN, y - box_h, W - 2 * MARGIN, box_h, 6 * mm, WHITE, stroke=LINE)
            blank_line(c, MARGIN + 10 * mm, y - 14 * mm, W - 2 * MARGIN - 20 * mm, LINE)
            blank_line(c, MARGIN + 10 * mm, y - 24 * mm, W - 2 * MARGIN - 20 * mm, LINE)
            y2 = y - box_h - 12 * mm
            rounded(c, MARGIN, y2 - 26 * mm, W - 2 * MARGIN, 26 * mm, 6 * mm, tint)
            wrapped(c, ex['contact_note'], MARGIN + 8 * mm, y2 - 9 * mm, W - 2 * MARGIN - 16 * mm,
                    'Sans', 11, 15, PLUM)
            c.setFont('Sans-Bold', 12)
            c.setFillColor(dark)
            c.drawCentredString(W / 2, y2 - 21 * mm, cfg['contact_email'])

        footer(i + 2, f"Übung {i}", dark)
        c.showPage()

    # ============ Letzte Seite: Zum Schluss / rechtliches ============
    bg(c, CREAM)
    rounded(c, 0, H - 60 * mm, W, 60 * mm, 0, COVER_BG)
    heart(c, W / 2, H - 26 * mm, 3.4, ACCENT2)
    c.setFont('Serif-Bold', 20)
    c.setFillColor(COVER_TEXT)
    c.drawCentredString(W / 2, H - 40 * mm, "Zum Schluss")

    y = H - 78 * mm
    disclaimer = ("Dieses Bonus-PDF ersetzt keine medizinische, psychologische oder "
        "psychotherapeutische Beratung, Diagnose oder Behandlung. Es stellt keine "
        "Diagnose und gibt keine Heilversprechen. Du handelst auf eigene "
        "Verantwortung. Bei anhaltenden Beschwerden wende dich bitte an eine "
        "Ärztin, einen Arzt, eine Therapeutin oder eine andere Fachperson.")
    y = wrapped(c, disclaimer, MARGIN, y, W - 2 * MARGIN, 'Sans', 10.5, 15, PLUM)

    y -= 10 * mm
    rounded(c, MARGIN, y - 24 * mm, W - 2 * MARGIN, 24 * mm, 6 * mm, ACCENT_LIGHT)
    c.setFont('Sans-Bold', 11.5)
    c.setFillColor(ACCENT_DARK)
    c.drawCentredString(W / 2, y - 7.5 * mm, "Bei einer akuten Krise")
    c.setFont('Sans', 11)
    c.setFillColor(PLUM)
    c.drawCentredString(W / 2, y - 14.5 * mm, "Schweiz 143 · Deutschland 0800 111 0 111 · Österreich 142")
    c.setFont('Sans', 9)
    c.drawCentredString(W / 2, y - 19 * mm, "Kostenlos, anonym, Tag und Nacht.")

    y -= 38 * mm
    copyright_txt = ("© Petra Tanner, Safe to Thrive. Alle Rechte vorbehalten. Nur für den "
        "persönlichen Gebrauch, nicht zur Weitergabe oder Veröffentlichung bestimmt.")
    y = wrapped(c, copyright_txt, MARGIN, y, W - 2 * MARGIN, 'Sans', 9.5, 13,
                HexColor('#7A6A66'), align='center')
    c.setFont('Sans-Bold', 10.5)
    c.setFillColor(ACCENT2_DARK)
    c.drawCentredString(W / 2, y - 6 * mm, cfg['contact_email'])
    footer(len(cfg['exercises']) + 3, "Safe to Thrive", ACCENT_DARK)
    c.showPage()

    c.save()
    print("Bonus-PDF erstellt:", OUT)
