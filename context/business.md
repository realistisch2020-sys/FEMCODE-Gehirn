# Mein Business

Hier kommt rein, womit du Geld verdienst und für wen. Damit kann Claude Content, Angebote und Texte wirklich in deinem Kontext bauen.

## Was ich anbiete

Zwei Standbeine:
1. **Safe to Thrive** — eigene Self-Help-Bücher (Amazon) + 1:1-Online-Sitzungen zum jeweiligen Thema.
2. **MONAT** — Haarpflege-Produkte als Beraterin, plus eigenes Team (andere Beraterinnen), für das ich gleichartige Lead-Funnel-Seiten mit deren eigenen Kontakt-/Shop-Daten aufsetze. Drei Seitentypen: Haar-Typ-Test, Business-Typ-Test (Rekrutierung ins Team) und zeitlich befristete VIP-Aktions-Landingpages (Countdown, Paket-Angebote) — von den Tests existieren auch mehrere Design-Varianten parallel (gleiche Daten, unterschiedlicher Look).

Beide laufen über denselben Mechanismus: ein interaktiver Quiz auf einer eigenen Seite (GitHub Pages), Ergebnis + Buch-/Produkt-Empfehlung, WhatsApp als Kontaktkanal.

## Wichtig: Live-Links nie über Kreuz verändern

Es gibt viele ähnlich benannte Quiz-Seiten (Safe-to-Thrive-Persönlichkeitstest, mehrere MONAT-Haartest-Varianten, `glow-typ-test.html` für MONAT Gloss Mode™ Warteliste, `monat-detox-test/` für die Detox-Phase, `monat-anwendungstest.html` für die Produkt-Anwendung). Jede ist eigenständig. Arbeit an einer Seite (z.B. Persönlichkeitstest) darf nie eine andere live Seite oder deren Link verändern — auch nicht aus Versehen wegen ähnlichem Namen/Aufbau.

Team-Kopien für andere Beraterinnen: gleicher Seiteninhalt, aber deren eigene Kontakt-/Shop-Daten (WhatsApp, E-Mail, mymonat.com-Subdomain). Bei "Kopie für [Name]"-Anfragen zuerst in bestehenden Seiten nach den echten Daten der Person suchen, nicht neu fragen oder erfinden. Fehlt ein Feld dort auch (z.B. keine E-Mail hinterlegt), in der Kopie einfach weglassen statt erfinden.

Bereits bekannte Original-Kontaktdaten:
- Angela Gross → `monat-persoenlichkeitstest-2/index.html`, auch `monat-anwendungstest-angela.html`
- Monika Gessler → `monat-persoenlichkeitstest-3/index.html`, auch `monat-anwendungstest-monika.html`
- Edith Furrer → `monat-persoenlichkeitstest-4/index.html`, auch `monat-anwendungstest-edith.html` (keine E-Mail/Instagram hinterlegt)
- Monika Duhme → `monat-haartest-monika-duhme.html` (Glanz-Test-Stil, siehe unten)
- Andrea Klaus, Coiffeur Haar-Lay → `monat-haartest-andrea-klaus.html` (Glanz-Test-Stil, siehe unten)

### Team-Kopien im Glanz-Test-Stil (seit Monika Duhme/Andrea Klaus)

Vorlage ist `monat-haartest-glanz.html` (Quiz, 5 Ergebnisse: trockenes-haar/kopfhaut/frizz/volumen/feines-haar) — eigene Dateien `monat-haartest-[name].html`, nicht die Anwendungstest-Vorlage. Pro Person brauche ich: Name, WhatsApp, E-Mail (optional), Instagram (optional), MONAT-Shop-Link, ggf. eigener Business-Name statt "Unabhängige MONAT Markenpartnerin" im Footer/Badge. Fehlt ein Feld, weglassen statt erfinden.

