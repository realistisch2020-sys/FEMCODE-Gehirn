# Automatisierung Social Media (Insta / Facebook / TikTok)

Vollständige Bestandsaufnahme: was für ein komplettes Automatisieren nötig ist — Reels/Posts organisch UND bezahlte Werbung, für zwei Content-Spuren (Bücher / Produkte+Business). Nicht der Kurs von der Werbeanzeige — das hier ist die echte Umsetzung.

Start: Instagram + Facebook zusammen (eine Meta-App deckt beide ab). TikTok später.

## Die 4 Bausteine

1. **Content (Text)** — kann ich automatisieren
2. **Video/Bild** — kann ich NICHT allein automatisieren
3. **Plattform-Zugänge** — musst du selbst einrichten (deine Identität, deine Logins)
4. **Automatisierungs-Engine** — baue ich, sobald 1–3 stehen

Baustein 2 und 3 sind die eigentlichen Hürden. Baustein 1 und 4 sind für mich reine Fleißarbeit.

---

## Baustein 1: Content-Erstellung (übernehme ich)

Zwei getrennte Content-Spuren, je mit eigenem Ton und Zielgruppe:
- **Bücher**: Hooks, Skripte, Captions, Hashtags rund um deine Buchthemen
- **Produkte/Business**: dasselbe für dein laufendes Angebot

Pro Reel/Post liefere ich: Hook (erste 2 Sek.), Skript/Talking Points, Caption, Hashtag-Set, CTA. Das läuft nach einem festen monatlichen Rhythmus (z. B. X Reels/Woche pro Spur), gespeichert in `outputs/`.

Voraussetzung: `context/business.md` muss gefüllt sein (Buchtitel, Themen, Zielgruppe, Angebot, Preise) — aktuell noch leer. Ohne das sind alle Texte generisch.

## Baustein 2: Video/Bild-Produktion (größte offene Frage)

Ich kann Skripte schreiben, aber kein fertiges Reel-Video erzeugen. Drei Optionen:

- **A — Du filmst, ich schreibe.** Du lieferst Rohclips (Talking-Head, Buch-Flatlays, B-Roll), ich liefere Skript + Schnitt-Anweisung + Caption. Wenig Automatisierung, aber sofort machbar.
- **B — Template-Video-Tool.** Text-over-B-Roll automatisiert zusammenbauen (z. B. mit Stockfootage + Untertiteln). Mittlerer Aufwand, braucht ein zusätzliches Tool/API und etwas Bildmaterial-Vorrat.
- **C — KI-Avatar/Video-Generator.** Ein separater Dienst erzeugt aus dem Skript ein fertiges Video (Avatar spricht den Text). Am meisten "komplett automatisch", aber zusätzliche Kosten + ein weiterer Account/API, den du einrichten musst — das ist kein Anthropic/Claude-Produkt, sondern ein Drittanbieter.

Ohne Entscheidung hier bleibt die Automatisierung bei "Text fertig, Video von Hand".

## Baustein 3: Plattform-Zugänge (das machst du, nicht ich)

Das kann ich nicht für dich erledigen — Tokens und App-Zugänge hängen an deinem Login und deiner Identität. Ich schreibe dir die exakten Schritte, aber du klickst sie in deinem Meta-Account durch (im Prinzip die 9 Schritte aus der Anzeige, die du mir gezeigt hast):

- **Instagram + Facebook**: Creator/Business-Konto → Meta-Entwicklerportal → eigene App → Zugriffsschlüssel → 60-Tage-Token. Eine App deckt beide Plattformen ab.
- **TikTok** (Phase 2): eigener Entwickler-Account + Content-Posting-API-Freigabe — kann Tage bis Wochen dauern, strenger als Meta.
- **Werbekonten** (für den bezahlten Teil): Meta Ads Manager (Werbekonto + Zahlungsmittel) und später TikTok Ads Manager — beides zusätzlich zu den normalen API-Zugängen oben.

Tokens/App-Geheimnisse sind wie Passwörter: die kommen in Secrets (z. B. GitHub Actions Secrets), nie in den Chat oder ins Repo.

## Baustein 4: Automatisierungs-Engine (baue ich)

Sobald 1–3 stehen, baue ich in diesem Repo einen geplanten Job (GitHub Actions, läuft bereits fürs Pages-Deploy):

- **Organisch**: Content-Plan aus Baustein 1 → zur richtigen Zeit posten (Graph API)
- **Kommentare**: neue Kommentare abholen, Standardantworten automatisch, alles Heikle/Negative eskalieren statt automatisch beantworten
- **Ads-Layer**: Kampagnen/Anzeigen über die Marketing-API erstellen — hier empfehle ich einen Freigabe-Schritt vor Go-Live, bis sich das System bewährt hat. Echtes Geld ohne Kontrolle rauslassen ist der Teil, wo ein Fehler am meisten kostet.
- Jeder Lauf protokolliert, was gepostet/beantwortet/geschaltet wurde, in `outputs/`

## Laufende Kosten (Realitätscheck)

- Claude API für die Textgenerierung (gering)
- Ggf. Video-Tool/Avatar-API, falls Option B/C (Baustein 2) — variiert stark
- Werbebudget selbst (kommt on top, das ist deine Mediaspend-Entscheidung, nicht Teil der "Automatisierung")
- IG-Token muss alle 60 Tage erneuert werden — dafür baue ich eine Erinnerung/einen Refresh-Job ein

## Empfohlene Reihenfolge

1. `context/business.md` füllen (Bücher, Produkte, Zielgruppe, Preise)
2. Content-System bauen (Baustein 1) — läuft ohne jeden API-Zugang, sofort nutzbar
3. Meta-Setup machen (Baustein 3, Insta+Facebook)
4. Posting-Engine anschließen (Baustein 4, organisch)
5. Kommentar-Antworten dazu
6. Erst danach: Ads-Layer + TikTok — mehr bewegliche Teile, mehr Risiko (Geld, Freigaben)

## Offen

- Entscheidung Baustein 2 (A/B/C)
- Buch- und Produktinfos für `context/business.md`
- Wann Meta-Setup (Baustein 3) angehen
