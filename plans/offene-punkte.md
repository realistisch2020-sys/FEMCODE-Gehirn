# Offene Punkte

Hier landen alle laufenden ToDos. Claude pflegt diese Datei beim `/shutdown` automatisch — erledigte Punkte raus, neue rein.

## Diese Woche

- Posting-Engine (Baustein 4, organisch) ist gebaut: `automation/` — generieren → freigeben → posten/beantworten, siehe `automation/README.md`. Läuft noch nicht automatisch, nur manuell per GitHub Actions.
- Blocker für echten Content: `context/business.md` füllen (Bücher, Produkte, Zielgruppe, Preise) — ohne das verweigert `generate_content.py` bewusst den Lauf
- Video-Produktion Baustein 2: Option A/B/C wählen (siehe `plans/automatisierung-social-media.md`) — bis dahin muss `video_url` bei jedem Post von Hand gesetzt werden

## Demnächst

- Meta-Setup (Instagram+Facebook App/Token) machen, dann als Secrets hinterlegen (Liste in `automation/README.md`)
- API-Feldnamen in `automation/scripts/` einmal gegen die aktuelle Meta-Doku gegenchecken (konnte hier nicht direkt abgerufen werden)
- Danach: `schedule`-Trigger im Workflow einkommentieren
- Später: Ads-Layer + TikTok (Baustein 6)

## Ideen / später

- (noch nichts)
