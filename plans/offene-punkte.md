# Offene Punkte

Hier landen alle laufenden ToDos. Claude pflegt diese Datei beim `/shutdown` automatisch — erledigte Punkte raus, neue rein.

## Buch 6 (Ich bin so müde. Und niemand fragt mich warum): kurz vor dem Upload

**Stand 25. Juli 2026.** Manuskript ist fertig und geprüft. Es fehlt nur das Cover.

### Was fertig ist

- 125 Seiten, 19 Kapitel, 5 Schritte
- Alleinstellungsmerkmal drin: Selbsttest vorne, Notfall-Seiten vorne, Satz-Sammlung hinten
- Claudia zieht sich als roter Faden durch fünf Stellen
- 21 TikTok-Zeilen in grauen Kästen
- Impressum vollständig, mit Anschrift Wiesentalstrasse 68, 9240 Uzwil
- Geprüft: kein ß, keine Gedankenstriche, Anführungszeichen paarig, keine leeren
  Seiten, keine verwaisten Zwischentitel, alle Krisennummern, Inhaltsverzeichnis
  vollständig

Dateien: `outputs/buch6/buch6-MANUSKRIPT.docx` und `buch6-Taschenbuch.pdf`
Skripte: `tools/buch6-word2pdf.py` und `tools/buch6-cover.py`

### Der einzige Blocker: die Cover-Datei

Petra erzeugt das Cover mit ChatGPT. Zwei Dinge fehlen noch:

1. **Rosé aufhellen.** Die Zeilen „UND NIEMAND FRAGT MICH WARUM" stehen aktuell
   auf `#AA6E5A`, das ergibt nur 5,1 zu 1 Kontrast. Die Creme-Zeilen darüber haben
   14 zu 1. Zielfarbe `#E8B49B`, das ergibt 11,4 zu 1. Im Druck und im Thumbnail
   fällt der schwache Kontrast sonst auseinander.

2. **Seitenverhältnis 0,7 zu 1**, zum Beispiel 2100 × 3000 Pixel. Die bisherige
   Datei ist 2:3, dabei würden oben und unten je 5 mm abgeschnitten, und unten
   steht „SAFE TO THRIVE".

Aktueller Entwurf liegt in `outputs/buch6/cover-entwuerfe/cover-v3-dunkles-rose.png`.

Sobald die Datei da ist:
```bash
python3 tools/buch6-cover.py pfad/zur/datei.png
```

### Danach: KDP-Upload

Noch nicht gemacht, muss vorbereitet werden:

- Titel: `Ich bin so müde. Und niemand fragt mich warum`
- Untertitel: `Das Funktions-Ich: Wenn du für alle stark bist und dich dabei verlierst`
  (Wort für Wort wie auf dem Cover, Amazon gleicht das ab. Nach dem Upload für immer fix.)
- Seitenzahl 125, Papier Creme, Format A5
- **Die sieben Keywords fehlen noch.** Petra hat ausdrücklich die bestmöglichen
  verlangt, nicht nur plausible. Muss noch recherchiert werden.
  Erste Kandidaten: Mental Load Mutter, erschöpfte Frauen keine Kraft,
  Nein sagen lernen Frauen, Grenzen setzen Buch Frauen, immer für alle da sein,
  emotionale Erschöpfung Alltag, Selbstfürsorge für Frauen Buch
- Produktbeschreibung fehlt noch
- Kategorien fehlen noch

### Reihenfolge beim Start, so besprochen

1. Cover fertig, Druckbogen bauen
2. KDP-Upload und veröffentlichen
3. Drei Tage Indexierung abwarten
4. Fünf bis zehn Bewertungen sammeln, verteilt über zwei bis drei Wochen
5. Ab erster Bewertung Amazon Ads, klein anfangen
6. Ab etwa fünf Bewertungen erst TikTok mit dem Buch

Niemals umgekehrt. Ein viraler Clip auf ein Buch ohne Bewertungen verbrennt den
Traffic, und der kommt nicht wieder.

## Social Media: neue Konten aufbauen

