# -*- coding: utf-8 -*-
"""Baut das Kindle-eBook (EPUB) aus der massgeblichen Word-Datei.

Anders als beim Taschenbuch gibt es hier keine Seitenzahlen: Kindle-Text
fliesst, das Inhaltsverzeichnis wird ueber die eReader-Navigation verlinkt,
nicht ueber Seitenzahlen. Deshalb wird der alte Papier-TOC (mit Tab und
Seitenzahl) nicht mit uebernommen, sondern durch die EPUB-Navigation ersetzt.

    python3 tools/buch6-ebook.py
"""
from docx import Document
from ebooklib import epub

QUELLE = 'outputs/buch6/buch6-MANUSKRIPT.docx'
ZIEL = 'outputs/buch6/buch6-eBook.epub'
KONTAKT = 'beyondlimitsnow25@gmail.com'


def laufweite_html(p):
    """Absatztext mit Fett/Kursiv aus den Runs, als HTML."""
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
    d = Document(QUELLE)
    ps = d.paragraphs

    buch = epub.EpubBook()
    buch.set_identifier('femcode-gehirn-buch6')
    buch.set_title('Ich bin so müde. Und niemand fragt mich warum')
    buch.set_language('de')
    buch.add_author('Petra Tanner')

    # ─── Titelseite ─────────────────────────────────────────────────────────
    titel_html = '''
    <div style="text-align:center; margin-top:20%;">
      <h1>Ich bin so müde.</h1>
      <h2>Und niemand fragt mich warum</h2>
      <p style="margin-top:2em;"><i>Das Funktions-Ich</i><br/>
      Wenn du für alle stark bist und dich dabei verlierst</p>
      <p style="margin-top:3em;">Petra Tanner<br/>Safe to Thrive</p>
    </div>'''
    titelseite = epub.EpubHtml(title='Titelseite', file_name='titel.xhtml', lang='de')
    titelseite.content = titel_html
    buch.add_item(titelseite)

    widmung_html = '''
    <div style="text-align:center; margin-top:30%;">
      <p><i>Für alle Frauen,<br/>die im Auto weinen, damit es niemand sieht.</i></p>
      <p style="margin-top:2em;">Es ist Zeit, dass jemand fragt.</p>
    </div>'''
    widmung = epub.EpubHtml(title='Widmung', file_name='widmung.xhtml', lang='de')
    widmung.content = widmung_html
    buch.add_item(widmung)

    kapitel_items = [titelseite, widmung]
    spine = ['nav', titelseite, widmung]
    toc = []

    # ─── Body ab "Einleitung" (Index 50), TOC-Papierseite (15-49) auslassen ─
    start = next(i for i, p in enumerate(ps) if p.style.name == 'Heading 1'
                 and p.text.strip() == 'Einleitung')

    aktuelles_h1 = None
    aktuelles_h1_kinder = []
    zaehler = 0

    def schliesse_h1():
        nonlocal aktuelles_h1, aktuelles_h1_kinder
        if aktuelles_h1 is not None:
            if aktuelles_h1_kinder:
                toc.append((epub.Link(aktuelles_h1.file_name, aktuelles_h1.title,
                                       aktuelles_h1.file_name.replace('.xhtml', '')),
                            aktuelles_h1_kinder))
            else:
                toc.append(epub.Link(aktuelles_h1.file_name, aktuelles_h1.title,
                                      aktuelles_h1.file_name.replace('.xhtml', '')))
        aktuelles_h1 = None
        aktuelles_h1_kinder = []

    html_buffer = []
    aktuelle_seite = None

    def neue_seite(titel, ist_h2=False):
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
        stil = p.style.name
        text = p.text.strip()

        if stil == 'Heading 1':
            schliesse_h1()
            seite = neue_seite(text)
            aktuelles_h1 = seite
            html_buffer.append('<h1>%s</h1>' % text)
        elif stil == 'Heading 2':
            seite = neue_seite(text, ist_h2=True)
            html_buffer.append('<h2>%s</h2>' % text)
            if aktuelles_h1 is not None:
                aktuelles_h1_kinder.append(
                    epub.Link(seite.file_name, seite.title,
                              seite.file_name.replace('.xhtml', '')))
        else:
            if not text:
                continue
            html_buffer.append('<p>%s</p>' % laufweite_html(p))

    if aktuelle_seite is not None:
        aktuelle_seite.content = '<div>%s</div>' % ''.join(html_buffer)
    schliesse_h1()

    # ─── CSS ────────────────────────────────────────────────────────────────
    css = '''
    body { font-family: serif; line-height: 1.5; }
    h1 { text-align:center; margin-top:2em; }
    h2 { text-align:center; margin-top:1.5em; }
    p { margin: 0 0 0.8em 0; text-indent: 0; }
    '''
    stil_datei = epub.EpubItem(uid='stil', file_name='stil.css',
                                media_type='text/css', content=css)
    buch.add_item(stil_datei)
    for item in kapitel_items:
        item.add_item(stil_datei)

    buch.toc = tuple(toc)
    buch.add_item(epub.EpubNcx())
    nav = epub.EpubNav()
    buch.add_item(nav)
    buch.spine = spine

    epub.write_epub(ZIEL, buch)
    print('eBook erstellt: %s' % ZIEL)
    print('  Kapitel/Seiten: %d' % zaehler)

    # Pflichtangaben pruefen
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
