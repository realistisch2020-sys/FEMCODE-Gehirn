# Einrichtung: Impact-Fragen-Bot

## Was der Bot macht

- Schickt dir **jeden Samstag um 12:00 Uhr** genau 10 Fragen deiner Zielgruppe
- Verteilt die Fragen über 7 Kategorien (Haare, Geld, Schlaf, Emotionen, Loslassen, Zyklus, Systeme)
- Befehl `/fragen` → sofort 10 Fragen abrufen, wann immer du willst

---

## Einrichtung (einmalig, ca. 15 Minuten)

### Schritt 1 – Bot bei Telegram erstellen

1. Öffne Telegram → suche **@BotFather**
2. Sende `/newbot`
3. Name eingeben: z. B. `Impact Fragen Bot`
4. Benutzername eingeben (muss auf „bot" enden): z. B. `impactfragenbot`
5. BotFather gibt dir einen **API-Token** – sicher kopieren

### Schritt 2 – Token eintragen

Öffne `bot.py`, Zeile 16:
```python
BOT_TOKEN = "DEIN_BOT_TOKEN_HIER"
```
Ersetze `DEIN_BOT_TOKEN_HIER` durch deinen echten Token.

### Schritt 3 – Chat-ID herausfinden

1. Bot installieren und starten (Schritt 4)
2. Schreibe deinem Bot `/start` auf Telegram
3. Der Bot antwortet mit deiner Chat-ID
4. Diese ID in `bot.py` Zeile 17 eintragen:
```python
CHAT_ID = "123456789"
```

### Schritt 4 – Bot auf deinem Computer/Server starten

```bash
# Python-Pakete installieren
pip install -r requirements.txt

# Bot starten
python bot.py
```

---

## Dauerhaft laufen lassen (empfohlen)

Damit der Bot auch läuft, wenn du deinen Computer zumachst, braucht er einen Server.

**Einfachste Option: Railway.app (kostenlos)**
1. Gehe zu [railway.app](https://railway.app)
2. Neues Projekt → „Deploy from GitHub" oder manuell
3. Dateien hochladen: `bot.py`, `fragen.py`, `requirements.txt`
4. Umgebungsvariablen setzen: `BOT_TOKEN` und `CHAT_ID`
5. Deployment starten → Bot läuft 24/7

**Alternative: PythonAnywhere (kostenlos)**
1. Account auf [pythonanywhere.com](https://pythonanywhere.com) erstellen
2. Dateien hochladen
3. „Always-on task" einrichten

---

## Zeitzone beachten

Der Bot ist auf **10:00 UTC** eingestellt = **12:00 Uhr Schweizer Sommerzeit (CEST)**.

Im Winter (MEZ = UTC+1): Nachricht kommt um 11:00 Uhr.
→ Dann `bot.py` Zeile 38 auf `"11:00"` ändern.

---

## Fragen anpassen

Alle Fragen stehen in `fragen.py`. Du kannst jederzeit:
- Neue Fragen hinzufügen
- Kategorien ergänzen (z. B. „Ernährung", „Beziehungen")
- Fragen entfernen, die nicht mehr passen

---

## Befehle im Bot

| Befehl | Funktion |
|--------|----------|
| `/start` | Bot starten, Chat-ID anzeigen |
| `/fragen` | Sofort 10 Fragen abrufen |
