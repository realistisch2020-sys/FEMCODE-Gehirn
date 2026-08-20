# Kopiere diese Datei zu config.py und trage deine echten Daten ein.
# config.py wird NICHT in git gespeichert (siehe .gitignore) - deine Bankdaten
# bleiben also nur auf deinem Rechner.

# --- Wer bist du (Rechnungssteller) ---
ABSENDER_NAME = "Vorname Nachname"
ABSENDER_STRASSE = "Musterstrasse"
ABSENDER_HAUSNUMMER = "1"
ABSENDER_PLZ = "8000"
ABSENDER_ORT = "Zürich"
ABSENDER_LAND = "CH"

# --- Zahlungsdaten ---
# IBAN oder QR-IBAN deines Kontos (ohne Leerzeichen)
IBAN = "CH0000000000000000000"

# True, wenn IBAN oben eine QR-IBAN ist (erkennbar an "30000" bis "31999"
# als 5.-9. Ziffer der IBAN). Falls True, braucht JEDER Kunde in kunden.csv
# eine Referenz_ID (siehe kunden_vorlage.csv).
IST_QR_IBAN = False

WAEHRUNG = "CHF"
SPRACHE = "de"  # de, fr, it oder en

# --- Sonstiges ---
KUNDEN_DATEI = "kunden.csv"
AUSGABE_ORDNER = "entwuerfe"
PROTOKOLL_DATEI = "protokoll.csv"

# Zahlungsfrist in Tagen, die auf der Rechnung als Hinweistext erscheint
ZAHLUNGSFRIST_TAGE = 30
