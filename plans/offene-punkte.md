# Offene Punkte

Hier landen alle laufenden ToDos. Claude pflegt diese Datei beim `/shutdown` automatisch — erledigte Punkte raus, neue rein.

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