Plus Warenkorb-Links: 5 Stück, einer pro Ergebniskategorie (volumen+feines-haar nur teilen, wenn sie das wie bei sich selbst so will — nicht automatisch annehmen). Optional 2 Marketpartner-Links (Kampagne `..._mp`) für einen Zusatz-Block "Werde Teil meines Teams", optional weitere Einzel-Links (z.B. "Männerset") als zusätzliche Buttons unter "Fertige Sets direkt bestellen" — Beschriftung dafür erfragen, nicht raten.

Nur Links im Format `enrollments/<id>/share?...&utm_campaign=pre_package_cart` funktionieren als Warenkorb-Link. Das Format `shop/orders/<id>/share` ist ungültig (führt zu MONATs eigener Fehlerseite "this page flaked out like drugstore shampoo") — bei diesem Format nachfragen/neue Links erbitten, nicht verwenden.

Immer ohne GTM (Kopf-Script + Noscript-Block entfernen). Bei unbeschrifteten Linklisten: Reihenfolge wie zuletzt mit ihr abgestimmt übernehmen (aktuell: trockenes-haar, kopfhaut, frizz, volumen, feines-haar), aber kurz bestätigen lassen statt stillschweigend anzunehmen.

Veröffentlicht wird erst auf expliziten Wunsch ("Link zum Weitergeben/Rauskopieren" o.ä.) — vorher nur Artifact-Vorschau + Datei zum Prüfen.

## MONAT-Quiz-Vorlage: visueller Standard

Die MONAT-Test-Seiten teilen sich einen Effekt-Baukasten (Glitzer-Canvas, Konfetti, 3D-Emblem, drehende Icon-Badges, Buttons die beim Klick wackeln/Farbe zeigen). Lieber zu viel Bewegung/Effekte als zu wenig einsetzen.

## MONAT-Compliance-Standard (seit Haartest-Umbau)

`monat-haartest-glanz.html` läuft jetzt nach strengeren Regeln, weil sie als Google-Ads-Funnel gedacht ist:
- Sie-Form, neutraler Name, kein Anschein eines offiziellen MONAT-Tests
- Keine medizinischen Aussagen/Heilversprechen (auch nicht "stoppt/behandelt Haarausfall", "heilt", "regeneriert Haarfollikel" o.ä.) — Haarausfall-Anfragen verweisen auf Arzt/Fachperson statt Test-Ergebnis
- Footer mit "Petra Tanner | Unabhängige MONAT Markenpartnerin" + Orientierungs-Disclaimer
- Keine Countdown/künstliche Verknappung/erfundene Bewertungen
- Tracking-Events einheitlich: `test_started`, `test_completed`, `result_<kategorie>`, `product_click`, `contact_click`
- Ergebnisseiten per Sprungmarke direkt erreichbar (`#kategorie-name`) für Google-Ads-Deep-Links
Bei künftigen MONAT-Funnel-Anfragen zuerst nachfragen, ob dieser strengere Standard gelten soll (falls nicht ausdrücklich gesagt).

Pro Ergebnis gibt es jetzt zwei Buttons: "Als VIP bestellen" (primär, führt zum passenden Enrollment-/VIP-Warenkorb-Link) + "Produkte ansehen" (sekundär, zum allgemeinen Shop). Die VIP-Links liegen im Code als `VIP_LINKS`-Objekt (ein Link pro Ergebniskategorie), extra als einfach austauschbare Variable angelegt — Petra kann sie selbst ersetzen, sobald sie die aktuellen offiziellen Links hat. Kaufabschluss immer auf der offiziellen MONAT-Seite.

## Meine Zielgruppe

Safe to Thrive: Menschen mit Mustern wie Schuldgefühlen, Beziehungs-Erschöpfung, unsichtbarer Erschöpfung, People Pleasing, Reizbarkeit/Nervensystem-Themen.
MONAT: Interessierte an Haarpflege, angesprochen über Instagram/WhatsApp/Facebook via Haartyp-Test.

## Meine Kanäle

Instagram, Facebook, WhatsApp — Tests/Quizzes als Einstieg, geteilt auch über eigene Kurzlinks (tinyurl).

## Meine Angebote und Preise

(noch nichts)

Kurz halten. Genug damit Claude dich versteht, kein vollständiges Wiki.
