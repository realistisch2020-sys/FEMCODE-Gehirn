# Funnel „LISTE“ – Reel → PDF → Buch (08.10.2026)

Design: modern, Beerentöne (Beere #6B1D46, Himbeere #B8326A, Zartrosa #F6E3EB), Schriften Fraunces + DM Sans. Übersicht: `funnel-uebersicht.png`. Generatoren: `pdf-generator.js`, `reel-generator.js`, `funnel-grafik.js`.

## Ablauf

1. **Reel** (`reel-9-saetze.mp4`, 46 Sek.) auf Instagram + Facebook posten. Musik in Instagram selbst wählen (ruhig, Klavier/Ambient).
2. Zuschauerin kommentiert **LISTE** → bekommt automatisch eine DM.
3. DM → Link zum **Gratis-PDF** (`9-saetze-fuer-dich.pdf`) auf **Tentary** (Gratis-Produkt, sammelt die E-Mail-Adresse).
4. PDF letzte Seite → **Hero-Buch** auf Amazon.
5. Nach 24 h: 2. DM mit sanftem Buch-Hinweis.

## Was du einmal einrichten musst

| Schritt | Wo | Aufwand |
|---|---|---|
| PDF als Gratis-Produkt anlegen (Preis 0 €, E-Mail-Pflicht) | Tentary | 10 Min. |
| Kommentar-Automatisierung: Stichwort `LISTE` → DM 1 | ManyChat (mit Instagram verbinden) | 15 Min. |
| Reel posten + Caption unten | Instagram | 5 Min. |
| Link in Bio auf das Tentary-PDF | Instagram | 2 Min. |

Annahme, nicht geprüft: Die Gratis-Version von ManyChat reicht für eine Stichwort-Automatisierung. Kosten vor dem Start prüfen, ein kostenpflichtiger Plan nur mit deiner Freigabe.

## Texte

### Caption Reel

Du denkst an alle. Nur nicht an dich? 🤍

Diese 9 Sätze sind für die Tage, an denen du vergisst, dass du auch zählst.

👉 Kommentiere **LISTE** und ich schicke dir alle 9 Sätze als PDF, plus fertige Sätze, mit denen du Nein sagst, ohne dich zu rechtfertigen.

#selbstfürsorge #neinsagen #grenzensetzen #peoplepleasing #selbstwert #mentalload #schlechtesgewissen #affirmationen #selbstliebe

### Antwort auf Kommentar (öffentlich, automatisch)

Ist unterwegs zu dir 🤍 Schau in deine Nachrichten.

### DM 1 (sofort)

Hey, schön, dass du da bist 🤍
Hier sind deine 9 Sätze, mit einer Frage zu jedem Satz, Satzhilfen zum Neinsagen ohne Rechtfertigung und der Übung „Meine eigene Liste“:
👉 [Tentary-Link]

Mein Tipp: Nimm dir nur einen Satz pro Tag. Welcher trifft dich gerade am meisten?

### DM 2 (nach ca. 23 h, noch im 24-h-Fenster von Instagram)

Hast du schon in deine 9 Sätze reingeschaut? 🤍
Wenn du merkst, dass du schon sehr lange ganz unten auf deiner eigenen Liste stehst: Genau darüber habe ich ein Buch geschrieben.
„Ich stand nie auf meiner eigenen Liste“ – kurze Kapitel, Übungen, Sätze für Momente, in denen du sonst automatisch Ja sagst.
👉 amazon.de/dp/B0HGT4PX8H

### Story (am Tag nach dem Reel)

Bild 10 aus dem Karussell + Umfrage: „Welcher Satz fällt dir am schwersten? 3 / 5 / 9“ + Link-Sticker zum PDF.

## Inhalte wiederverwenden

- Karussell `outputs/2026-10-08-karussell-eigene-liste/` 3–4 Tage nach dem Reel posten, im letzten Bild dann auch „Kommentiere LISTE“.
- Gute Reaktionen später als Meta-Anzeige testen (nur mit Freigabe).

## Messen (nach 7 Tagen)

| Kennzahl | Woher |
|---|---|
| Reel-Aufrufe, Shares, Kommentare „LISTE“ | Instagram Insights |
| DMs verschickt / Link-Klicks | ManyChat |
| PDF-Downloads / E-Mails | Tentary |
| Buchverkäufe | KDP (Hinweis: Amazon-Klicks ohne Attribution-Link nicht zuordenbar → Amazon Attribution prüfen, siehe offene Punkte) |

## Variante: Persönlichkeitstest „Welcher Ja-Sager-Typ bist du?“ (für Männer und Frauen)

Datei: `ja-sager-test.html` (Vorschau: https://claude.ai/artifact/P5fGYtpjFdXEbvUMcVMxLV, privat)

- 8 Fragen, 4 Typen: Typ Fürsorge · Typ Harmonie · Typ Stärke · Typ Pflicht
- Ergebnis: Beschreibung, Prozent je Typ, „Dein Muster“, passender Satz aus den 9 Sätzen, erster Schritt für die Woche
- Danach: Gratis-Workbook (DM „LISTE“ auf Instagram) + Buch-Knöpfe (Taschenbuch Warenkorb, Kindle)
- „Ergebnis kopieren“ → Text für Story/Nachricht (Teilen = Reichweite)

Ablauf: Reel/Post „Welcher Ja-Sager-Typ bist du?“ (für Männer und Frauen) → Kommentar „TEST“ → DM mit Test-Link → Ergebnis → „LISTE“ → PDF → Buch.

Offen: Test öffentlich erreichbar machen. Die Vorschau ist privat. Die HTML-Datei funktioniert eigenständig und kann auf jede Website/Landingpage-Tool (z. B. Tentary-Seite, eigene Domain, Netlify Drop) hochgeladen werden.

## Zählung im Test (anonym)

Eingebaut über GoatCounter (keine Cookies, keine Namen). Aktiv, sobald im Test `const GOATCOUNTER='…'` eingetragen ist und der Test öffentlich läuft.
Gezählt: Aufrufe der Seite · `test/gestartet` · `test/fertig` · `test/typ-fürsorge|harmonie|stärke|pflicht` · `test/klick-whatsapp` · `test/klick-amazon` · `test/klick-instagram`.
Wer genau: nur über WhatsApp (wer das PDF anfordert).
