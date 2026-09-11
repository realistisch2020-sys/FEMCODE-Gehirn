# Mein Business

Hier kommt rein, womit du Geld verdienst und für wen. Damit kann Claude Content, Angebote und Texte wirklich in deinem Kontext bauen.

## Was ich anbiete

- MONAT Haarpflege-Produkte (Schweiz, swiss.mymonat.com) unter der Marke "Safe to Thrive x MONAT"
- "DupliHer für Networker": Duplikationssystem für Teampartnerinnen (17 Module, 35 Skripte, 112 Posts, fertig zum Kopieren)
- Interaktive Quiz-Landingpages als Lead-Magnet (z. B. "Welcher Haar-Typ bist du?")

## Meine Zielgruppe

- Endkundinnen für Haarpflege (Einstieg über den Haar-Typ-Test)
- Eigene Teampartnerinnen im MONAT-Business (Duplikationssystem, personalisierte Testseiten)

## Meine Kanäle

- Instagram: @petra.safetothrive
- WhatsApp (Direktkontakt über wa.me-Links in den Landingpages)
- Landingpages via GitHub Pages, siehe "So veröffentliche ich Seiten" unten

## Meine Angebote und Preise

Was kostet was? Grobe Preisspannen reichen.

## So veröffentliche ich Seiten (technisch)

- Alle Quiz-/Landingpages laufen über GitHub Pages im Repo FEMCODE-Gehirn, Branch `gh-pages`, jede Seite in eigenem Unterordner (z. B. `monat-persoenlichkeitstest/`) → eigener Link, bestehende Seiten bleiben beim Hinzufügen unangetastet.
- Teampartner-Seiten kommen unter `team/<name>/` im selben Repo — ein komplett eigenes Repo geht technisch nicht (GitHub-Berechtigung hier reicht nur für FEMCODE-Gehirn, `create_repository` liefert 403).
- Pro Teampartner-Seite werden 4 Dinge ausgetauscht: Name, WhatsApp-Nummer, Instagram-Handle, MONAT-Anmelde-/Shoplink. Rest (Fragen, Bilder, Design) bleibt gleich.
- Netlify/Vercel CLI funktionieren in dieser Cloud-Umgebung nicht (kein Login möglich) — GitHub Pages ist der zuverlässige Weg.
- Deployte Seiten sind unbefristet gültig (kein Ablaufdatum), solange Datei/Repo/Pages bestehen bleiben.

Kurz halten. Genug damit Claude dich versteht, kein vollständiges Wiki.
