# Werkzeuge für die Buchproduktion

Zwei Skripte. Beide laufen ohne Installation, Python und ReportLab sind da.

---

## buch6-word2pdf.py

Macht aus der korrigierten Word-Datei das druckfertige Taschenbuch-PDF.

```bash
python3 tools/buch6-word2pdf.py outputs/buch6/buch6-MANUSKRIPT.docx
```

Ergebnis: `outputs/buch6/buch6-Taschenbuch.pdf`

**So läuft der Ablauf:** Petra korrigiert im Word, das Skript setzt daraus das PDF.
Die Word-Datei ist die Quelle, das PDF wird immer neu erzeugt und nie von Hand bearbeitet.

Was das Skript automatisch macht:

- 5,5 x 8,5 Zoll, Ränder 1,9 cm seitlich und 2,2 cm oben/unten
- Seitenzahl mittig unten, kleines Herz unten rechts
- Vorspann ohne Seitenzahlen, Hauptteil nummeriert
- Inhaltsverzeichnis mit echten Seitenzahlen, in zwei Durchgängen berechnet
- Kapitel beginnen 1,9 cm tiefer auf der Seite, wie im klassischen Buchsatz
- Fette Zwischentitel stehen nie allein am Seitenfuss
- Reflexionsblöcke werden nie über den Seitenrand gerissen
- Fett und kursiv werden aus dem Word übernommen
- Die grauen TikTok-Kästen bleiben erhalten

---

## buch6-cover.py

Baut den Full-Wrap-Umschlag für KDP: Rückseite, Rücken und Vorderseite in einem Stück.

**Mit eigenem Coverbild:**
```bash
python3 tools/buch6-cover.py pfad/zum/cover-vorderseite.png
```

**Ohne Bild**, dann wird eine rein typografische Vorderseite gezeichnet:
```bash
python3 tools/buch6-cover.py
```

Ergebnis: `outputs/buch6/buch6-Cover-FullWrap.pdf`

Das Skript sagt beim Ausführen, wie viele dpi das eingesetzte Bild erreicht,
und warnt, wenn es unter 300 liegt.

**Wichtig:** Oben im Skript steht `SEITEN = 126`. Ändert sich der Umfang des
Manuskripts, muss diese Zahl angepasst werden, sonst stimmt die Rückenbreite nicht.

---

## Die Formeln, falls von Hand gerechnet wird

Papier Creme, 5,5 x 8,5 Zoll (139,7 × 215,9 mm):

```
Rückenbreite  = Seitenzahl × 0,0025 Zoll × 25,4
Coverbreite   = 3,2 + 139,7 + Rücken + 139,7 + 3,2   (mm)
Coverhöhe     = 3,2 + 215,9 + 3,2 = 222,3            (mm)
```

Bei 126 Seiten: Rücken 8,00 mm, Cover 293,80 × 222,30 mm.

Ab 79 Seiten erlaubt KDP Text auf dem Buchrücken.
Sicherheitsabstand zu allen Schnittkanten: mindestens 6 mm.
Barcode-Feld unten rechts auf der Rückseite freihalten, etwa 52 × 32 mm.

---

## buch-pruefen.py

Prüft ein Manuskript und sein PDF gegen alle Regeln, die je aufgefallen sind.

```bash
python3 tools/buch-pruefen.py outputs/buch6/buch6-MANUSKRIPT.docx \
                              outputs/buch6/buch6-Taschenbuch.pdf
```

Läuft **nach jeder Änderung**, nicht nur am Schluss. Genau da sind bisher die
Fehler entstanden: geprüft wurde immer nur die eine Stelle, die gerade geändert
wurde, und die Fehler von letzter Woche lagen weiter da.

Was geprüft wird:

- Typografie: ß, Gedankenstriche, gerade Anführungszeichen und Apostrophe,
  doppelte Leerzeichen, Leerzeichen vor Satzzeichen, Auslassungspunkte,
  Anführungszeichen paarig gezählt
- **Fehlende Kommas** vor Relativ- und Nebensätzen
- Rechtssicherheit nach `context/rechtssicherheit.md`: private Mailadresse,
  Bezeichnung Heilerin, Therapeutin über die Autorin, Ausschlussdiagnosen,
  Heilversprechen, alle acht Punkte des Pflichtteils
- Kapitelnummern lückenlos, kein Kapiteltitel mit Schlusspunkt
- Im PDF: leere und fast leere Seiten, **jede Seitenzahl im Inhaltsverzeichnis
  gegen die tatsächliche Seite**, Krisennummern im vorderen Drittel
- Rückenbreite und Covermass aus der tatsächlichen Seitenzahl

Das Skript endet mit einem Fehlercode, wenn es etwas gefunden hat.
Nicht jeder Treffer ist ein Fehler, Vergleichssätze werden mitgemeldet.
Aber jeder Treffer muss angeschaut werden.

---

## haut-entrastern.py

Nimmt das regelmässige Netzmuster aus KI-erzeugter Gesichtshaut.

```bash
python3 tools/haut-entrastern.py cover-front-roh.png cover-front-druckfertig.png 1.0
```

Bildgeneratoren legen auf Haut oft eine gleichmässige feine Struktur, die aus
der Nähe wie Stoff oder Reptilhaut aussieht. Das ist nicht dasselbe wie zu
glatte Haut, es ist zu viel gleichförmige Textur.

Das Skript dämpft genau diese hochfrequente Schicht und lässt Falten, Poren
und Formen stehen. Geschützt werden über eine Kanten- und Helligkeitsmaske:
Augen, Brauen, Lippen, Nasenlöcher, Haare und die Goldadern. Zum Schluss
kommt feines Filmkorn dazu, sonst wirkt die Fläche tot.

Die letzte Zahl ist die Stärke, 0 bis 1. Bei 1 wird am meisten gedämpft.
Die Rohdatei immer aufheben, das Skript arbeitet nicht rückwärts.
