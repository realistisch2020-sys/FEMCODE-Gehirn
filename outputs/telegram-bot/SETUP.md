# Einrichtung: Impact-Fragen-Bot

## Was der Bot macht

- Schickt dir **jeden Samstag um 12:00 Uhr** 10 frische Fragen deiner Zielgruppe
- Die Fragen werden wöchentlich **neu generiert** (via Claude AI) – kein fixer Pool
- Befehl `/fragen` → sofort 10 aktuelle Fragen abrufen, wann du willst

---

## Tokens sicher übergeben – NIEMALS in den Chat schreiben

Du brauchst drei Schlüssel. Alle werden als **Umgebungsvariablen** gesetzt –
niemals in eine Datei oder in einen Chat eingefügt.

| Variable          | Woher                        |
|-------------------|------------------------------|
| `BOT_TOKEN`       | @BotFather auf Telegram      |
| `CHAT_ID`         | nach `/start` im Bot         |
| `ANTHROPIC_API_KEY` | console.anthropic.com       |

---

## Einrichtung Schritt für Schritt

### Schritt 1 – Telegram Bot erstellen

1. Öffne Telegram → suche **@BotFather**
2. Sende `/newbot`
3. Name eingeben: z. B. `Impact Fragen Bot`
4. Benutzername (muss auf „bot" enden): z. B. `impactfragenbot`
5. BotFather gibt dir deinen **BOT_TOKEN** – nur für dich, sicher aufbewahren

### Schritt 2 – Anthropic API Key holen

1. Gehe zu [console.anthropic.com](https://console.anthropic.com)
2. Account erstellen (kostenloser Einstieg verfügbar)
3. „API Keys" → „Create Key"
4. Key kopieren und sicher speichern (nur einmal sichtbar)

### Schritt 3 – Bot auf Railway.app deployen (empfohlen, kostenlos)

Railway ist eine Plattform, auf der der Bot dauerhaft läuft – kein eigener Server nötig.

1. Gehe zu [railway.app](https://railway.app) → Account mit GitHub erstellen
2. „New Project" → „Deploy from GitHub" → diesen Ordner verbinden
   *(oder: „Empty Project" → Dateien manuell hochladen)*
3. Im Railway-Dashboard: **„Variables"** öffnen
4. Drei Variablen eintragen (hier sind Tokens sicher):

```
BOT_TOKEN       = [dein Token von BotFather]
CHAT_ID         = [wird nach Schritt 4 bekannt]
ANTHROPIC_API_KEY = [dein Key von Anthropic]
```

5. Deployment starten

### Schritt 4 – Chat-ID herausfinden

1. Suche deinen Bot auf Telegram (z. B. `@impactfragenbot`)
2. Schreibe `/start`
3. Bot antwortet mit deiner Chat-ID
4. Diese ID in Railway unter `CHAT_ID` nachtragen → Bot neu starten

---

## Zeitzone

Bot ist auf **10:00 UTC** eingestellt = **12:00 Uhr Schweizer Sommerzeit (CEST)**

Winter (MEZ, November–März): Nachricht kommt um 11:00 Uhr.
→ Dann in `bot.py` Zeile `time(hour=10)` auf `time(hour=11)` ändern.

---

## Befehle im Bot

| Befehl | Funktion |
|--------|----------|
| `/start` | Bot starten, Chat-ID anzeigen |
| `/fragen` | Sofort 10 frische Fragen generieren |

---

## Kosten

| Dienst | Kosten |
|--------|--------|
| Railway.app | Kostenlos (Hobby-Plan) |
| Anthropic API | ~0.01–0.03 CHF pro Woche |
| Telegram Bot | Kostenlos |

Der Bot kostet dich praktisch nichts.
