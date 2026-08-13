# KDP Buch-Produktion — Gelerntes

Alles, was beim Erstellen von Buch 3 und Buch 4 sehr viel Zeit gekostet hat. Diese Regeln gelten für jedes weitere Buch.

---

## Cover-Gestaltung — Titelstruktur

**Bewährtes Layout (ab Buch 5):**

Kurze, kraftvolle Zeilen — das erste/stärkste Wort riesig (200px Bold), dann Folgezeilen gross (130px Bold), und den letzten Teil des Titels klein kursiv darunter — wie geflüstert.

Beispiel Buch 5:
```
NIEMAND          ← riesig, weiss (200px Bold)
HAT DICH         ← gross, Gold  (130px Bold)
GEFRAGT          ← gross, Gold  (130px Bold)
wie es dir geht  ← klein kursiv, Cream (62px Italic)
```

**Regel:** Langen Titel nie komplett in Grossbuchstaben und gleicher Grösse durchziehen. Das kämpft mit dem Bild. Stattdessen: Hierarchie durch Grösse + Stil.

**Untertitel:** Mit Vertikallinie links (4px, Gold), Caps Regular + Kursiv Gold.

**Autor-Block unten:** Zentriert, Trennlinie Gold, Punkt als Trenner zwischen Name und Publisher.

**Kein Bild mit Person nötig** — abstrakte Bilder (fliessende Formen, organische Strukturen) funktionieren stärker, weil sich jede Leserin selbst darin sehen kann.

**ChatGPT-Prompt-Formel für abstrakte Cover:**
> Abstract book cover art, flowing organic 3D shapes like liquid silk or draped fabric. Colors: [Hauptfarbe] background, [Kontrastfarbe] flowing forms, [Akzent] gold lines and sphere focal point. Left side slightly darker for text overlay. No text, no people. Mood: [Emotion].

---

## Manuskript-Format (PDF, nicht DOCX)

**Problem:** DOCX mit Georgia/benutzerdefinierten Fonts wird von KDP auf Linux gerendert. Da Georgia nicht eingebettet ist, substituiert KDP einen riesigen Fallback-Font → 800+ Seiten statt 70–130.

**Lösung: Immer ReportLab PDF mit eingebetteten Liberation Serif Fonts.**

```
Script: /tmp/.../scratchpad/build_pdf.py
Fonts: /usr/share/fonts/truetype/liberation/
  LiberationSerif-Regular.ttf
  LiberationSerif-Bold.ttf
  LiberationSerif-Italic.ttf
  LiberationSerif-BoldItalic.ttf
```

**Einstellungen KDP Taschenbuch:**
- Seitengrösse: 5.5 × 8.5 Zoll
- Ränder: links=1.1", rechts=0.8", oben=0.9", unten=0.75"
- Schriftgrösse: 11pt Body, 17pt Kapitelüberschrift
- Seitenzahl: ab Seite 3, zentriert, y=0.35" vom unteren Rand
- Erste 2 Seiten (Titelseite + Inhaltsverzeichnis): KEINE Seitenzahl
- Schwarz/Weiss, mattes Papier

**Seitenanzahl und Rückenbreite:**
- Weisspapier: Seiten × 0.002252" × 300 DPI = Rückenbreite in Pixeln
- 72 Seiten → 49px Rücken
- 123 Seiten → 83px Rücken

---

## Full-Wrap Cover (PDF)

**Canvas-Grösse bei 300 DPI:**
```
BLEED = 38px (0.125")
PAGE_W = 1650px (5.5")
PAGE_H = 2550px (8.5")
TOTAL_W = 38 + 1650 + SPINE + 1650 + 38
TOTAL_H = 38 + 2550 + 38 = 2626px
```

**Sicherheitsabstand Rückseite: 0.5" = 150px von allen Kanten**
```
BL = BLEED + 150 = 188px   (linker Textrand)
BR = BLEED + PAGE_W - 150 = 1538px  (rechter Textrand)
TW = BR - BL = 1350px   (Textbreite)
BT = BLEED + 150 = 188px   (oberer Textrand)
BB = BLEED + PAGE_H - 150 = 2438px  (unterer Textrand)
```