Petra fängt auf TikTok und Instagram neu an, entschieden am 25. Juli 2026.

**Warum:** Das bestehende Konto `petra.safetothrive` ist ein MONAT-Konto.
MONAT steht im Namensfeld, in der Bio, in den Highlights („Bestelle hier", „Ränge")
und in etwa der Hälfte der Beiträge. Auf TikTok gibt es nur das MONAT-Konto.

Zwei Gründe: Der Algorithmus hat gelernt, dass es um Haare und Vertriebseinstieg
geht, Buchinhalte werden also den Falschen gezeigt. Und eine erschöpfte Leserin,
die dort landet, trifft auf eine Verkaufsabsicht, genau das, wovon das Buch sie
befreien will.

Beleg für das Problem: 5'819 Aufrufe in 30 Tagen bei 3'379 Followern. Das ist wenig.

### Zu tun

- Neues Konto auf **beiden** Plattformen, gleicher Name. Vorschlag `petra.tanner.autorin`,
  Verfügbarkeit auf TikTok und Instagram gleichzeitig prüfen
- Bio: `Naturheilpraktikerin, 26 Jahre Praxis` / `Für Frauen, die für alle stark sind.
  Nur nicht für sich.` / `Autorin von „Ich bin so müde. Und niemand fragt mich warum"`
- Namensfeld mit Suchwörtern, nicht nur der Name. Instagram durchsucht das Namensfeld mit.
- Sofort täglich posten, **ohne das Buch zu erwähnen**. Material sind die
  21 TikTok-Zeilen aus dem Buch. Der Kanal muss lernen, wofür er steht, bevor
  das Buch kommt.
- MONAT-Konto bereinigen: „Safe to Thrive", „Naturheilpraktikerin" und „Coach"
  raus, dafür eine Zeile `Meine Bücher: @petra.tanner.autorin`. Die Richtung bleibt
  einseitig, auf dem Autorinnenkonto steht kein Hinweis auf MONAT.
- Einmaliger Übergabebeitrag auf dem MONAT-Konto

## Rückwirkende Angleichung der älteren Bücher (nach Buch 6, ab August 2026)

Bei Buch 6 haben wir zwei Dinge festgelegt, die den anderen Büchern noch fehlen.
Beides lässt sich bei KDP jederzeit nachträglich ändern, Titel und Untertitel bleiben unangetastet.

### 1. Impressum: ladungsfähige Anschrift ergänzen

In Buch 3, 4 und 5 steht nur „Safe to Thrive, Schweiz" plus E-Mail. Keine Adresse.
Die deutschen Landespressegesetze verlangen bei gedruckten Werken Name und Anschrift
des Verlegers, bei Selfpublishing also Petra selbst.

Neuer Block, wie in Buch 6:

```
© 2026 Petra Tanner
Alle Rechte vorbehalten.

Petra Tanner
Wiesentalstrasse 68
9240 Uzwil, Schweiz

Selbstverlag
Unabhängig veröffentlicht über Amazon Kindle Direct Publishing

Kontakt: beyondlimitsnow25@gmail.com
```

Betrifft:
- `outputs/buch-beziehungen/` (Wenn Beziehungen erschöpfen)
- `outputs/buch-schuldgefuehle/` (Das schlechte Gewissen)
- `outputs/buch-niemand-gefragt/` (Niemand hat dich gefragt, wie es dir geht)

Achtung: Das Impressum steht im Buchblock. Änderung heisst neues Manuskript-PDF
hochladen. Seitenzahl prüfen, danach stimmt eventuell die Rückenbreite nicht mehr
und das Cover muss neu gerechnet werden.

### 2. Cover auf die Bildsprache von Buch 6 umstellen

Die drei alten Cover sind elegant, aber im Amazon-Thumbnail bei 160 Pixel Breite
kaum lesbar. Für TikTok, wo das Buch fingernagelgross am Clipende erscheint,
erst recht nicht.

Buch 6 löst das: grosse fette Groteske, hoher Kontrast, ein Gesicht, Kintsugi-Gold.

