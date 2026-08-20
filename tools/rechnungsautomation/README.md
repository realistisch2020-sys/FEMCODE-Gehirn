# Rechnungsautomation Fernhilfe

Erstellt jeden Sonntag automatisch Rechnungs-Entwürfe (Schweizer QR-Rechnung, PDF)
für alle Kunden, die in der kommenden Woche fällig sind — egal ob monatlich,
alle 3 oder alle 6 Monate. Du prüfst die PDFs und verschickst sie selbst.

## Einmalige Einrichtung

1. Pakete installieren:
   ```
   pip3 install -r requirements.txt
   ```

2. `config_vorlage.py` kopieren zu `config.py` und ausfüllen (Name, Adresse, IBAN).
   `config.py` wird **nicht** in git gespeichert — deine Bankdaten bleiben lokal.

3. `kunden_vorlage.csv` kopieren zu `kunden.csv` und deine echten Kunden eintragen.
   Auch `kunden.csv` wird nicht in git gespeichert.

   Spalten:
   - `Rhythmus`: `monatlich`, `3 monate` oder `6 monate`
   - `Start`: Datum der **nächsten fälligen** Rechnung (nicht das ursprüngliche
     Kundenstart-Datum — sonst holt das Skript beim ersten Lauf alle
     vergangenen Perioden nach!)
   - `Letzte_Rechnung`: leer lassen bei neuen Kunden. Wenn du für einen
     bestehenden Kunden schon manuell eine Rechnung gestellt hast, trag hier
     deren Datum ein — das Skript rechnet dann korrekt ab dort weiter.
   - `Referenz_ID`: nur nötig, falls deine IBAN eine QR-IBAN ist (`IST_QR_IBAN = True`
     in config.py). Einfach eine fortlaufende Kundennummer, z.B. 1001, 1002, ...
   - `Aktiv`: `JA`/`NEIN` — mit `NEIN` pausierst du einen Kunden, ohne die Zeile
     zu löschen.

## Benutzung

Testlauf (zeigt nur an, was passieren würde, ändert nichts):
```
python3 rechnungslauf.py --dry-run
```

Echter Lauf (erstellt PDFs in `entwuerfe/`, aktualisiert `kunden.csv` und
schreibt ins `protokoll.csv`):
```
python3 rechnungslauf.py
```

Testen mit einem anderen Datum:
```
python3 rechnungslauf.py --datum 2026-08-23 --dry-run
```

Die erstellten PDFs landen in `entwuerfe/JJJJ-MM-TT_kundenname.pdf`.

## Wöchentliche Automatisierung (jeden Sonntag)

Läuft lokal auf deinem Rechner — deine Kundendaten und Bankdaten bleiben so
bei dir, keine Cloud nötig.

**Mac/Linux (cron):**
```
crontab -e
```
Zeile einfügen (läuft jeden Sonntag um 8 Uhr):
```
0 8 * * 0 cd /pfad/zu/tools/rechnungsautomation && /usr/bin/python3 rechnungslauf.py >> lauf.log 2>&1
```

**Windows (Task-Planer):**
1. Taskplaner öffnen → "Aufgabe erstellen"
2. Trigger: wöchentlich, Sonntag, 08:00 Uhr
3. Aktion: Programm `python.exe`, Argumente `rechnungslauf.py`,
   Starten in: Pfad zu `tools\rechnungsautomation`

Nach jedem automatischen Lauf: `entwuerfe/`-Ordner öffnen, PDFs prüfen und
verschicken.

## Hinweis

Die Rechnungsnummer wird hier nicht vergeben (nur Dateiname mit Datum).
Falls du eine Buchhaltungssoftware mit fortlaufender Nummerierung nutzt,
trag die Nummer beim Verschicken dort ein.
