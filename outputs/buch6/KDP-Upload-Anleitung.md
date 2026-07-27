# Buch 6 bei KDP hochladen, Schritt für Schritt

Stand 26. Juli 2026. Alles zum Abschreiben oder Kopieren.
Nichts davon muss noch entschieden werden.

---

## Schritt 0: Was du bereithalten musst

| | |
|---|---|
| Manuskript | `buch6-Taschenbuch.pdf`, 111 Seiten |
| Cover | `buch6-Cover-FullWrap.pdf`, 292,85 × 222,30 mm |
| Format | 5,5 x 8,5 Zoll (13,97 × 21,59 cm) |
| Papier | Creme |
| Rückenbreite | 7,05 mm |
| Covermass gesamt | 292,85 × 222,30 mm |

Das Manuskript ist fertig geprüft: Schriften eingebettet, Seitenmass stimmt,
keine leere Seite, alle Seitenzahlen im Inhaltsverzeichnis korrekt.

Beide Dateien sind fertig und geprüft. Neu bauen lässt sich das Cover mit:

```bash
python3 tools/buch6-cover.py outputs/buch6/cover-entwuerfe/cover-front-druckfertig.png
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
Ich bin so müde. Und niemand fragt mich warum
```

**Subtitle:**
```
Das Funktions-Ich: Wenn du für alle stark bist und dich dabei verlierst
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
Du funktionierst. Aber du lebst nicht.

Du stehst auf, machst Kaffee, beantwortest Nachrichten, bevor du gefrühstückt
hast. Du bist für alle da. Du sagst „Macht nichts“, obwohl es doch etwas macht.
Und abends fällst du ins Bett und weisst nicht, wovon du eigentlich so erschöpft
bist.

Es ist keine Krise. Es ist nichts Dramatisches passiert.
Und genau das macht es so schwer zu erklären.

Dieses Buch gibt dem einen Namen: das Funktions-Ich.

DAS EINZIGE BUCH, DAS AUCH AN DEM TAG FUNKTIONIERT, AN DEM DU GAR NICHTS KANNST

Fast jeder Ratgeber verlangt Energie, die du gerade nicht hast. Dieses hier ist
anders gebaut:

• Ein Selbsttest gleich am Anfang. Zwei Minuten, und du weisst, wo du stehst.
• Notfall-Seiten weit vorne. Was tun, wenn heute wirklich nichts geht.
• Wörtliche Sätze zum Auswendiglernen, nicht nur Haltungen.
• Ein Kapitel für den Fall, dass die anderen nicht mitmachen.
• Ein Rückfall-Kapitel, damit du dich nach drei Wochen nicht gescheitert fühlst.
• Eine Satz-Sammlung am Schluss, zum Nachschlagen ohne nochmal zu lesen.

IN FÜNF SCHRITTEN

Sehen. Verstehen. Erlauben. Lernen. Werden.
Neunzehn Kapitel, die dich nicht überfordern, weil jedes für sich steht.

FÜR DICH, WENN DU DICH HIER WIEDERFINDEST

Du weinst im Auto, damit es niemand sieht.
Du machst alles selbst, weil bitten sich schlimmer anfühlt als tragen.
Du hast ein schlechtes Gewissen, wenn du Nein sagst.
Du weisst nicht mehr, wer du bist, wenn niemand etwas von dir will.

Petra Tanner ist Coachin und arbeitet seit sechsundzwanzig Jahren mit Menschen
in ihrer Praxis. In dieser Zeit hat sie einen Satz öfter gehört als jeden
anderen: „Ich kann nicht mehr. Aber ich muss ja.“

Du musst nicht stark sein, um dieses Buch zu lesen.
Du darfst müde sein. Das ist der Anfang.
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
Stress & Stressbewältigung
Emotionen
Selbstachtung
```

- **Stress & Stressbewältigung** ist der direkte Treffer für Erschöpfung
- **Emotionen** deckt Schuldgefühle und schlechtes Gewissen ab
- **Selbstachtung** trifft Grenzen setzen und Nein sagen

Nicht „Allgemein" nehmen. Grösste Kategorie, keine Chance auf eine Liste.

## Schritt 5: Die sieben Keywords

Eins pro Feld, genau so:

```
1   mental load mutter erschöpft
2   nein sagen lernen frauen grenzen setzen
3   emotionale erschöpfung alltag hilfe
4   selbstfürsorge für frauen buch
5   immer für alle da sein aufhören
6   grenzen setzen ohne schuldgefühle
7   erschöpfte mütter kraftlos ratgeber
```

**Warum diese und keine anderen:**

Wörter, die schon im Titel oder Untertitel stehen, sind bei Amazon bereits
indexiert. Sie im Keywordfeld zu wiederholen ist verschenkter Platz. Deshalb
kommt „müde", „stark" und „Funktions-Ich" hier nicht mehr vor.

Jedes Feld ist eine ganze Suchphrase, kein Einzelwort. So sucht die Zielgruppe
tatsächlich: nicht „Erschöpfung", sondern „immer für alle da sein aufhören".
Diese langen Phrasen haben weniger Konkurrenz, und wer so sucht, kauft.