**Wichtig:** Niemals mehr als 150px Rand vom Bleed-Rand — sonst wird Text im Druck abgeschnitten. Niemals weniger — dann landet Text zu nah am Schnitt.

**Schriftgrössen Rückseite (bewährt):**
- Klappentext-Überschrift: Bold 30px
- Klappentext-Body: Regular 26px
- Autorin-Name: Bold 30px
- Biografie-Zeile: Regular 24px
- E-Mail / Publisher: Regular 22px

**Textumbruch:** Immer `font.getlength()` (Pillow) für pixelgenaue Messung — NICHT `textwrap.wrap()` mit Zeichenzahl-Schätzung. Schätzung produziert einzelne Wörter pro Zeile.

```python
def wrap_text_px(text, font, max_px):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if font.getlength(t) <= max_px:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines
```

**Cover PDF speichern — NUR über ReportLab (nicht PIL .save('PDF')):**
```python
from reportlab.pdfgen import canvas as rl_canvas
W_pt, H_pt = W/300*72, H/300*72
c = rl_canvas.Canvas(OUT_PDF, pagesize=(W_pt, H_pt))
c.drawInlineImage(canvas, 0, 0, width=W_pt, height=H_pt)
c.save()
```
PIL `.save('PDF')` dreht das Bild um 90° — falsch.

**Rücken (Spine):**
- Bild in Querformat zeichnen, dann um 90° drehen:
```python
spine_img = Image.new('RGB', (PAGE_H, SPINE), bg_color)
# Text darauf zeichnen
spine_rotated = spine_img.rotate(90, expand=True)
canvas.paste(spine_rotated, (spine_x, BLEED))
```

**Barcode:** KDP fügt den Barcode automatisch hinzu — KEINEN Platzhalter ins Cover einbauen.

---

## Textstil — Deutsch / Schweizerdeutsch

- Kein Em-Dash (—) als Trenner im Fliesstext und auf Covern. Stattdessen Komma oder Punkt.
- Schweizer Schreibung: „ss" statt „ß"
- Keine Aufzählungszeichen mit Strichen
- Grossschreibung: „Ja", „Nein" als Nomen
- Kommas vor Relativsätzen und nach einleitenden Elementen
- Keine KI-typischen Phrasen ("Es ist wichtig, dass…", "Zusammenfassend lässt sich sagen…")

---

## KDP Preisaktionen

### eBook — Kindle Countdown Deal (Aktionspreis möglich)

1. kdp.amazon.com → eBook → "Buch bearbeiten"
2. Reiter **KDP Select** aktivieren (Buch muss 90 Tage exklusiv bei Amazon sein)
3. Danach unter **"Werbung"** → **"Kindle Countdown Deal"**
4. Datum + Aktionspreis setzen (mind. 20% unter Normalpreis, mind. $0.99)
5. Vorteil: 70% Tantieme bleibt auch während des Deals erhalten

### Taschenbuch — KEIN Aktionspreis möglich

KDP bietet für Print-Bücher keine Countdown Deals oder zeitlich begrenzte Aktionspreise an. Einzige Möglichkeit: den Listenpreis dauerhaft senken. Für Aktionen daher immer das eBook nutzen, nicht das Taschenbuch.

---

## Cross-Promotion zwischen den Büchern (ab Buch 5 Standard)

Jedes neue Buch verweist am Ende auf die anderen Bücher der Reihe — im Abschnitt "Wenn du mehr möchtest".

**Pflicht-Elemente im Backmatter:**
- Kurze Beschreibung jedes anderen Buches (1–2 Sätze, Titel fett)
- Amazon-Link oder QR-Code zur Buchseite (sobald ISBN/ASIN bekannt)
- Hinweis: "Alle Bücher sind auch als eBook erhältlich"

**QR-Code generieren:**
- Kostenlos auf qr-code-generator.com oder ähnlich
- URL: amazon.de/dp/[ASIN] des jeweiligen Buches
- Als PNG einbetten — im ReportLab-Script mit `Image()` einfügen

**Reihenfolge der Bücher (für Backmatter-Text):**
1. "Wenn Beziehungen erschöpfen" — Warum du gibst, bis nichts mehr von dir übrig ist
2. "Das schlechte Gewissen" — Warum du dich immer schuldig fühlst
3. "Niemand hat dich gefragt, wie es dir geht" — Warum du nicht weisst, was du fühlst

