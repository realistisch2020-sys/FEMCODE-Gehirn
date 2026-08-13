# Upload-Übersicht: Ich habe nie gelernt, an mich zu denken

Stand: 13. August 2026, zweite Prüfrunde. Manuskripte inhaltlich gelesen (nicht
nur automatisch geprüft), Rechtschreibung mit hunspell (deutsches Wörterbuch)
geprüft, Rechtssicherheit und leere Seiten in allen drei Formaten kontrolliert.

**Ehrliche Einschätzung zum Inhalt:** Das Manuskript ist stark. Eine durchgängige
Beispielfigur (Claudia), konkrete Szenen statt allgemeiner Ratgeber-Sprache,
ein klar benanntes Alleinstellungsmerkmal (das „Selbstvergessen" als Stufe vor
Grenzen setzen), harte Fakten eingebaut (Gehaltslücke, Pflegearbeit-Zahlen),
und durchgehend die geforderte Tun-Komponente (wörtliche Sätze, Wochenplan,
Rückfall-Kapitel). Erfüllt den eigenen Standard aus `context/buch-standard.md`.

## Gefunden und behoben (13. August, zweite Runde)

- **Echter Tippfehler**, Hauptbuch, Abschnitt „Zur Autorin": „ist seid 26 Jahren"
  → „ist seit 26 Jahren" korrigiert. Taschenbuch-PDF und eBook daraus neu gebaut.
- **11 Gedankenstriche + 3 Auslassungspunkte im Journal-Manuskript**, verstösst
  gegen die explizite, rückwirkend geltende Regel in `context/buch-standard.md`
  §8/§9 (kein Gedankenstrich im Fliesstext, keine Auslassungspunkte). Alle 14
  Stellen korrigiert (Gedankenstrich → Komma, Auslassungspunkte entfernt).
  Journal-Taschenbuch-PDF daraus neu gebaut, Seitenzahl unverändert (59).
- Keine echten Rechtschreibfehler sonst gefunden (hunspell-Liste bestand fast
  nur aus Schweizer ss-Schreibung, Eigennamen und dem Fachbegriff
  „Selbstvergessen" — alles korrekt so).
- Keine leeren Seiten in Taschenbuch oder Journal. Zwei sehr kurze Seiten im
  Hauptbuch (32, 58) sind Absicht: einzeilige „Pointe"-Sätze am Kapitelende.
- Rechtssicherheit in beiden Manuskripten vollständig: alle acht Pflichtteile,
  keine private Mailadresse, keine „Heilerin", korrekte Berufsbezeichnung.

## Noch offen: zwei Punkte im Journal-COVER, nicht selbst korrigiert

Beim visuellen Cover-Check gefunden, aber **nicht** repariert, weil dafür die
ursprüngliche Design-Datei nötig wäre (nur das fertige PNG/PDF liegt hier) und
weil einer der Punkte eine inhaltliche Entscheidung ist, die dir gehört:

1. Auf der Journal-Rückseite steht im Titel ein Gedankenstrich: „Ich habe nie
   gelernt, an mich zu denken — Das Journal" sowie im Fliesstext „eine kleine
   Übung — dazu eine Checkliste". Verstösst gegen dieselbe No-Gedankenstrich-Regel
   wie oben, diesmal im Cover-Bild selbst eingebrannt.
2. Cover-Vorderseite und Rückseite behaupten beide „22 Kapitel". Das Journal-
   Manuskript hat tatsächlich 25 mit „Kapitel" überschriebene Abschnitte (20
   durchnummerierte plus 5 mit Buchstaben, z. B. 10b, 18b–18e). Möglich, dass
   22 bewusst vereinfacht war, bevor die Buchstaben-Kapitel dazukamen — das
   kann ich nicht für dich entscheiden.

Zusätzlich, rein kosmetisch: Die Unterzeile auf dem Hauptbuch-Cover lautet
„...für alle sorgst und dich selbst dabei verlierst", im Manuskript-Titelblatt
steht „...für alle sorgst und dich dabei selbst verlierst" (Wortstellung
vertauscht). Fällt beim Lesen kaum auf, der Vollständigkeit halber notiert.

**Sag Bescheid, wenn ich die Cover-Korrektur versuchen soll** (Text-Patch auf
dem bestehenden Bild, Schrift/Farbe nachgebildet) — sonst kannst du heute Abend
mit den Covern so hochladen, wie sie sind, das sind keine KDP-Blocker, nur
Konsistenz-/Genauigkeitsfragen.

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

- Manuskript: `buch4-Journal-MANUSKRIPT.docx` / `buch4-Journal-Taschenbuch.pdf`, 59 Seiten (unverändert nach der Korrektur)
- Cover: `journal-Cover-Print-FullWrap.pdf`, 289,14 × 222,25 mm — Korrekturbedarf siehe oben
- eBook-Cover Vorderseite: `journal-cover-FRONT.png`
- Text jetzt zweimal geprüft (Lektorat aus der letzten Session + heutige Rechtschreib-/Stilprüfung).

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
