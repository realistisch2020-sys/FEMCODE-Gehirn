# Social Automation — Buchverkaufs-System, kein reines Posting-Tool

**Priorität: Amazon-Buchverkäufe steigern, Hauptbuch „Ich stand nie auf meiner eigenen Liste" zuerst.** Instagram/Facebook sind Verkaufs- und Vertrauenskanäle dafür, nicht Selbstzweck. MONAT (Haarpflege) ist bewusst ein komplett separates, noch nicht gebautes System — nicht vermischen.

**Status (29.09.2026):** Code fertig und funktionsfähig, läuft als Zusatzkanal neben dem Haupthebel Ads + Backmatter + E-Mail (`plans/weg-zu-50k.md`). Zwei Dinge fehlen noch bis zum ersten echten Post — siehe "Was noch fehlt" unten.

## Module

| Modul | Datei |
|---|---|
| Buch-Registry (Amazon-Links, Content-Pillars) | `books.json` |
| Hooks (Rohmaterial fürs Hauptbuch) | `data/hooks_buch1.json` |
| Content-Kalender-Builder (Hooks → geplante Posts + Bilder) | `scripts/build_content_plan.py` |
| Text-Overlay-Generator (Bild + Hook → fertiges Post-Bild) | `scripts/render_image.py` |
| Caption-Generator (KI-gestützt, für neue Themen/Bücher) | `scripts/generate_content.py` |
| Freigabe-CLI (Status-Übergänge, nichts geht ohne das live) | `scripts/approve.py` |
| Meta Publishing (Graph API) | `scripts/publish_instagram.py`, `scripts/publish_facebook.py` |
| TikTok-Export (Vorbereitung, kein Auto-Posting) | `scripts/tiktok_export.py` |
| Kommentare abholen/beantworten | `scripts/fetch_comments.py`, `scripts/reply_comments.py` |
| Log (geplant/veröffentlicht/fehlgeschlagen) | `content_queue.json` + `outputs/social-log.md` |

## Ablauf

```
build_content_plan.py   →  status: draft   (Bild bereits gerendert, Hauptformat)
generate_content.py     →  status: draft   (KI-Text für neue Themen, optional ergänzend)
        ↓
    approve.py           →  status: approved   (setzt platform + image_url, bei Reels video_url)
        ↓
publish_instagram.py     →  status: posted  |  status: failed (+ fehler-Feld)
publish_facebook.py
```

Kommentare genauso: `fetch_comments.py` → `approve.py` (draft_reply prüfen/setzen, freigeben) → `reply_comments.py`.

Jeder Post-Eintrag trägt: `datum, plattform, kategorie, buch, hook, overlay_text, caption, cta, link, status, fehler` (plus interne Felder wie `id`, `image_url`, `image_local_path`).

## Hauptformat: Bild-Posts, Reels nur optional

Instagram/Facebook: **Bild mit starkem Text-Overlay** ist das Hauptformat — kein Video-Tool, kein KI-Avatar-Dienst nötig. `render_image.py` legt den Hook-Text direkt auf ein echtes Foto (Petras Portrait oder ein thematisch passendes Bild), mit dunklem Verlauf für Lesbarkeit. Bisher zwei Quellbilder in `assets/images/` — für mehr Abwechslung im Feed sind weitere Fotos von Petra der größte Hebel.

Reels bleiben möglich (die 6 ursprünglichen Konzepte in `content_queue.json` mit `type: "reel"`), sind aber nicht der Standardweg — brauchen weiterhin einen `video_url`.

## Setup

1. `pip install -r automation/requirements.txt`
2. Secrets hinterlegen — lokal in `.env` (siehe `.env.example`, ist gitignored) oder als GitHub-Actions-Secrets:
   - `ANTHROPIC_API_KEY` — nur für `generate_content.py` (neue Themen/Bücher)
   - `IG_ACCESS_TOKEN`, `IG_BUSINESS_ACCOUNT_ID` — Anleitung: `reference/meta-setup.md`. Token läuft nach 60 Tagen ab.
   - `FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN` — fallen bei derselben Anleitung mit ab