**Buch 5 Manuskript noch anpassen:** Abschnitt "Wenn du mehr möchtest" bereits vorhanden — QR-Codes ergänzen sobald ASINs bekannt sind.

---

## KDP-Einreichung Reihenfolge

1. Manuskript-PDF hochladen → Seitenanzahl notieren
2. Spine-Breite berechnen: Seiten × 0.002252" × 300
3. Cover-PDF mit korrekter Spine-Breite generieren
4. Cover-PDF hochladen
5. KI-Angaben: Texte = "Gesamtes Werk, mit umfangreicher Bearbeitung", Bilder = "Gesamtes Werk, mit minimaler oder keiner Bearbeitung"
6. Preis setzen (Empfehlung: $12.99–$13.99 je nach Seitenzahl)

**Druckkosten-Schätzung B&W, 5.5×8.5", matte:**
- ~72 Seiten: $2.15 → Empfehlung $12.99 → Royalty ~$4.94–5.54
- ~123 Seiten: $2.85 → Empfehlung $13.99 → Royalty ~$5.54

---

## Kontakt im Buch (immer)

- Öffentlich / im Buch: **info.safetothrive@gmail.com**
- Privat / NIEMALS im Buch: tanner.pe@bluewin.ch

---

## Amazon Keywords (7 Felder pro Buch, je max. 50 Zeichen)

KDP → Buchdetails bearbeiten → "Schlüsselwörter". Phrasen statt Einzelwörter.

### Buch 3 — Wenn Beziehungen erschöpfen
1. `Beziehungen erschöpfen sich auflösen`
2. `zu viel geben in Beziehungen Frauen`
3. `emotionale Erschöpfung Partnerschaft`
4. `Grenzen setzen Beziehung lernen`
5. `für andere da sein eigene Bedürfnisse`
6. `Selbstfürsorge Frauen Ratgeber`
7. `toxische Beziehungsmuster erkennen`

### Buch 4 — Das schlechte Gewissen
1. `schlechtes Gewissen loswerden Frauen`
2. `Schuldgefühle überwinden Ratgeber`
3. `immer schuldig fühlen warum`
4. `Nein sagen lernen ohne Schuldgefühle`
5. `Schuldgefühle aus der Kindheit`
6. `sich entschuldigen aufhören`
7. `emotionale Unabhängigkeit Selbstwert`

### Buch 5 — Niemand hat dich gefragt, wie es dir geht
1. `eigene Gefühle nicht kennen Frauen`
2. `emotionale Vernachlässigung Kindheit`
3. `Gefühle wahrnehmen lernen`
4. `innere Leere Ursache überwinden`
5. `sich selbst finden nach Kindheit`
6. `funktionieren statt leben Frauen`
7. `Selbstwahrnehmung stärken Ratgeber`

---

## Fertige Bücher

| Buch | Titel | Seiten | Manuskript-PDF | Cover-PDF | KDP-Status |
|---|---|---|---|---|---|
| Buch 3 | Wenn Beziehungen erschöpfen | 149 | outputs/buch-beziehungen/wenn-beziehungen-erschoepfen-Taschenbuch.pdf | outputs/buch-beziehungen/wenn-beziehungen-erschoepfen-Cover-Print-FullWrap.pdf | Live, Bewertungen vorhanden |
| Buch 4 | Das schlechte Gewissen | 106 | outputs/buch-schuldgefuehle/das-schlechte-gewissen-Taschenbuch.pdf | outputs/buch-schuldgefuehle/das-schlechte-gewissen-Cover-Print-FullWrap.pdf | Live, Bewertungen vorhanden, Ads laufen |
| Buch 5 | Niemand hat dich gefragt, wie es dir geht | 61 | outputs/buch-niemand-gefragt/niemand-hat-dich-gefragt-Taschenbuch.pdf | Full-Wrap fehlt noch | Rechtssicherheit/Cover offen |
| Buch 6 | Ich bin so müde. Und niemand fragt mich warum | 111 | outputs/buch6/buch6-Taschenbuch.pdf | outputs/buch6/buch6-Cover-FullWrap.pdf | Live |
| Buch 7 | Ich habe nie gelernt, an mich zu denken | 75 (Zielumfang ~100 bewusst nicht erreicht, Petra hat 75 Seiten final freigegeben) | outputs/buch-an-mich-denken/buch4-Taschenbuch.pdf | outputs/buch-an-mich-denken/buch4-Cover-Print-FullWrap.pdf | Bereit für Upload (Manuskript, Cover, eBook geprüft, Stand 13. August 2026), noch nicht hochgeladen |

