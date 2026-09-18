# Buch 6 "Du brauchst kein letztes Gespräch" bei KDP hochladen, Schritt für Schritt

Stand 18. September 2026. Alles zum Abschreiben oder Kopieren.
Nichts davon muss noch entschieden werden.

---

## Schritt 0: Was du bereithalten musst

| | |
|---|---|
| Manuskript | `buch-Taschenbuch.pdf`, 110 Seiten |
| Cover | `buch-Cover-FullWrap-Foto.pdf`, 292,78 × 222,30 mm |
| Format | 5,5 x 8,5 Zoll (13,97 × 21,59 cm) |
| Papier | Creme |
| Rückenbreite | 6,99 mm |
| Covermass gesamt | 292,78 × 222,30 mm |

Das Manuskript ist geprüft: Schriften eingebettet, Seitenmass stimmt,
keine leere Seite, Krisennummern vorne, Inhaltsverzeichnis korrekt,
Bonus-QR-Code mit deinem Tentary-Link eingebaut (Seite 104).

Neu bauen lässt sich alles mit:

```bash
python3 tools/manuskript-word2pdf.py outputs/buch-letztes-gespraech/buch-MANUSKRIPT.docx outputs/buch-letztes-gespraech/buch-Taschenbuch.pdf
python3 tools/buch-letztes-gespraech-cover-foto.py outputs/buch-letztes-gespraech/cover-front-foto.png
```

---

## Schritt 1: Neuen Titel anlegen

1. kdp.amazon.com öffnen, einloggen
2. **Bookshelf** → **Create** → **Create Paperback**

Nicht „Create Kindle eBook". Das Taschenbuch kommt zuerst.

---

## Schritt 2: Paperback Details

**Language:** German

**Book Title:**
```
Du brauchst kein letztes Gespräch
```

**Subtitle:**
```
Wie du innerlich frei wirst, auch wenn die Entschuldigung nie kommt
```

> Beides muss **Wort für Wort** so auf dem Cover stehen. Amazon gleicht das ab.
> Nach der Veröffentlichung sind Titel und Untertitel für immer fix.

**Series:** leer lassen
**Edition Number:** leer lassen

**Author:**
```
Vorname: Petra        Nachname: Tanner
```

**Contributors:** nichts eintragen

**Description:** siehe Schritt 3

**Publishing Rights:** `I own the copyright and I hold the necessary publishing rights`

**Primary Audience:** Sexually explicit images: **No** · Reading age: leer

**Marketplace:** `Amazon.de`

**Categories:** siehe Schritt 4

**Keywords:** siehe Schritt 5

---

## Schritt 3: Beschreibung

Das ist der Text, der über Kauf oder Nichtkauf entscheidet.
Genau so einfügen, die Zeilenumbrüche gehören dazu.

