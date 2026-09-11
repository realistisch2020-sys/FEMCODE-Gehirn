# Social Automation

Organischer Teil von Baustein 4 aus `plans/automatisierung-social-media.md`: Entwürfe erzeugen, freigeben, veröffentlichen, Kommentare abholen und beantworten. Alles läuft über zwei Warteschlangen mit einem Freigabe-Schritt dazwischen — **nichts geht live, ohne dass jemand `approve.py` benutzt hat.**

## Ablauf

```
generate_content.py  →  status: draft
        ↓
    approve.py        →  status: approved   (setzt platform + video_url)
        ↓
publish_instagram.py  →  status: posted
publish_facebook.py
```

Kommentare genauso: `fetch_comments.py` → `approve.py` (draft_reply prüfen/setzen, freigeben) → `reply_comments.py`.

## Setup

1. `pip install -r automation/requirements.txt`
2. Secrets als GitHub-Actions-Secrets hinterlegen (Repo → Settings → Secrets and variables → Actions):
   - `ANTHROPIC_API_KEY` — für die Content-Generierung
   - `IG_ACCESS_TOKEN`, `IG_BUSINESS_ACCOUNT_ID` — aus dem Meta-Setup (Baustein 3 in `plans/automatisierung-social-media.md`). Token läuft nach 60 Tagen ab.
   - `FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN` — dieselbe Meta-App deckt das ab
3. Vor dem ersten Workflow-Lauf lokal testen:
   ```
   export ANTHROPIC_API_KEY=...
   python automation/scripts/generate_content.py buecher --count 2
   python automation/scripts/approve.py content list
   ```

## Manuell auslösen

GitHub → Actions → "Social Media Automatisierung" → "Run workflow". Solange Secrets fehlen, brechen die Publish-/Comment-Schritte kontrolliert mit einer Fehlermeldung ab (kein stiller Fehlschlag).

## Automatisch laufen lassen

Der `schedule`-Trigger in `.github/workflows/social-automation.yml` ist bewusst auskommentiert, bis Baustein 3 (Meta-Zugänge) steht — sonst schlägt der Job jeden Tag sichtbar fehl. Einkommentieren, sobald die Secrets oben gesetzt sind.

## Wichtiger Vorbehalt: API-Details ungeprüft gegen die Live-Doku

`developers.facebook.com` war in dieser Umgebung nicht direkt abrufbar (Netzwerk blockiert die Domain). Die Endpunkte/Feldnamen in `scripts/common.py` und den Publish-/Comment-Skripten sind nach bestem Wissen aus Sekundärquellen zusammengestellt, nicht 1:1 aus der aktuellen Meta-Doku bestätigt. Vor dem ersten echten Lauf gegenchecken:
- `developers.facebook.com/docs/instagram-platform/content-publishing`
- `developers.facebook.com/docs/marketing-api/reference/instagram-comment/replies`

Ein Fehler wie "Unknown fields" oder ein 400 bei den ersten Testläufen ist meist ein falscher Feld-/Endpunktname — kein grundsätzliches Problem am Aufbau.

## Was hier bewusst fehlt

- **Video-Erstellung** (Baustein 2): `video_url` muss beim Freigeben manuell gesetzt werden, bis eine Entscheidung für Option A/B/C steht.
- **Facebook Reels** (natives Reels-Tab): `publish_facebook.py` postet Videos über die einfache `/videos`-Route, nicht über die Chunked-Upload-API fürs Reels-Tab — reicht für "Video auf der Page", nicht für denselben Feed wie Instagram Reels.
- **Ads/Marketing API**: bewusst nicht Teil dieses Bausteins, siehe Reihenfolge in `plans/automatisierung-social-media.md`.
- **TikTok**: kommt in Phase 2.
