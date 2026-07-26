# Buch 6 bei KDP hochladen, Schritt für Schritt

Stand 26. Juli 2026. Alles zum Abschreiben oder Kopieren.
Nichts davon muss noch entschieden werden.

---

## Schritt 0: Was du bereithalten musst

| | |
|---|---|
| Manuskript | `buch6-Taschenbuch.pdf`, 126 Seiten |
| Cover | `buch6-Cover-FullWrap.pdf` **fehlt noch** |
| Format | A5, 14,8 × 21 cm |
| Papier | Creme |
| Rückenbreite | 8,00 mm |
| Covermass gesamt | 310,40 × 216,40 mm |

Das Manuskript ist fertig geprüft: Schriften eingebettet, Seitenmass stimmt,
keine leere Seite, alle Seitenzahlen im Inhaltsverzeichnis korrekt.

**Ohne Cover geht es nicht weiter.** Sobald die Vorderseite von ChatGPT da ist:

```bash
python3 tools/buch6-cover.py pfad/zur/vorderseite.png
```

Anforderungen an die Vorderseite: mindestens 2100 × 3000 Pixel,
Seitenverhältnis 0,7 zu 1, kein Text am Rand.

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

Bis zu drei, in dieser Reihenfolge:

1. `Ratgeber > Lebensführung & Persönliche Entwicklung > Selbsthilfe`
2. `Ratgeber > Gesundheit & Fitness > Stressbewältigung`
3. `Sachbücher > Psychologie > Angewandte Psychologie`

Falls Amazon die Bezeichnungen leicht anders anzeigt, das Nächstliegende nehmen.
Kategorien lassen sich später jederzeit ändern, ohne Neuveröffentlichung.

---

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
- Trim Size: `14.8 x 21 cm`
- Bleed: `No Bleed`
- Cover Finish: `Glossy`

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

## Was noch offen ist

- Cover-Datei, der einzige echte Blocker
- Neue TikTok- und Instagram-Konten
- Rückwirkend: Rechtssicherheit, Impressum und Cover bei Buch 3, 4 und 5