Feld 1 holt die Frauen um dreissig, die sich im Cover nicht wiedererkennen,
aber genau dieses Problem googeln.

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

**Manuscript:** `buch6-Taschenbuch.pdf` hochladen

**Book Cover:** `Upload a cover you already have (print-ready PDF)` →
`buch6-Cover-FullWrap.pdf`

**Previewer starten.** Er meldet Fehler und Warnungen.
Fehler musst du beheben, Warnungen zu Randabständen kannst du ignorieren,
wenn im Vorschaubild alles gut aussieht.

**Im Previewer selbst nachsehen, nicht nur auf grün klicken:**
- Seite 1 Titel, Seite 5 Einleitung
- Seite 16 mit den Krisennummern
- Seite 126 Impressum
- Cover: Rücken mittig, Barcodefeld unten rechts frei

---

## Schritt 7: Rights & Pricing

**Territories:** `All territories (worldwide rights)`

**Primary Marketplace:** `Amazon.de`

**Preis:**

| | |
|---|---|
| Listenpreis | **12,99 EUR** |
| Druckkosten | ca. 2,11 EUR |
| Deine Tantieme | **ca. 5,17 EUR pro Buch** |

Die anderen Länder füllt Amazon automatisch. Mindestpreis wäre 3,52 EUR,
aber unter 10 EUR wirkt ein Ratgeber billig. 12,99 ist die Stelle, an der
Preis und Wahrnehmung zusammenpassen.

**Expanded Distribution:** aus lassen. Das kostet Marge und bringt kaum etwas.

**Publish Your Paperback Book** klicken.

---

## Schritt 8: Danach

1. **72 Stunden warten.** So lange braucht Amazon für die Indexierung.
   In dieser Zeit findet man das Buch über die Keywords noch nicht.
2. **Autorenseite** auf Amazon Author Central anlegen oder das Buch dem
   bestehenden Profil zuordnen.
3. **Ein Belegexemplar bestellen.** Author Copies, nur Druckkosten plus Versand.
   Das Buch in der Hand ist die letzte Prüfung, die kein Skript ersetzt.
4. **Fünf bis zehn Bewertungen sammeln**, verteilt über zwei bis drei Wochen.
   Nicht alle am ersten Tag, das fällt auf.
5. **Erst dann TikTok.** Ein viraler Clip auf ein Buch ohne Bewertungen
   verbrennt den Traffic, und der kommt nicht wieder.

---

## Schritt 9: Das eBook (Kindle)

Taschenbuch und eBook sind bei KDP zwei getrennte Veröffentlichungen, die du
später zu einer Produktseite verbinden kannst ("Kindle eBook" beim Taschenbuch
verlinken). Bereit dafür:

| | |
|---|---|
| Manuskript | `buch6-eBook.epub` |
| Cover | `buch6-eBook-Cover.png`, 2042 × 3267 px, Verhältnis 1,6:1 |

Neu bauen lässt sich beides mit:

```bash
python3 tools/buch6-ebook.py
```

**Wichtigster Unterschied zum Taschenbuch:** Kindle-Text fliesst, es gibt keine
festen Seiten. Deshalb hat das eBook kein Inhaltsverzeichnis mit Seitenzahlen
mehr, sondern eine anklickbare Navigation, die jeder eReader automatisch
anzeigt. Das Cover hat keinen Rücken und keine Rückseite, nur die Vorderseite,
zugeschnitten auf Amazons empfohlenes Verhältnis 1,6 zu 1.

**Bookshelf → Create → Create Kindle eBook**

- **Language / Title / Subtitle / Author:** identisch zum Taschenbuch, Schritt 2
- **Manuscript:** `buch6-eBook.epub` hochladen, Previewer starten und durchklicken
- **eBook Cover:** `buch6-eBook-Cover.png`
- **Kindle-eBook-Vorschau prüfen:** Titelseite, Widmung, Einleitung, erstes
  Kapitel, Krisennummern-Seite, Rechtliche Hinweise am Schluss
- **KDP Select:** an dir. Bindet das Buch 90 Tage exklusiv an Amazon, dafür
  Kindle Unlimited und Countdown-Deals möglich. Bei einem Erstlingsbuch in
  einer Nische meist sinnvoll, um die Reichweite von KU mitzunehmen
- **Preis:** eBooks liegen meist 30 bis 40 % unter dem Taschenbuchpreis,
  also etwa 7,99 bis 8,99 EUR, damit 70 % Tantieme greifen (zwischen 2,99
  und 9,99 EUR Voraussetzung dafür)

Geprüft am erzeugten eBook: keine private Mailadresse, keine Bezeichnung
"Heilerin", Kontaktadresse korrekt vorhanden, Krisennummer liegt bei rund
9 % der Textlänge, also weit vorne.

---

## Was noch offen ist

- Rückwirkend: Rechtssicherheit, Impressum und Cover bei Buch 3, 4 und 5
- Neue TikTok- und Instagram-Konten