```
Du wartest immer noch. Auf eine Antwort, die nie kommt. Auf eine Entschuldigung,
die nie kommt. Auf die eine Einsicht, die alles erklären würde.

Vielleicht ist die Person nicht mehr in deinem Leben. Vielleicht ist sie es noch,
schweigt aber zu dem, was passiert ist. Vielleicht ist sie gestorben, bevor das
Gespräch stattfinden konnte. In deinem Kopf läuft es trotzdem weiter, jeden Tag.

Dieses Buch stellt eine andere Frage: Was, wenn du kein letztes Gespräch brauchst,
um frei zu werden?

DAS EINZIGE BUCH, DAS AUCH OHNE ANTWORT, EINSICHT ODER ENTSCHULDIGUNG FUNKTIONIERT

Fast jeder Ratgeber zu Abschluss und Loslassen setzt voraus, dass die andere Person
mitmacht, sich entschuldigt oder wenigstens zuhört. Dieses Buch ist anders gebaut:

• Ein Selbsttest gleich am Anfang: Bist du das?
• Notfall-Seiten weit vorne, für Tage, an denen selbst das zu viel ist.
• Wörtliche Sätze zum Auswendiglernen, nicht nur Haltungen.
• Ein Kapitel darüber, was du tust, wenn die andere Person nie einsieht, was war.
• Ein Rückfall-Kapitel, für die Tage, an denen das alte Warten zurückkommt.
• Eine Satz-Sammlung am Schluss, zum Nachschlagen ohne nochmal zu lesen.

FÜR ALLE, DIE NOCH AUF EINE ANTWORT WARTEN

Von Eltern, die nie anerkennen, was geschehen ist.
Von Geschwistern, die die Vergangenheit anders erzählen.
Von Ex-Partnern, Freundschaften ohne Abschluss, ehemaligen Kollegen und Vorgesetzten.
Von Menschen, die sich nie erklärt haben, bevor sie gegangen sind, oder gestorben sind.

Petra Tanner ist Autorin und Mentorin und arbeitet seit sechsundzwanzig Jahren mit
Menschen in ihrer Praxis. Sie kennt den Satz, der öfter fällt als jeder andere:
„Ich warte doch nur auf ein einziges Gespräch."

Du brauchst dieses Gespräch nicht, um weiterzugehen. Das ist der Anfang.
```

---

## Schritt 4: Kategorien

**Achtung:** KDP hat einen eigenen Kategoriebaum, nicht den von Amazon.de.
Ein Oberbegriff „Ratgeber" existiert dort nicht. Der richtige heisst **Selbsthilfe**.

Vorher unbedingt den primären Marketplace auf **Amazon.de** stellen. Bei
Amazon.com landet das Buch im falschen Shop, und die deutschen Suchbegriffe
laufen ins Leere.

Dann unter `Bücher > Selbsthilfe` genau drei Häkchen:

```
Trauer & Verlust
Beziehungen
Emotionen
```

- **Trauer & Verlust** ist der direkte Treffer für unbeendete Kapitel, Verlust
  ohne Abschluss, Trauer ohne Beerdigung (Ambiguous Loss)
- **Beziehungen** deckt Familie, Ex-Partner, Freundschaften ohne Abschluss ab
- **Emotionen** trifft das Warten, die Hoffnung, den inneren Groll

Vor dem endgültigen Absenden im KDP-Dashboard die tatsächliche Dropdown-Liste
prüfen, sie ändert sich gelegentlich. Nicht „Allgemein" nehmen.

## Schritt 5: Die sieben Keywords

Eins pro Feld, genau so:

```
1   loslassen ohne entschuldigung buch
2   entfremdung familie eltern verstehen
3   abschluss finden ohne aussprache
4   trauer um beziehung ohne tod
5   toxische eltern nie entschuldigt
6   innerer frieden nach trennung ohne kontakt
7   emotional unabhängig werden von menschen die schweigen
```

**Warum diese und keine anderen:**

Wörter, die schon im Titel oder Untertitel stehen, sind bei Amazon bereits
indexiert. „Letztes Gespräch", „frei werden" und „Entschuldigung" kommen
deshalb hier nicht mehr einzeln vor.

Jedes Feld ist eine ganze Suchphrase, kein Einzelwort. Feld 2 und 6 holen
zwei grosse, unterschiedliche Zielgruppen: Menschen mit schwierigen Eltern,
und Menschen nach einer Trennung ohne Kontaktabbruch-Möglichkeit.

---

## Schritt 6: Paperback Content

**Print Options**
- Ink and Paper: `Black & white interior with cream paper`
- Format: `5,5 x 8,5 Zoll`
- Bleed: `No Bleed`
- Cover-Ausführung: `Matt`

> Glanz, nicht Matt. Bei dunklen Covern entstehen auf mattem Papier
> Scheuerstellen an den Kanten.

**ISBN:** `Assign me a free KDP ISBN`

**Manuscript:** `buch-Taschenbuch.pdf` hochladen

**Book Cover:** `Upload a cover you already have (print-ready PDF)` →
`buch-Cover-FullWrap-Foto.pdf`

