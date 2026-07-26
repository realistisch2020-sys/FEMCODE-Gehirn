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

- A5, Ränder 1,9 cm seitlich und 2,2 cm oben/unten
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

Papier Creme, A5:

```
Rückenbreite  = Seitenzahl × 0,0025 Zoll × 25,4
Coverbreite   = 3,2 + 148 + Rücken + 148 + 3,2   (mm)
Coverhöhe     = 3,2 + 210 + 3,2 = 216,4          (mm)
```

Bei 126 Seiten: Rücken 8,00 mm, Cover 310,40 × 216,40 mm.

Ab 79 Seiten erlaubt KDP Text auf dem Buchrücken.
Sicherheitsabstand zu allen Schnittkanten: mindestens 6 mm.
Barcode-Feld unten rechts auf der Rückseite freihalten, etwa 52 × 32 mm.
