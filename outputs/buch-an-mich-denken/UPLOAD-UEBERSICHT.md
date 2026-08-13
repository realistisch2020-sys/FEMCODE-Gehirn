# Upload-Übersicht: Ich habe nie gelernt, an mich zu denken

Stand: 13. August 2026. Alle Dateien in diesem Ordner geprüft und bereit für den KDP-Upload.

## Hauptbuch (Taschenbuch)

- Manuskript: `buch4-MANUSKRIPT.docx` (Quelle) / `buch4-Taschenbuch.pdf` (Druck-PDF)
- 75 Seiten. Ursprüngliches Ziel war ~100 Seiten, Petra hat den 75-Seiten-Stand am
  13. August 2026 final freigegeben, nicht weiter ausgebaut.
- Cover: `buch4-Cover-Print-FullWrap.pdf` (Vorderseite + Rücken + Rückseite),
  290,07 × 222,25 mm, Rücken 4,76 mm — passt exakt zu 75 Seiten. **Bei jeder
  weiteren Änderung der Seitenzahl muss dieses Cover neu berechnet werden**,
  sonst stimmt die Rückenbreite nicht mehr.
- Geprüft mit `tools/buch-pruefen.py`: alle acht Pflichtteile der
  Rechtssicherheit vorhanden (Impressum, Adresse, Kontakt, Haftungsausschluss
  etc.), keine private Mailadresse, keine „Heilerin", Kapitelnummern
  lückenlos, Schriften im PDF eingebettet, Seitenmass korrekt (5,5 × 8,5 Zoll).
- Zwei sehr kurze Seiten (32, 58) sind Absicht — einzeilige „Pointe"-Sätze am
  Kapitelende, kein Fehler.
- Inhaltsverzeichnis listet nur Kapiteltitel ohne Seitenzahlen (wie bei Buch 3
  und 4, gleiches einfacheres Erstellungs-Skript ohne Word-Formatvorlagen) —
  das ist der bestehende Stil dieser Buchreihe, kein neuer Fehler.

## Hauptbuch (eBook)

- Neu gebaut: `buch4-eBook.epub`, 37 Kapitel/Seiten, alle Pflichtteile
  automatisch geprüft und vorhanden.
- eBook-Cover (Vorderseite only): `cover-FRONT.jpg` (für den Upload, JPEG)
  bzw. `cover-FRONT.png` (Quelle), 1650 × 2550 px.

## Journal / Workbook (zweites Produkt)

- Manuskript: `buch4-Journal-MANUSKRIPT.docx` / `buch4-Journal-Taschenbuch.pdf`, 59 Seiten
- Cover: `journal-Cover-Print-FullWrap.pdf`, 289,14 × 222,25 mm
- eBook-Cover Vorderseite: `journal-cover-FRONT.png`
- Laut letztem Bearbeitungsstand bereits lektoriert.

## Noch offen (nicht in diesem Ordner enthalten)

- **Klappentext / Amazon-Beschreibung** für dieses Buch: nicht gefunden, wurde
  nie ausformuliert. Vor dem Upload nötig.
- **Amazon-Keywords** (7 Stück, siehe `context/kdp-buch-produktion.md`):
  für dieses Buch noch nicht recherchiert/festgelegt, anders als für Buch 3
  und 4 (schlechte Gewissen).
- **Kategorien** für die KDP-Einreichung: noch nicht festgelegt.
- **Preis**: noch nicht entschieden, Empfehlung aus dem Standard-Prozess wäre
  $12,99–13,99 je nach Seitenzahl.
- Journal: eBook (epub) wurde für das Journal nicht gebaut, nur Taschenbuch.

## Ablauf beim eigentlichen Upload

Reihenfolge und KDP-Detaileinstellungen (Papier, Ränder, KI-Angaben, Preisstufen)
sind identisch zum bewährten Prozess in `context/kdp-buch-produktion.md`
Abschnitt „KDP-Einreichung Reihenfolge". Kurzfassung:

1. Manuskript-PDF hochladen, Seitenzahl bestätigen (muss 75 bzw. 59 sein)
2. Cover-PDF hochladen (Full-Wrap-Datei, nicht die PNG)
3. KI-Angaben setzen: Text „Gesamtes Werk, mit umfangreicher Bearbeitung",
   Bilder „Gesamtes Werk, mit minimaler oder keiner Bearbeitung"
4. Klappentext, Keywords, Kategorien und Preis ergänzen (siehe oben, noch offen)
5. Druckausführung: **Matt**, Papier Creme, kein Bleed — Serienkonsistenz mit
   den anderen Büchern
6. eBook separat als Kindle-Produkt hochladen (`buch4-eBook.epub` +
   `cover-FRONT.jpg`)
