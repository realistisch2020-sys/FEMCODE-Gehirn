# -*- coding: utf-8 -*-
"""Baut ein Kindle-eBook (EPUB) direkt aus einem Manuskript ohne Word-
Formatvorlagen (wie tools/manuskript-word2pdf.py fuers Taschenbuch).

Titel/Ueberschrift/Fliesstext werden ueber die Schriftgroesse erkannt, nicht
ueber Formatvorlagen. Das Papier-Inhaltsverzeichnis (mit Tab und Seitenzahl-
Charakter) wird uebersprungen, die eReader-Navigation ersetzt es.

    python3 tools/manuskript-ebook.py <manuskript.docx> <ausgabe.epub> "<Titel>" "<Untertitel>" "<Autor>"
"""
import re
import sys
from docx import Document
from ebooklib import epub

_TIKTOK_PREFIX = re.compile(r'TikTok\s*(?:&#183;|·)?\s*', re.IGNORECASE)
_EBOOKONLY_PREFIX = re.compile(r'EBOOKONLY\s*(?:&#183;|·)?\s*', re.IGNORECASE)

DOCX = sys.argv[1]
OUT = sys.argv[2]
TITEL = sys.argv[3]
UNTERTITEL = sys.argv[4]
AUTOR = sys.argv[5] if len(sys.argv) > 5 else 'Petra Tanner'
KONTAKT = 'info.safetothrive@gmail.com'

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A_NS = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def eingebettetes_bild(p):
    """Bildbytes eines inline eingefuegten Bildes (z.B. QR-Code) in diesem
    Absatz, sonst None."""
    for blip in p._p.findall('.//{%s}blip' % A_NS):
        rId = blip.get('{%s}embed' % R_NS)
        if rId:
            return p.part.related_parts[rId].blob
    return None


def hat_inline_umbruch(p):
    for br in p._p.iter(NS + 'br'):
        if br.get(NS + 'type') == 'page':
            return True
    return False


def groesse(p):
    for r in p.runs:
        if r.text.strip():
            s = r.font.size.pt if r.font.size else None
            if s and s > 40:
                s = s / 10.0
            return s
    return None


def laufweite_html(p):
    teile = []
    for r in p.runs:
        t = r.text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        if not t:
            continue
        if r.bold:
            t = '<b>%s</b>' % t
        if r.italic:
            t = '<i>%s</i>' % t
        teile.append(t)
    return ''.join(teile) if teile else p.text


def baue():
    d = Document(DOCX)
    ps = d.paragraphs

    buch = epub.EpubBook()
    buch.set_identifier('femcode-gehirn-%s' % OUT.split('/')[-1])
    buch.set_title(TITEL)
    buch.set_language('de')
    buch.add_author(AUTOR)

    titel_html = '''
    <div style="text-align:center; margin-top:20%%;">
      <h1>%s</h1>
      <p style="margin-top:1em;"><i>%s</i></p>
      <p style="margin-top:3em;">%s<br/>Safe to Thrive</p>
    </div>''' % (TITEL, UNTERTITEL, AUTOR)
    titelseite = epub.EpubHtml(title='Titelseite', file_name='titel.xhtml', lang='de')
    titelseite.content = titel_html
    buch.add_item(titelseite)

    kapitel_items = [titelseite]
    spine = ['nav', titelseite]
    toc = []

    # Start: erster Absatz nach dem zweiten Inline-Seitenumbruch (nach dem
    # Papier-Inhaltsverzeichnis).
    umbrueche = [i for i, p in enumerate(ps) if hat_inline_umbruch(p)]
    start = umbrueche[1] + 1 if len(umbrueche) >= 2 else 0

    zaehler = 0
    bild_zaehler = 0
    aktuelle_seite = None
    html_buffer = []

    def neue_seite(titel):
        nonlocal aktuelle_seite, zaehler
        if aktuelle_seite is not None:
            aktuelle_seite.content = '<div>%s</div>' % ''.join(html_buffer)
            html_buffer.clear()
        zaehler += 1
        dateiname = 'kap_%03d.xhtml' % zaehler
        seite = epub.EpubHtml(title=titel, file_name=dateiname, lang='de')
        buch.add_item(seite)
        kapitel_items.append(seite)
        spine.append(seite)
        aktuelle_seite = seite
        return seite

    for i in range(start, len(ps)):
        p = ps[i]
        text = p.text.strip()
        bild = eingebettetes_bild(p)
        if bild is not None and aktuelle_seite is not None:
            bild_zaehler += 1
            bild_name = 'bild_%03d.png' % bild_zaehler
            bild_item = epub.EpubItem(uid='img%d' % bild_zaehler, file_name=bild_name,
                                       media_type='image/png', content=bild)
            buch.add_item(bild_item)
            html_buffer.append(
                '<p style="text-align:center;"><img src="%s" alt="QR-Code" '
                'style="max-width:45%%;"/></p>' % bild_name)
            continue
        if not text:
            continue
        size = groesse(p)

        if size and 15 <= size < 20:
            seite = neue_seite(text)
            html_buffer.append('<h1>%s</h1>' % text)
            toc.append(epub.Link(seite.file_name, seite.title,
                                  seite.file_name.replace('.xhtml', '')))
        elif text.startswith('TikTok'):
            if aktuelle_seite is None:
                neue_seite(text[:30])
                toc.append(epub.Link(aktuelle_seite.file_name, aktuelle_seite.title,
                                      aktuelle_seite.file_name.replace('.xhtml', '')))
            zitat = _TIKTOK_PREFIX.sub('', laufweite_html(p), count=1)
            html_buffer.append('<p class="zitat">%s</p>' % zitat)
        else:
            if aktuelle_seite is None:
                neue_seite(text[:30])
                toc.append(epub.Link(aktuelle_seite.file_name, aktuelle_seite.title,
                                      aktuelle_seite.file_name.replace('.xhtml', '')))
            html_buffer.append('<p>%s</p>' % _EBOOKONLY_PREFIX.sub('', laufweite_html(p), count=1))

    if aktuelle_seite is not None:
        aktuelle_seite.content = '<div>%s</div>' % ''.join(html_buffer)

    css = '''
    body { font-family: serif; line-height: 1.5; }
    h1 { text-align:center; margin-top:1.5em; }
    p { margin: 0 0 0.8em 0; text-indent: 0; }
    p.zitat { background: #efece6; font-style: italic; padding: 0.8em 1em;
              margin: 1em 0; }
    '''
    stil_datei = epub.EpubItem(uid='stil', file_name='stil.css',
                                media_type='text/css', content=css)
    buch.add_item(stil_datei)
    for item in kapitel_items:
        item.add_item(stil_datei)

    buch.toc = tuple(toc)
    buch.add_item(epub.EpubNcx())
    buch.add_item(epub.EpubNav())
    buch.spine = spine

    epub.write_epub(OUT, buch)
    print('eBook erstellt:', OUT)
    print('  Kapitel/Seiten:', zaehler)

    voll = '\n'.join(p.text for p in ps[start:])
    fehlt = [k for k in ('Haftungsausschluss', 'Zur Autorin',
                          'Notfall und professionelle Hilfe', KONTAKT)
             if k not in voll]
    if fehlt:
        print('  ACHTUNG, im eBook-Text fehlt:', fehlt)
    else:
        print('  Pflichtteile vorhanden.')


if __name__ == '__main__':
    baue()