Alle vier Bücher (3, 4, 6, in Arbeit auch 7) enthalten jetzt vor dem
Impressum den Abschnitt „Ein letztes Wort" — eine Bewertungs-Bitte im
Franzi-Rhythmus, ohne jede Gegenleistung (Anreiz-Rezensionen sind bei
Amazon verboten, Kontosperrungsrisiko, siehe `plans/safe-to-thrive-masterplan.md`).

## A+ Content — Technik-Lehren (August 2026)

Für jedes Buch drei Module: Zitatkarte, „Was dich erwartet"
(Themenübersicht), Cross-Promotion (Cover der anderen Bücher). Bild- und
Textvorlagen liegen in den jeweiligen `outputs/<buch>/`-Ordnern
(`werbung-zitatkarte-*.png`, `aplus-was-dich-erwartet.png`) und einmal
gemeinsam in `outputs/aplus-cross-promotion.png`.

**Wichtigste Lehre: A+-Module brauchen Querformat, nicht Instagram-Hochformat.**
Die für Social Media gebauten Zitatkarten (1080×1350, Hochformat) werden
von den KDP-A+-Modulen abgelehnt bzw. nicht richtig übernommen — die
Module verlangen mindestens 970×300px im **Querformat**. Immer eine
eigene Querformat-Version bauen (970×600 hat sich bewährt), Dateiname
mit `-quer-` kennzeichnen, um sie von der Social-Media-Version zu
unterscheiden.

**Cross-Promotion-Bild:** Mindesthöhe 600px (nicht 300px wie ursprünglich
gebaut). Nur die tatsächlich veröffentlichten Bücher zeigen — ein noch
nicht live geschaltetes Buch nicht mit abbilden, das verwirrt Leserinnen
auf einer Produktseite, wo es das Buch noch nicht zu kaufen gibt.

**Bekannter KDP-Bug: „Project could not be deserialized" beim Speichern.**
Tritt gelegentlich beim „Als Entwurf speichern" oder in der Vorschau auf,
unabhängig von Bild-/Textqualität (Bilder vorher immer trotzdem prüfen:
PNG, RGB, richtige Grösse — war in unseren Fällen nie die Ursache).
Bekannte Abhilfen, der Reihe nach probieren:
1. Einzeln speichern (erst Bild, dann Überschrift, dann Text), nicht alles auf einmal
2. Bei zwei Modulen mit exakt demselben Layout-Typ: eines auf ein anderes Layout wechseln
3. Neuer Entwurf in einem frischen Browser/Inkognito-Fenster, statt den hängenden Entwurf zu reparieren
4. Bleibt es bestehen: KDP-Support kontaktieren, Fehlermeldung + Reproduktionsschritte mitgeben

**ASIN-Zuordnung zuerst machen, nicht zuletzt.** Reihenfolge, die weniger
Fehler produziert hat: ASINs anwenden (Kindle- und Taschenbuch-ASIN
beide), erst danach die drei Module befüllen. Ein Buch hat zwei ASINs
(Kindle + Taschenbuch), A+ Content gilt für beide, wenn man beim
Zuordnen beide anhakt.

