# Offene Punkte

Hier landen alle laufenden ToDos. Claude pflegt diese Datei beim `/shutdown` automatisch — erledigte Punkte raus, neue rein.

## Katalog-Qualitätsprüfung abgeschlossen, KDP-Re-Upload für alle 7 Bücher nötig (Stand 14. Oktober 2026)

Alle Hauptbücher wurden von je zwei unabhängigen Lektorinnen auf Wiederholung/
generischen Füllstoff geprüft (Ziel: "ein spannendes Buch mit Mehrwert") und
wo nötig chirurgisch gestrafft. Alle Taschenbuch-PDFs und eBooks sind neu
gebaut, `buch-pruefen.py` lief überall sauber (keine neuen Befunde), Seiten
visuell geprüft. Details je Commit in der Git-Historie.

**Wichtiger Technik-Fund dabei:** `tools/manuskript-word2pdf.py` und
`tools/manuskript-ebook.py` lasen bisher nur Fliesstext-Absätze, Inhalt in
Word-Tabellen (Zitat-/Reflexionsboxen) fiel lautlos weg. Betraf "Wenn
Beziehungen erschöpfen" (54 Tabellen, u.a. eine ganze Antwort in Kapitel 1
fehlte) und "Das schlechte Gewissen" (2 Tabellen, u.a. ein Satz aus "Zur
Autorin"). Beide Tools jetzt gefixt, beide Bücher neu gebaut und geprüft.

**Seitenzahlen, alt → neu:**
- Das schlechte Gewissen: 106 → 106 (Tabellen-Fix gleicht Kürzung aus)
- Wenn Beziehungen erschöpfen: 153 → **169** (grösstenteils wiederhergestellter Tabelleninhalt)
- Ich bin so müde...: 113 → 113
- Deine Reaktion gehört dir. Nicht mir.: 102 → 101
- Ich stand nie auf meiner eigenen Liste: 121 → 120
- Meine Lust ist nicht weg...: 123 → 115
- Du brauchst kein letztes Gespräch: 110 → 99 (schon letzte Session erledigt, siehe unten)

**Offen — Cover-Neubau nötig, weil sich die Seitenzahl/Rückenbreite geändert hat:**
- "Wenn Beziehungen erschöpfen" (deutlichste Änderung, +16 Seiten) und "Das
  schlechte Gewissen": **kein Build-Skript in `tools/` gefunden**, die
  Cover sind offenbar früher manuell/ad-hoc gebaut worden. Für einen
  Neubau müsste zuerst geklärt werden, wie das Cover ursprünglich
  entstand, oder ein neues Skript nach dem Muster der neueren Bücher
  gebaut werden.
- "Ich stand nie auf meiner eigenen Liste" (121→120) und "Meine Lust ist
  nicht weg..." (123→115): Build-Skripte vorhanden
  (`/tmp/.../buch4_newcover2.py` bzw. `tools/buch7-cover-foto.py`,
  `PAGES`/`SEITEN`-Konstante anpassen und neu bauen).
- "Deine Reaktion gehört dir" (102→101) und "Ich bin so müde..." (113→113,
  unverändert): Rückenbreite praktisch gleich, Cover-Neubau nicht dringend.

**Danach für ALLE 7 Bücher:** Taschenbuch-PDF, eBook und (wo neu gebaut)
Cover bei KDP neu hochladen.

## "Seit 26 Jahren in eigener Praxis" auf Buch-Rückseiten — Textfix erledigt, Cover-PDFs noch nicht neu gebaut

Siehe Abschnitt weiter unten für den Hintergrund. Quelltext in
`tools/buch6-cover.py`, `tools/buch7-cover-foto.py` und
`tools/buch-letztes-gespraech-cover.py` (unbenutzte Zweitfassung) korrigiert
zu "Petra Tanner, Coachin. Safe to Thrive, Schweiz." — die eigentlichen
Cover-PDFs für Buch 6 ("Ich bin so müde") und Buch 7 sind noch **nicht**
neu gebaut (richtiges Vorderseitenbild pro Buch erst klären). Für
"Du brauchst kein letztes Gespräch" ist das bereits erledigt (Commit
631879f). `buch5-cover.py` war bereits korrekt.

## DRINGEND: "Naturheilpraktikerin"/"eigener Praxis" auf mehreren Buch-Rückseiten (seit 13. Okt. 2026)

Eine 2/5-Rezenzo-Rezension zu "Du brauchst kein letztes Gespräch" führte zu
einer Volllektorats-Prüfung des Manuskripts (siehe unten) — dabei beim
Cover-Neubau entdeckt: Die Rückseite trug die Zeile **"Seit 26 Jahren in
eigener Praxis."** Das verstösst gegen `rechtssicherheit.md` Regel 1
("Niemals ... Naturheilpraktikerin" — genau dieser Begriff steht auch als
früherer Bio-Vorschlag weiter unten in dieser Datei, Abschnitt Social
Media/`petra.tanner.autorin`: "Naturheilpraktikerin, 26 Jahre Praxis").
`buch-pruefen.py` prüft nur Manuskript + Taschenbuch-PDF, nicht den
Cover-Text — darum ist das nie aufgefallen (derselbe Fehlerkanal wie bei
Buch 3 mit "Therapeutin" auf dem Cover, siehe `rechtssicherheit.md` §9).

**Korrigiert (Quelltext UND Cover-PDF neu gebaut):**
`tools/buch-letztes-gespraech-cover-foto.py` → "Petra Tanner, Coachin.
Safe to Thrive, Schweiz.", Cover neu gebaut (Commit 631879f), noch
**nicht bei KDP neu hochgeladen**.

**Korrigiert (nur Quelltext, Cover-PDF noch NICHT neu gebaut — richtiges
Vorderseitenbild pro Buch zuerst klären):**
- `tools/buch6-cover.py` (Buch "Ich bin so müde...", 113 Seiten passt noch)
- `tools/buch7-cover-foto.py` (Buch 7 "Meine Lust ist nicht weg...", Skript
  hat 130 als Platzhalter-Seitenzahl, tatsächlich aktuell 123 Seiten —
  beim Neubau `python3 tools/buch7-cover-foto.py <bild> 123` mit der
  echten Seitenzahl aufrufen)
- `tools/buch-letztes-gespraech-cover.py` (alte typografische Zweitfassung,
  wird aktuell nicht verwendet — die Foto-Fassung oben ist die aktive)

**Bereits geprüft und sauber, keine Änderung nötig:** `tools/buch5-cover.py`
(steht dort schon "Safe to Thrive.", keine "eigener Praxis"-Zeile).

Sobald die Cover-PDFs für Buch 6 und Buch 7 neu gebaut sind: Petra
informieren, dass sie die korrigierten Cover bei KDP erneut hochladen
muss (betrifft mehrere bereits live/gedruckte Bücher).

## Buch 6: "Du brauchst kein letztes Gespräch" — Inhalt gekürzt, Cover-Re-Upload nötig (Stand 13. Oktober 2026)

**13. Oktober 2026:** 2/5-Rezenzo-Rezension ("ständige Wiederholungen, zu
allgemein") führte zu einer Doppel-Lektoratsprüfung. Ergebnis: teilweise
berechtigt. Korrigiert: Dopplung Verzeihen/Vergessen aufgelöst (Kapitel 10
behalten, Dopplung gestrichen, stärkste Einsicht integriert), 4 der
formelhaften "Wenn..."-Abschnitte ab Kapitel 8 gestrichen (Geschwister zu
Fremden, einseitige Freundschaft, Feiertage, Selbstvertrauen aufbauen),
Übungsformulierungen in 5 verbleibenden Abschnitten variiert, doppelte
FAQ-Frage zusammengeführt. Seitenzahl **110 → 99**. `buch-pruefen.py` und
visuelle PDF-Prüfung sauber. Commits 888b5d0 (Manuskript/PDF/eBook) und
631879f (Cover, inkl. Rechtssicherheits-Fix oben), beide gepusht.

**Offen:** Taschenbuch-PDF, eBook und Cover bei KDP neu hochladen
(Seitenzahl und Rückenbreite haben sich geändert, Cover-Text korrigiert).

## Buch 6: "Du brauchst kein letztes Gespräch" — komplett hochgeladen (Stand 18. September 2026)

**Von Petra bestätigt: Taschenbuch, eBook und Journal sind alle bei KDP
hochgeladen.** Bonus-PDF fertig, Tentary-QR-Code im Buch eingebaut. Alle
Dateien in `outputs/buch-letztes-gespraech/`.

**Nächste Schritte (Standardablauf, noch nicht begonnen):** A+ Content
bauen, fünf bis zehn Bewertungen sammeln (verteilt über zwei bis drei
Wochen), erst danach TikTok/Social zu diesem Buch.

**Journal mit Cover-Fehler, gelöst:** Das Journal hatte ursprünglich nur
20 Seiten, unter KDPs Mindestanforderung von 24 für Taschenbücher — auf
26 Seiten erweitert (neuer Abschnitt "Eigene Notizen" mit Schreiblinien).
Danach kam beim Cover-Upload trotzdem wiederholt "Fehler beim
Verarbeiten des Covers", auch nachdem die Datei technisch dreifach
gehärtet wurde (Font-Einbettung, exaktes Beschnittmass, zuletzt als
reines Rasterbild ohne Schriftarten/Vektoren). Die Datei bestand jede
externe Prüfung (qpdf, Ghostscript) und alle Petras KDP-Einstellungen
waren korrekt. **Was tatsächlich geholfen hat: den Cover-Upload im
bestehenden, bereits mehrfach fehlgeschlagenen Entwurf löschen und
frisch hochladen** — der Entwurf selbst hatte sich festgefahren, nicht
die Datei. Lehre für künftige Bücher in `context/kdp-buch-produktion.md`
gespeichert.

**Wichtig für alle künftigen Bücher (Petras Regel vom 18. September
2026):** Jedes Buch bekommt denselben vollständigen Ablauf — Taschenbuch,
eBook, Journal, Bonus-PDF, siehe `context/strategie.md`.

## KDP-Upload ausstehend (Stand 14. September 2026)

"Wenn Beziehungen erschöpfen" und "Ich bin so müde..." sind mit
Bonusseite/QR-Code aktualisiert und fertig, laut Erinnerung vom 13.9.
aber noch nicht neu bei KDP hochgeladen.

## Stand 30. Juli 2026: 3 Bücher + 3 Journale fertig

Alle drei Hauptbücher (Das schlechte Gewissen, Wenn Beziehungen erschöpfen,
Ich bin so müde...) haben jetzt je ein eigenständiges Journal/Workbook als
zweites KDP-Produkt, siehe `context/kdp-buch-produktion.md` Abschnitt
„Journal-Serie". Alle drei sind mehrfach durch KDP-Fehlerkorrekturen (Cover-
Grösse, Bild-außerhalb-Ränder, Font-Einbettung, leere Seiten, Waisen-Zeile,
Dateigrösse) gelaufen und laut Petra erfolgreich hochgeladen.

**Noch zu prüfen, falls nicht schon geschehen:** Querverweis auf das Journal
im jeweiligen Hauptbuch-Manuskript (Backmatter) — wurde für alle drei
eingebaut, bei nächster Buch-Überarbeitung gegenprüfen.

**Offen:** Amazon-Ads-Kampagne für „Das schlechte Gewissen" — zwei Kampagnen
liefen zuletzt (automatisch + manuell), beide sichtbar. Keine akuten Probleme
mehr bekannt, aber nicht aktiv weiterverfolgt diese Session.

## Erinnerung: Gumroad

Petra wollte an Gumroad (Direktverkauf-Plattform, Alternative/Ergänzung zu
Amazon KDP mit höherer Marge, z. B. für die Journale als PDF-Download ohne
Print) erinnert werden. Kein funktionierender Reminder-Mechanismus vorhanden
(send_later schlug mit Berechtigungsfehler fehl) — beim nächsten Gespräch
aktiv ansprechen.

## Erinnerung: Metricool einrichten (ca. 3. August 2026)

Petra will Metricool (automatisches Posten TikTok + Instagram) erst einrichten,
nachdem sie gesehen hat, wie die ersten Bilder/Karussells aus dem
Kupka-System (`context/tiktok-karussell-system.md`) aussehen. Automatische
Erinnerung nach 1 Woche ist technisch fehlgeschlagen (Berechtigungsfehler
beim send_later-Tool) — bei nächster Gelegenheit erneut versuchen oder
Petra beim nächsten Gespräch aktiv daran erinnern.

## Carousel Slide 1-7 fuer Buch 6 in Canva fertigstellen (TikTok/Instagram)

Erstes Carousel steht inhaltlich fest (siehe `context/tiktok-carousel-prozess.md`,
8 Slides zum Thema "Das Funktions-Ich verstehen"). Zwei Bild-Favoriten fuer
Slide 1 sind bereits als editierbare Canva-Designs erzeugt:
- Favorit 2: https://www.canva.com/d/pkTQv2NsxbqYEts
- Favorit 4: https://www.canva.com/d/c8Ki8E39cTDD9hV

**Offen:** Headline-Text bei beiden einfuegen ("Du bist nicht faul. Du bist
erschöpft von etwas, das niemand sieht."), Petra entscheidet sich fuer einen,
dann Slides 2-7 nach demselben Muster bauen (Bildgenerierung via Canva +
Textoverlay). Die Bildgenerator-Prompts fuer alle 8 Slides liegen im Chat-
Verlauf vom 27. Juli 2026 bereit.

**Blockiert aktuell an:** Das Canva-`edit-design`-Werkzeug (Text/Formen
einfuegen) schlaegt wiederholt mit "MCP tool call requires approval" fehl,
auch nach Freigabe durch Petra. `generate-design` und `create-design-from-
candidate` funktionieren dagegen. Sobald das Editieren wieder geht: Petra hat
ausdruecklich gesagt, ich soll die restlichen Slides selbststaendig fertig
bauen, ohne nochmal nachzufragen.

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

### Buch 3 und Buch 4: erledigt (Stand 28. Juli 2026)

Rechtssicherheit, Impressum-Adresse, Selbsttests, Cross-Promotion-Abschnitt
„Meine andere Bücher" und Cover-Grösse sind für Buch 3 und Buch 4 durch.
Im Detail:

- „Therapeutin" komplett raus (auch aus dem Buch-3-Cover, das war die letzte
  Fundstelle), überall „Coachin"
- Alte private E-Mail-Adresse überall ersetzt (auch auf dem Buch-3-Cover)
- Kompletter Pflichtteil (8 Teile aus `rechtssicherheit.md` §7) inkl. Adresse
  Wiesentalstrasse 68, 9240 Uzwil in beiden Büchern
- Checkbox-Selbsttest mit Einordnung in beiden Büchern
- Krisennummern vorne und hinten in beiden Büchern
- Abschnitt „Meine anderen Bücher" (Cross-Promotion) in Buch 3 ergänzt —
  bei Buch 4 und künftigen Büchern nachziehen
- „Literatur und Weiterführendes" aus Buch 3 entfernt (kein Pflichtteil)
- Cover-Grösse an aktuelle Seitenzahl angepasst: Buch 3 jetzt 148 Seiten,
  Cover 11.583×8.750in — **falls Petra das Cover schon bei KDP hochgeladen
  hatte, muss die neue Cover-PDF nochmal hochgeladen werden**

**Noch offen: Buch 5** (Niemand hat dich gefragt, wie es dir geht) — dieselbe
Prüfung/Korrektur fehlt noch komplett (siehe eigener Abschnitt unten).

### Technik-Lehren dieser Runde (schon in `context/buch-standard.md` §9 gespeichert)

Neue generische Skripte `tools/manuskript-word2pdf.py` und
`tools/manuskript-ebook.py` für Manuskripte ohne Word-Formatvorlagen (Buch 3,
4, vermutlich auch 5). Wichtigste Lehren: verzehnfachte Schriftgrössen
normalisieren, Inline-Seitenumbrüche zusätzlich zu `page_break_before`
prüfen, Inhaltsverzeichnis kompakt setzen, Absätze/Zwischentitel/Pointe-Sätze
nie über eine Seite reissen lassen, Cover-Rechtstext separat prüfen.

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

## Buch 4 (Das schlechte Gewissen): live, A+ Content eingereicht

Live auf Amazon, 106 Seiten, „Ein letztes Wort" (Bewertungs-Bitte) ergänzt.
A+ Content (Zitatkarte quer, Themen-Übersicht, Cross-Promotion) ist fertig
gebaut und am 1./2. August 2026 erfolgreich zur Prüfung eingereicht — Status
bei Petra prüfen (Genehmigung/Veröffentlicht).

## Buch 3 (Wenn Beziehungen erschöpfen): live, A+ Content hängt an KDP-Fehler

Live auf Amazon, 149 Seiten, „Ein letztes Wort" ergänzt. A+ Content-Bilder
sind fertig (`outputs/buch-beziehungen/zitatkarte-quer-*.png`,
`aplus-was-dich-erwartet.png`, `outputs/aplus-cross-promotion.png`), aber
das Speichern im KDP-Editor schlägt wiederholt fehl mit „Project could not
be deserialized (CatchAll)". Ausprobiert und nicht gelöst: leeres Modul
löschen, Modul-Layouts variieren (Petra hat das versucht, half nicht).

**Nächster Schritt:** frischer Browser/Inkognito-Modus, sonst KDP-Support
kontaktieren.

## Buch 5 ("Deine Reaktion gehört dir. Nicht mir.") — bereit zum KDP-Upload (Stand 30. Aug. 2026)

- Titel geändert von "Niemand hat dich gefragt, wie es dir geht" — der alte
  Ordner `outputs/buch-niemand-gefragt/` ist veraltet, nicht mehr verwenden.
- Alles Aktuelle liegt in `outputs/buch-reaktion/`, 102 Seiten:
  - `buch5-MANUSKRIPT.docx` — Quelle, gemeinsam für Taschenbuch und eBook
  - `buch5-Taschenbuch.pdf` — druckfertig, Rücken 6,48 mm
  - `buch5-eBook.epub`
  - `buch5-Cover-FullWrap.pdf` (Taschenbuch, Rücken auf 102 Seiten kalibriert)
    und `buch5-eBook-Cover.jpg` (Kindle) — Vorderseitenbild ist ein von Petra
    ausgewähltes Bild (Petrol/Gold-Riss-Motiv, 320 dpi, Quelle gesichert unter
    `buch5-cover-front-source.png`)
  - `buch5-Bonus-PDF.pdf` — Freebie in Petrol/Gold, sechs Übungen aus dem Buch
  - Kapitel "Vertiefende Übungen zu diesem Buch" mit QR-Code zu Tentary
    (Freebie + Newsletter) in Taschenbuch UND eBook eingebaut. Der Text-Link
    als Fallback steht nur im eBook, im Taschenbuch reicht der QR-Code
    (neuer "EBOOKONLY·"-Marker in `tools/manuskript-word2pdf.py` /
    `tools/manuskript-ebook.py`, analog zum TikTok-Marker)
  - Facebook-Gruppen-Link aus dem Kontakt-Abschnitt entfernt
  - `tools/buch-pruefen.py` sauber durchgelaufen (nur bekannte Heuristik-Treffer,
    keine echten Fehler): alle 8 Pflichtteile da, Krisennummern vorne
  - Build-Skripte: `tools/buch5-cover.py`, `tools/buch5-bonus-pdf.py`
    (SEITEN-Konstante bei künftiger Umfangsänderung anpassen)
- **Offen:** KDP-Upload (Taschenbuch + eBook), danach A+ Content — Petra will
  das am **Samstag, 5. September 2026** hochladen
- Empfohlener Preis: 12,99 € (Taschenbuch), 9,99 € (eBook)

## Buch 6 (Ich bin so müde...): A+ Content noch nicht begonnen

Manuskript und Cover live wie oben beschrieben. A+ Content (Zitatkarte,
Übersicht, Cross-Promotion) für dieses Buch wurde diese Session noch nicht
gebaut — nach Buch 3 und Buch 4 nachziehen, gleiches Muster (970×600px
Querformat, siehe `context/kdp-buch-produktion.md` Abschnitt „A+ Content —
Technik-Lehren").

## Buch 7 — jetzt „Ich stand nie auf meiner eigenen Liste" (Titel am 15. Aug. geändert): in Arbeit

- Hiess vorher „Ich habe nie gelernt, an mich zu denken" — Titel, Untertitel,
  Impressum/Markenrecht und Cover sind auf den neuen Titel umgestellt.
  Alte Bezeichnung nirgends mehr verwenden.
- Manuskript: `outputs/buch-an-mich-denken/buch4-MANUSKRIPT.docx` /
  `buch4-Taschenbuch.pdf`, aktuell 75 Seiten, Ziel ca. 100 Seiten — noch
  nicht erreicht, weitere Kapitel/Vertiefung nötig
- eBook (`buch4-eBook.epub`) ist inzwischen gebaut, ebenso ein eigenes
  eBook-Cover (`buch4-eBook-Cover.jpg`)
- Cover komplett neu (neues Bildmotiv: Kintsugi-Riss lila/gold, dunkler
  Hintergrund), Front + eBook-Cover + Vollwrap-PDF fertig, Spine auf 75
  Seiten kalibriert — **muss bei jeder weiteren Seitenzahl-Änderung neu
  gebaut werden** (`/tmp/.../scratchpad/buch4_newcover2.py`, `PAGES`-Konstante
  anpassen)
- Lektorat: KI-typisches Kontrastmuster („Das ist kein… Es ist…") teilweise
  variiert, absolute Aussagen zu Gehalt/Bindungsforschung/Wut abgeschwächt,
  gerade Anführungszeichen korrigiert, Sprache für gemischte Zielgruppe
  (Männer + Frauen) geöffnet
- Journal (`buch4-Journal-MANUSKRIPT.docx`) trägt noch den **alten** Titel —
  bei Gelegenheit auf „Ich stand nie auf meiner eigenen Liste" umstellen
- **Offen:** auf ~100 Seiten bringen, danach `buch-pruefen.py` laufen lassen,
  Journal-Titel/Cover nachziehen, A+ Content bauen, erst dann KDP-Upload —
  bewusst zurückgehalten, bis die vier laufenden Bücher sich stabilisieren
  (siehe Timing-Hinweis oben)

## Buch 1 (ADHD Planner): Cover-Anzeige prüfen

- Cover auf KDP hochgeladen — auf Amazon.de noch nicht aktualisiert
- Sobald live: Facebook + Instagram Post mit Link amazon.de/dp/B0H9B3XZF8
- KI-Angabe in KDP auf "Ja" korrigieren

## Nach Veröffentlichung (alle Bücher)

- Instagram Story + Feed-Post pro Buch
- Erste Bewertungen organisieren
- Homepage / Landingpage für Safe to Thrive erstellen (aktuell keine vorhanden)

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
- Journale auch als eigene eBooks/interaktive PDFs prüfen (siehe Gumroad-Idee oben)

## Nächster Buchtitel-Kandidat (Stand 5. August 2026)

„Ich fühle mich nicht richtig glücklich" — von Petra als möglicher weiterer
Titel genannt, noch nicht ausgearbeitet. Vor dem Start: Markt-Gegencheck wie
bei Buch 4 (Konkurrenz auf Amazon.de/.com, Content-Gap), dann erst
Manuskript-Konzept.