3. Vor dem ersten Workflow-Lauf lokal testen:
   ```
   python automation/scripts/build_content_plan.py     # Kalender + Bilder erzeugen
   python automation/scripts/approve.py content list   # ansehen, was geplant ist
   python automation/scripts/tiktok_export.py           # CSV für manuellen TikTok-Upload
   ```

## Was noch fehlt, bevor der erste echte Post rausgeht

1. **Meta-Setup** (`reference/meta-setup.md`) — nur Petra kann das machen, Login-gebunden.
2. **Bild-Hosting.** Instagram/Facebook holen sich das Bild über eine öffentliche URL, keinen Datei-Upload. Die Bilder in `outputs/social-images/` haben schon die dafür vorgesehene URL eingetragen (`image_url` in `content_queue.json`, Format `https://realistisch2020-sys.github.io/FEMCODE-Gehirn/social-images/<datei>`) — **die Datei liegt dort aber noch nicht.** Dieses Repo hat schon eine GitHub-Pages-Automatisierung (`.github/workflows/deploy-pages.yml`), die den `gh-pages`-Branch deployed. Der `gh-pages`-Branch ist Petras **echte, bereits live geschaltete Website** (Persönlichkeitstest-Funnel, MONAT-Seiten) — dort ungefragt reinzupushen hätte sofort einen Live-Effekt auf ihre öffentliche Seite, deshalb ist das hier absichtlich **nicht** automatisch passiert. Empfehlung: einen `social-images/`-Unterordner im `gh-pages`-Branch anlegen (berührt nichts Bestehendes) und die Dateien aus `outputs/social-images/` dorthin kopieren — nach Petras ausdrücklicher Zustimmung.

Bis beides steht, kann alles andere (Kalender bauen, Bilder rendern, Freigeben-Workflow durchspielen) schon getestet werden — nur das tatsächliche Veröffentlichen hängt daran.

## Vor dem ersten Live-Post (Checkliste)

1. Testpost gegen einen Test-/Entwurfsmodus, nicht sofort live
2. Token-Berechtigungen prüfen (Content Publishing muss freigeschaltet sein)
3. Fehlerlogging prüfen — `content_queue.json`-Einträge mit `status: "failed"` zeigen das `fehler`-Feld
4. Posting-Zeiten testen
5. Petra bestätigt Stil und Inhalte, bevor die ersten Einträge freigegeben werden

## Wichtiger Vorbehalt: API-Details ungeprüft gegen die Live-Doku

`developers.facebook.com` war in dieser Umgebung nicht direkt abrufbar (Netzwerk blockiert die Domain). Die Endpunkte/Feldnamen in `scripts/common.py` und den Publish-/Comment-Skripten sind nach bestem Wissen aus Sekundärquellen zusammengestellt, nicht 1:1 aus der aktuellen Meta-Doku bestätigt. Vor dem ersten echten Lauf gegenchecken:
- `developers.facebook.com/docs/instagram-platform/content-publishing`
- `developers.facebook.com/docs/marketing-api/reference/instagram-comment/replies`

Ein Fehler wie "Unknown fields" oder ein 400 bei den ersten Testläufen ist meist ein falscher Feld-/Endpunktname — kein grundsätzliches Problem am Aufbau.

## Was hier bewusst fehlt / bewusst nicht erzwungen wird

- **TikTok-Auto-Posting**: nur Export vorbereitet (`tiktok_export.py`), kein Live-Posting — TikToks API ist restriktiver, erst prüfen, wenn ein sauberer Zugang möglich ist.
- **Facebook Reels** (natives Reels-Tab): `publish_facebook.py` postet Videos über die einfache `/videos`-Route, nicht über die Chunked-Upload-API fürs Reels-Tab.
- **Ads/Marketing API**: bewusst nicht Teil dieses Bausteins.
- **MONAT**: separates System, eigene Zielgruppe/Sprache/Links/Compliance — kommt später, nicht hier mit reinmischen.
- **Keine Tokens hardcoden oder im Chat ausgeben.** Immer über `.env`/GitHub-Secrets.