**Vorsicht vor doppelten Entwürfen.** Der A+-Inhaltsmanager zeigt alle
Entwürfe zu einem Buch in einer Liste — es kann leicht ein zweiter,
neuer Entwurf neben einem älteren entstehen. Vor dem Weiterarbeiten
immer prüfen, mit welchem Entwurf man gerade verbunden ist (Titel + Datum
„Zuletzt geändert" oben auf der Seite).

## Journal-Serie (Workbooks zu Buch 4, 3, 6)

Jedes Hauptbuch hat inzwischen ein eigenständiges Journal (Workbook) als
zweites Amazon-Produkt — Querverweis im Hauptbuch, eigenes KDP-Listing.

| Journal (zu) | Seiten | Manuskript | Cover Full-Wrap | Klappentext |
|---|---|---|---|---|
| Das schlechte Gewissen | 42 | outputs/buch-schuldgefuehle/das-schlechte-gewissen-Journal.pdf(+.docx) | outputs/buch-schuldgefuehle/journal-Cover-Print-FullWrap.pdf | outputs/buch-schuldgefuehle/journal-klappentext.md |
| Wenn Beziehungen erschöpfen | 44 | outputs/buch-beziehungen/wenn-beziehungen-erschoepfen-Journal.pdf | outputs/buch-beziehungen/journal-Cover-Print-FullWrap.pdf | outputs/buch-beziehungen/journal-klappentext.md |
| Ich bin so müde... | 38 | outputs/buch6/ich-bin-so-muede-Journal.pdf | outputs/buch6/journal-Cover-Print-FullWrap.pdf | outputs/buch6/journal-klappentext.md |

**Aufbau je Journal:** Titelseite (Cover-Bild als Hintergrund), pro Kapitel
kurze Einordnung + Reflexionsfragen mit Schreiblinien + kleine Übung +
Checkliste + 3-Schritte-Prozess + Vorher/Nachher-Tabelle, dazwischen
Zitat-Trennseiten (Foto-Hintergrund geblurrt), Impressum am Ende.

**Reusable Baumuster (gilt für jedes künftige Journal):**
- Trimgrösse, Ränder, Fonts identisch zum Hauptbuch (5.5×8.5in, Liberation
  Serif eingebettet)
- Bild-Hintergründe (Titelseite, Zitatseiten) NUR als JPEG einbetten
  (`quality=85`), nie PNG — PNG treibt die Dateigrösse auf mehrere MB hoch
  und macht die KDP-Vorschau extrem langsam. Zielgrösse < 1MB gesamt.
- Bilder in Frames NIE randlos/bleed zeichnen — nur innerhalb derselben
  Ränder wie der Fliesstext platzieren. Ein randloses Vollbild (auch mit
  Farbfüllung dahinter) löst "Bild befindet sich außerhalb der Ränder" aus.
- Jede Frage + ihre Schreiblinien in `KeepTogether([...])` verpacken (aus
  `reportlab.platypus`) — verhindert, dass die Frage auf der letzten Zeile
  einer Seite landet und die Striche erst auf der nächsten. Regel gilt für
  jeden Frage-Block, jede Übung, jede Standortbestimmung.
- Zwischen normalem Kapitelinhalt und einer Zitat-Trennseite NIE zwei
  `PageBreak()` hintereinander — erzeugt eine leere Seite. `NextPageTemplate`
  direkt vor den einen nötigen `PageBreak()` setzen, danach jedes Dokument
  mit `fitz` (PyMuPDF) auf leere Seiten prüfen.
- Impressum/Legal-Block kompakt halten (spaceAfter/spaceBefore klein setzen),
  damit kein einzelner Satz ("Selbstverlag über Amazon KDP") als Waise auf
  einer eigenen Schlussseite landet.
- Rücken-Formel (Weisspapier) je nach finaler Seitenzahl neu berechnen:
  `SPINE_IN = SEITEN * 0.002252`. Nach jeder inhaltlichen Änderung, die die
  Seitenzahl verschiebt, Full-Wrap-Cover neu bauen.
- Nach jedem Build: `python3 tools/buch-pruefen.py <docx> <pdf>` UND das PDF
  visuell mit `fitz`-Rendering prüfen (leere Seiten, Ränder, Seitenumbrüche).

**Master-Skripte (Scratchpad, bei Bedarf neu ausführen mit angepasster
PAGES-Konstante):** `journal_pdf_full.py` / `journal2_pdf_full.py` /
`journal3_pdf_full.py` (Inhalt) und `journal_fullwrap.py` /
`journal2_fullwrap.py` / `journal3_fullwrap.py` (Cover) — je einer pro Buch,
liegen im Session-Scratchpad, nicht im Repo. Bei künftigen Journalen dieses
Muster kopieren statt neu erfinden.
