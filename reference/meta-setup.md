# Meta-Setup: Instagram + Facebook Zugänge

Ziel: die vier Werte, die `automation/` als Secrets braucht — `IG_ACCESS_TOKEN`, `IG_BUSINESS_ACCOUNT_ID`, `FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN`.

**Das hier machst nur du.** Hängt an deinem Facebook-/Instagram-Login — kann ich nicht für dich klicken, und App-Geheimnis/Token sind wie ein Passwort (nie in den Chat einfügen, nie committen).

## Voraussetzung

Instagram-Konto als Profi-Konto (Creator oder Business), verknüpft mit einer Facebook-Seite:
- Instagram-App → Einstellungen → Konto → zu professionellem Konto wechseln
- Bei der Einrichtung (oder später unter Einstellungen → Verknüpfte Konten) mit einer Facebook-Seite verbinden — ohne Page geht der API-Zugriff nicht

## Schritt für Schritt

1. **App anlegen** — developers.facebook.com → Meine Apps → App erstellen → Typ "Business". Name ist egal.
2. **Instagram-Produkt hinzufügen** — im App-Dashboard "Instagram" als Produkt einrichten (Meta nennt das gelegentlich um, z. B. "Instagram-API mit Instagram-Login" — folge der Beschriftung im Dashboard).
3. **App-Zugangsdaten notieren** — App-Einstellungen → Basic → App-ID und App-Geheimnis.
4. **Dich selbst als Tester eintragen** (nötig, solange die App nicht von Meta review-geprüft ist) — App-Rollen → Rollen → Personen hinzufügen → Instagram-Tester → deinen Instagram-Namen eintragen. Status wird "Pending".
5. **Einladung annehmen** — auf instagram.com einloggen → Profil bearbeiten → Apps und Websites → Tester-Einladungen → annehmen. Status wechselt im Entwicklerportal auf "Active".
6. **Token erzeugen** — im Entwicklerportal über den Graph-API-Explorer bzw. die verlinkte API-Setup-Seite: deine App + Seite auswählen, Berechtigungen anhaken: `pages_show_list`, `pages_read_engagement`, `pages_manage_posts`, `instagram_basic`, `instagram_content_publish`, `instagram_manage_comments` → Token generieren.
7. **Kurzlebigen gegen 60-Tage-Token tauschen**:
   ```
   curl -s "https://graph.facebook.com/v21.0/oauth/access_token\
   ?grant_type=fb_exchange_token\
   &client_id=DEINE_APP_ID\
   &client_secret=DEIN_APP_GEHEIMNIS\
   &fb_exchange_token=DEIN_KURZER_TOKEN"
   ```
   Antwort enthält `access_token` — das ist der lange Token, gültig 60 Tage.
8. **Facebook Page ID + Page Access Token holen**:
   ```
   curl -s "https://graph.facebook.com/v21.0/me/accounts?access_token=DEIN_LANGER_TOKEN"
   ```
   Antwort ist eine Liste deiner Seiten mit `id` (→ `FB_PAGE_ID`) und `access_token` (→ `FB_PAGE_ACCESS_TOKEN`).
9. **Instagram Business Account ID holen**:
   ```
   curl -s "https://graph.facebook.com/v21.0/FB_PAGE_ID?fields=instagram_business_account&access_token=FB_PAGE_ACCESS_TOKEN"
   ```
   Antwort: `instagram_business_account.id` → `IG_BUSINESS_ACCOUNT_ID`.
10. **Testen**:
    ```
    curl -s "https://graph.facebook.com/v21.0/IG_BUSINESS_ACCOUNT_ID?fields=username&access_token=IG_ACCESS_TOKEN"
    ```
    Antwort sollte deinen Instagram-Namen zeigen. Als `IG_ACCESS_TOKEN` reicht normalerweise derselbe Page-Access-Token aus Schritt 8.

## In GitHub hinterlegen

Repo → Settings → Secrets and variables → Actions → New repository secret — für jeden der vier Werte oben plus `ANTHROPIC_API_KEY`. Nie im Klartext committen.

## Token-Ablauf

60 Tage ab Ausstellung. Vor Ablauf erneuern: Schritt 7 mit dem noch gültigen Token wiederholen, verlängert um weitere 60 Tage. Einmal abgelaufen heißt von vorne. Empfehlung: Erinnerung auf Tag 50 stellen.

## Wenn ein Schritt anders aussieht

Metas Entwicklerportal ändert Bezeichnungen und Klickpfade öfter. Die Konzepte und API-Aufrufe oben sind stabil, auch wenn ein Button gerade anders heißt — im Zweifel dem folgen, was im Dashboard tatsächlich steht.
