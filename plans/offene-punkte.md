# Offene Punkte

Hier landen alle laufenden ToDos. Claude pflegt diese Datei beim `/shutdown` automatisch — erledigte Punkte raus, neue rein.

## Erinnerung: Metricool einrichten (ca. 3. August 2026)

Petra will Metricool (automatisches Posten TikTok + Instagram) erst einrichten,
nachdem sie gesehen hat, wie die ersten Bilder/Karussells aus dem
Kupka-System (`context/tiktok-karussell-system.md`) aussehen. Automatische
Erinnerung nach 1 Woche ist technisch fehlgeschlagen (Berechtigungsfehler
beim send_later-Tool) — bei nächster Gelegenheit erneut versuchen oder
Petra beim nächsten Gespräch aktiv daran erinnern.

## Buch 6 (Ich bin so müde. Und niemand fragt mich warum): kurz vor dem Upload

**Stand 26. Juli 2026.** Manuskript und Cover sind fertig. Bereit für den Upload.

### Was fertig ist

- 111 Seiten, 19 Kapitel, 5 Schritte. Kapitel/Trennseiten beginnen jetzt
  bewusst auf der gleichen Höhe wie normale Fliesstext-Seiten (keine 1,9 cm
  Einrückung mehr — auf Petras Wunsch geändert, weicht von der ursprünglichen
  Regel in context/buch-standard.md ab)
- Alleinstellungsmerkmal drin: Selbsttest vorne, Notfall-Seiten vorne, Satz-Sammlung hinten
- Claudia zieht sich als roter Faden durch fünf Stellen
- 21 TikTok-Zeilen in grauen Kästen
- Impressum vollständig, mit Anschrift Wiesentalstrasse 68, 9240 Uzwil
- Geprüft: kein ß, keine Gedankenstriche, Anführungszeichen paarig, keine leeren
  Seiten, keine verwaisten Zwischentitel, alle Krisennummern, Inhaltsverzeichnis
  vollständig

Dateien: `outputs/buch6/buch6-MANUSKRIPT.docx` und `buch6-Taschenbuch.pdf`
Skripte: `tools/buch6-word2pdf.py` und `tools/buch6-cover.py`

### Cover: fertig (Stand Abend 26. Juli 2026, finale Entscheidung)

`outputs/buch6/buch6-Cover-FullWrap.pdf`, 292,85 × 222,30 mm, Rücken 7,05 mm
(111 Seiten, seit der Korrektur der Absatz- und Kapitelabstände weniger als zuvor).

Finales Motiv: Kintsugi-Riss mit Foto einer Frau, die sich erschöpft den Kopf
hält (schwarzer Blazer). Quelle `cover-entwuerfe/cover-front-kintsugi-frau-hires.png`,
Originalauflösung 2100×3267 px (nicht hochskaliert) → 373 dpi. Störer-Kreis
unten links direkt ins Bild eingebaut, Text korrigiert auf „MIT SELBSTTEST UND
DEN SÄTZEN FÜR 9 KONKRETE SITUATIONEN" (nicht „DIE DU WIRKLICH SAGST").

Geprüft: 373 dpi, alle Schriften eingebettet, kein „bluewin", Gesamtmass exakt.
Verworfene Varianten (Marmor ohne Gesicht, Ganzkörperfoto bei 187 dpi, Träne,
graues T-Shirt/rote Schrift) liegen zur Referenz noch in `cover-entwuerfe/`.

Neu erzeugen, falls nötig:
```bash
python3 tools/buch6-cover.py outputs/buch6/cover-entwuerfe/cover-front-kintsugi-frau-hires.png
```

**Achtung:** Druckausführung ist **Matt**, nicht Glanz (Serienkonsistenz mit
Petras drei anderen Büchern) — siehe KDP-Upload-Anleitung.md Schritt 6.

### eBook: fertig

`outputs/buch6/buch6-eBook.epub` + `outputs/buch6/buch6-eBook-Cover.png`
(2042×3267 px, Verhältnis 1,6:1, nur Vorderseite ohne Rücken/Rückseite).

Gebaut direkt aus der massgeblichen `buch6-MANUSKRIPT.docx` (nicht aus der
älteren `.md`-Datei), mit anklickbarer Navigation statt Seitenzahlen-TOC.
Geprüft: keine private Mailadresse, keine „Heilerin", Kontaktadresse korrekt,
Krisennummer bei ca. 9 % der Textlänge.

Neu erzeugen:
```bash
python3 tools/buch6-ebook.py
```

Upload-Schritte stehen in `KDP-Upload-Anleitung.md`, Schritt 9.

### Danach: KDP-Upload

**Vollständige Anleitung liegt in `outputs/buch6/KDP-Upload-Anleitung.md`.**
Titel, Untertitel, Beschreibung, drei Kategorien, die sieben Keywords,
alle Druckeinstellungen und der Preis stehen dort fertig zum Kopieren.

Kurzfassung der Eckdaten:

- 111 Seiten, 5,5 x 8,5 Zoll, Papier Creme, kein Bleed, Cover Matt
- Listenpreis 12,99 EUR, Tantieme ca. 5,17 EUR
- Kostenlose KDP-ISBN, Expanded Distribution aus
- Nach dem Upload 72 Stunden Indexierung abwarten
- Primärer Marketplace muss Amazon.de sein, nicht Amazon.com
- Kategorien: KDP hat einen eigenen Baum, kein „Ratgeber". Richtig ist
  `Bücher > Selbsthilfe` mit Stress & Stressbewältigung, Emotionen, Selbstachtung

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

Bei Buch 6 haben wir drei Dinge festgelegt, die den anderen Büchern noch fehlen.
Alles lässt sich bei KDP jederzeit nachträglich ändern, Titel und Untertitel bleiben unangetastet.

### 0. Rechtssicherheit nachziehen (zuerst, weil es das Risiko ist)

`context/rechtssicherheit.md` gilt rückwirkend. In Buch 3, 4 und 5 prüfen und korrigieren:

- Steht irgendwo „Therapeutin" über Petra? Ersetzen durch „Coachin"
- Sagt ein Satz der Leserin, was sie hat oder nicht hat? Umformulieren auf
  „Es fühlt sich an wie … Ich nenne es …"
- Selbsttests ohne Einordnung? Absatz „kein Test im medizinischen Sinn" davorsetzen
- Krisennummern nur im Rechtlichen? Zusätzlich ins vordere Drittel
- Fehlt der Abschnitt „Zur Autorin" im Rechtlichen? Ergänzen


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
