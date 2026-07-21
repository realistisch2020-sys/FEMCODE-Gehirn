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

- Öffentlich / im Buch: **beyondlimitsnow25@gmail.com**
- Privat / NIEMALS im Buch: tanner.pe@bluewin.ch

---

## Fertige Bücher

| Buch | Titel | Seiten | Spine | Manuskript-PDF | Cover-PDF | KDP-Status |
|---|---|---|---|---|---|---|
| Buch 3 | Wenn Beziehungen erschöpfen | 123 | 83px | outputs/buch-beziehungen/…-Taschenbuch.pdf | outputs/buch-beziehungen/…-FullWrap.pdf | In Vorbereitung |
| Buch 4 | Das schlechte Gewissen | 72 | 49px | outputs/buch-schuldgefuehle/…-Taschenbuch.pdf | outputs/buch-schuldgefuehle/…-FullWrap.pdf | In Vorbereitung |
| Buch 5 | Niemand hat dich gefragt, wie es dir geht | 61 | 41px | outputs/buch-niemand-gefragt/niemand-hat-dich-gefragt-Taschenbuch.pdf | — | Cover ausstehend |
