# CLAUDE.md - Dein FEMCODE Gehirn

Claude liest diese Datei bei jedem Start zuerst. Sie sagt in wenigen Zeilen, wer du bist und wie hier gearbeitet wird. Sie muss nicht sofort perfekt sein. Sie wächst mit dir.

## Wer ich bin

- Name:
- Was ich mache:
- Für wen:

Mehr in `context/ueber-mich.md` und `context/business.md`.

## Aufbau

- `context/` alles über mich und mein Business, wird beim Start gelesen
- `plans/` Pläne und offene Punkte
- `outputs/` fertige Ergebnisse (Texte, Posts, Mails, Bilder)
- `reference/` Vorlagen und Beispiele

## Befehle

### /start

Wenn ich `/start` schreibe, mach Folgendes:

1. Lies in dieser Reihenfolge:
   - `CLAUDE.md` (diese Datei)
   - Alle Dateien im Ordner `context/`
   - `plans/offene-punkte.md` (falls vorhanden)

2. Begrüße mich danach mit meinem Namen (steht in `context/ueber-mich.md` unter "Name:"):
   "Hey [Name]! Woran arbeiten wir heute?"
   Falls noch kein Name eingetragen ist: "Hey! Woran arbeiten wir heute?"

3. Kein Statusbericht ungefragt. Wenn ich einen Überblick will, sag kurz:
   - 1-2 Punkte aus `plans/offene-punkte.md`
   - Sonst nichts vorab — ich gebe die Richtung vor.

4. Halte dich kurz, klar und direkt. Keine KI-Floskeln.

### /shutdown

Wenn ich `/shutdown` schreibe, mach Folgendes:

1. **Erkenntnisse direkt einarbeiten:** Neue Infos über mich oder mein Business, die in dieser Session aufgekommen sind, SOFORT in die passende Datei in `context/` schreiben (Datei anlegen, falls noch nicht vorhanden).
   WICHTIG: Gespeichert wird die destillierte Lehre / Regel / das Wording. Nicht der einmalige Rohinhalt.

2. **Konkrete Outputs** (fertige Texte, Posts, Mails, Bilder) gehören nach `outputs/`, nicht in `context/`.

3. **Offene Punkte:** In `plans/offene-punkte.md` aktualisieren (Datei anlegen, falls noch nicht da). Erledigte Punkte raus, neue rein. Bei unklarem Status: drin lassen, nicht raten.

4. **Abschluss-Meldung im Chat, kurz und konkret:**

   Session abgeschlossen.
   - Eingearbeitet: <welche Dateien aktualisiert>
   - Offene Punkte: <Anzahl + Tendenz>
   - Nächster Schritt: <eine Sache>

## So arbeitest du mit mir

- Einfach erklären, kein Fachjargon ohne Erklärung
- Bei Unklarheit nachfragen statt raten
- Tokenfreundlich: kurz, klar, keine Wiederholungen
- Immer den einfachsten Weg wählen
- Vor größeren Aufgaben kurz überlegen, wie der beste Output aussieht, und mir den Vorschlag nennen
- **WICHTIG: Niemals Vorschläge machen ohne vorherige Recherche.** Keine Gruppen, Links, Namen, Plattformen oder Strategien nennen, die nicht zuerst recherchiert und verifiziert wurden. Wenn unsicher: erst recherchieren, dann antworten.

## Speichern (wichtig)

- Neue Infos über mich oder mein Business sofort in die passende `context/`-Datei schreiben
- Wichtige Ergebnisse einer Session laufend in `outputs/` oder die passende Datei sichern, nicht erst am Ende
- Auch zwischendurch regelmäßig speichern, damit nichts verloren geht, falls eine Session abbricht
- `/shutdown` ist die letzte Sicherung, nicht die einzige