Was von der alten Reihe erhalten bleiben muss:
- Autorinnenblock unten mittig, zweizeilig: PETRA TANNER über SAFE TO THRIVE,
  gesperrt, mit feinem goldenem Trenner
- Gold als Akzentfarbe
- Der Konzeptbegriff in goldener Serifenschrift

Reihenfolge: erst schauen, ob Buch 6 läuft. Wenn ja, die anderen nachziehen.
Nicht umgekehrt, und nicht bevor Buch 6 draussen ist.

## Buch 4 (Das schlechte Gewissen): Taschenbuch Cover neu einreichen

- Cover wurde von KDP abgelehnt: Spine-Text zu nah an Rändern + unter 79 Seiten (kein Spine-Text erlaubt)
- ✅ Fix: Spine leer, SAFE=0.5", ReportLab PDF neu generiert
- **Jetzt:** Neues Cover PDF bei KDP hochladen → `outputs/buch-schuldgefuehle/das-schlechte-gewissen-Cover-Print-FullWrap.pdf`
- Nach Freigabe: Taschenbuch-Link prüfen, Instagram Post

## Buch 3 (Wenn Beziehungen erschöpfen): Taschenbuch Upload ausstehend

- Manuskript PDF: `outputs/buch-beziehungen/wenn-beziehungen-erschoepfen-Taschenbuch.pdf` (123 Seiten)
- Cover Full-Wrap PDF: `outputs/buch-beziehungen/wenn-beziehungen-erschoepfen-Cover-Print-FullWrap.pdf`
- Spine: 83px (123 Seiten × 0.002252 × 300) — Spine-Text erlaubt (>79 Seiten)
- Empfohlener Preis: $13.99
- KDP Print: Neues Taschenbuch-Projekt anlegen

## Buch 5 (Niemand hat dich gefragt, wie es dir geht): Cover fertigstellen

- Manuskript PDF: `outputs/buch-niemand-gefragt/niemand-hat-dich-gefragt-Taschenbuch.pdf` (61 Seiten)
- Vordercover PNG erstellt: `outputs/buch-niemand-gefragt/cover-niemand-FRONT.png` (Petrol & Gold, abstraktes Bild)
- **Offen:** Manuskript überarbeiten — KI-typische Stellen raus (Kap. 11, 14 zu dünn, "Ich möchte dir sagen" zu oft)
- **Offen:** Full-Wrap Cover (Rückseite + Spine) generieren → dann KDP Upload
- Spine: 41px (61 Seiten) — KEIN Spine-Text (unter 79 Seiten)
- Empfohlener Preis: $12.99

## Buch 1 (ADHD Planner): Cover-Anzeige prüfen

- Cover auf KDP hochgeladen — auf Amazon.de noch nicht aktualisiert
- Sobald live: Facebook + Instagram Post mit Link amazon.de/dp/B0H9B3XZF8
- KI-Angabe in KDP auf "Ja" korrigieren

## Nach Veröffentlichung (alle Bücher)

- Instagram Story + Feed-Post pro Buch
- Erste Bewertungen organisieren
- Homepage / Landingpage für Safe to Thrive erstellen (aktuell keine vorhanden)
- Newsletter aufbauen

## TikTok-Automation-Workflow aufbauen

- Vollautomatischer Content-Workflow nach Kupka-System (jeden Montag 08:00 Uhr)
- Schritte: Online-Recherche → Content-Plan → Ideogram-Prompts → Bilder + Text-Overlay → Google Drive
- Ergebnis: 7-10 fertige Clips / 70-100 Bilder + Captions + Hashtags pro Woche
- Kosten: ca. 3€/Woche
- **Einmalig aufbauen — dann läuft es selbst**
- Tools: KI (Claude) + Ideogram + automatisches Text-Overlay + Google Drive

## Ideen / später

- Instagram-Content zu Buch 3, 4, 5 planen
- eBook für Buch 5 erstellen (nach Taschenbuch)
- Aktionspreise: nur über eBook möglich (Kindle Countdown Deal, KDP Select)