**Previewer starten.** Er meldet Fehler und Warnungen.
Fehler musst du beheben, Warnungen zu Randabständen kannst du ignorieren,
wenn im Vorschaubild alles gut aussieht.

**Im Previewer selbst nachsehen, nicht nur auf grün klicken:**
- Seite 1 Titel, Seite 5 Einleitung
- Seite mit den Krisennummern (weit vorne, „Wenn heute gar nichts geht")
- Seite 104 mit dem Bonus-QR-Code, Code testweise scannen
- Impressum am Schluss (Wiesentalstrasse 68, 9240 Uzwil)
- Cover: Rücken mittig, Barcodefeld unten rechts frei

---

## Schritt 7: Rights & Pricing

**Territories:** `All territories (worldwide rights)`

**Primary Marketplace:** `Amazon.de`

**Preis:**

| | |
|---|---|
| Listenpreis | **12,99 EUR** |
| Druckkosten | ca. 2,05 EUR |
| Deine Tantieme | **ca. 5,22 EUR pro Buch** |

Die anderen Länder füllt Amazon automatisch. Unter 10 EUR wirkt ein
Ratgeber billig, 12,99 ist die Stelle, an der Preis und Wahrnehmung
zueinander passen, konsistent mit deinen anderen Büchern.

**Expanded Distribution:** aus lassen. Das kostet Marge und bringt kaum etwas.

**Publish Your Paperback Book** klicken.

---

## Schritt 8: Danach

1. **72 Stunden warten.** So lange braucht Amazon für die Indexierung.
2. **Autorenseite** auf Amazon Author Central prüfen, das Buch dem
   bestehenden Profil zuordnen.
3. **Ein Belegexemplar bestellen.** Author Copies, nur Druckkosten plus Versand.
4. **Fünf bis zehn Bewertungen sammeln**, verteilt über zwei bis drei Wochen.
5. **Erst dann TikTok/Social**, nicht davor.

---

## Schritt 9: Das eBook (Kindle)

Taschenbuch und eBook sind bei KDP zwei getrennte Veröffentlichungen, die du
später zu einer Produktseite verbinden kannst.

| | |
|---|---|
| Manuskript | `buch-eBook.epub` |
| Cover | `buch-eBook-Cover.png`, 1600 × 2560 px, Verhältnis 1,6:1 |

**Bookshelf → Create → Create Kindle eBook**

- **Language / Title / Subtitle / Author:** identisch zum Taschenbuch, Schritt 2
- **Manuscript:** `buch-eBook.epub` hochladen, Previewer starten und durchklicken
- **eBook Cover:** `buch-eBook-Cover.png`
- **Kindle-eBook-Vorschau prüfen:** Titelseite, Einleitung, erstes Kapitel,
  Krisennummern-Seite, Bonus-QR-Code-Seite, Rechtliche Hinweise am Schluss
- **KDP Select:** an dir. Bindet das Buch 90 Tage exklusiv an Amazon, dafür
  Kindle Unlimited und Countdown-Deals möglich
- **Preis:** etwa 7,99 bis 8,99 EUR, damit 70 % Tantieme greifen

---

## Schritt 10: Das Journal (zweites, eigenständiges Produkt)

Eigener Titel, eigene ASIN, verweist im Buch aufeinander, aber ist kein
Teil derselben KDP-Veröffentlichung.

| | |
|---|---|
| Manuskript | `journal-Taschenbuch.pdf` |
| Cover | `journal-Cover-FullWrap.pdf` |

Gleicher Ablauf wie Schritt 1-8, mit eigenem Titel (z. B. „Du brauchst
kein letztes Gespräch, das Journal") und eigener Beschreibung.

---

## Was noch offen ist

- Journal-Beschreibungstext für KDP schreiben, sobald du so weit bist
- Rückwirkend: Rechtssicherheit, Impressum und Cover bei Buch 3, 4 und 5 prüfen
