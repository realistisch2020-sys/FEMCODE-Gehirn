# Offene Punkte

Hier landen alle laufenden ToDos. Claude pflegt diese Datei beim `/shutdown` automatisch — erledigte Punkte raus, neue rein.

## Diese Woche

- Edith Furrers Kopie (monat-persoenlichkeitstest-4): Warenkorb-Reihenfolge unbeschriftet übernommen (Glow/Repair/Volumen/Detox/Kopfhaut/Locken hoch/Locken normal/Männerset) — bitte gegenchecken. E-Mail + Instagram fehlen, Kontaktzeile zeigt nur Telefon. Sobald ihre E-Mail da ist: auch in monat-anwendungstest-edith.html den E-Mail-Button ergänzen (aktuell nur WhatsApp + Homepage).
- In Edith Furrers Warenkorb-Links (monat-persoenlichkeitstest-4) steht als Enrollment-Name "CarolineYvonneTanner" statt Edith — evtl. ihr voller/offizieller Name, evtl. Verwechslung. Bitte kurz bestätigen.
- Die "Als VIP bestellen"-Buttons in monat-haartest-glanz.html verwenden aktuell die alten, bereits vorhandenen Enrollment-Links (Kampagne "pre_package_cart") — ich bin mir nicht sicher, ob das technisch auch deine echten VIP-Warenkorb-Links sind oder nur normale Vorbereitet-Warenkorb-Links. Bitte kurz prüfen und im Code (VIP_LINKS-Objekt, ganz oben leicht zu finden) korrigieren, falls es einen Unterschied gibt. Nebenbefund aus dem Audit (25.9.): "Mehr Volumen" und "Feines Haar" teilen sich aktuell denselben Link (…1789133994) — plausibel, da beide dieselben Produkte empfehlen, aber bitte bestätigen.
- Tracking-Feinheit (optional, aus dem Audit vom 25.9.): `product_click` fasst den großen "Produkte ansehen"-Button und die einzelnen Produkt-Links zusammen; `contact_click` fasst WhatsApp- und E-Mail-Anfrage zusammen. Für Gesamt-Interesse reicht das, für eine Kanal-Trennung in Google Ads/GTM bräuchte es je 2 eigene Event-Namen. Nur ändern, falls gewünscht.
- Beim Umbau von monat-haartest-glanz.html entfernt (war nicht Teil der neuen Vorgabe): Männer-Set-Pfad, Locken-Porositäts-Frage, VIP-Registrierung, Market-Partner-Button. Falls diese Inhalte woanders gebraucht werden (z.B. im neuen monat-typ-test.html, siehe unten), bitte Bescheid geben.
- Zweiter Link-Fragment von dir war unvollständig: `https://mymonat.com/enrollments/` ohne Rest, zusammen mit dem gültigen Market-Partner-Link geschickt — nie geklärt, wofür der gedacht war.
- Es ist am 24.9. eine weitere Claude-Session (Opus 5.5, andere Session-ID) aufgefallen, die `monat-typ-test.html` veröffentlicht hat — ein Du-Form-Persönlichkeitstest mit Kundinnen-/VIP-/Business-Wegen. Falls das eine parallele Session von dir war: gut zu wissen, dass es jetzt zwei ähnliche Tests gibt (`monat-haartest-glanz.html` neu neutral/Compliance-fokussiert, `monat-typ-test.html` spielerisch/Business-fokussiert) — evtl. bewusst als zwei Zielgruppen-Varianten gewollt, sonst ggf. abgleichen.

## Demnächst

- Klären: soll `monat-glanz/index.html` (die alte, unveränderte erste Version) neben `monat-haartest-glanz.html` (die aktiv weiterentwickelte) dauerhaft live bleiben, oder irgendwann raus?

## Ideen / später

- WhatsApp Business "Schnellantworten" (Textbausteine pro Ergebnis-Typ) einrichten — angeboten, noch keine Rückmeldung ob gewünscht.
