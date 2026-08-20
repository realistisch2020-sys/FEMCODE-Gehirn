#!/usr/bin/env python3
"""
Rechnungslauf: erstellt jeden Sonntag Rechnungs-Entwuerfe (Schweizer QR-Rechnung)
fuer alle Kunden, die in der kommenden Woche faellig sind.

Aufruf:
    python3 rechnungslauf.py                # normaler Lauf, heute = echtes Datum
    python3 rechnungslauf.py --dry-run       # nur anzeigen, nichts schreiben/erstellen
    python3 rechnungslauf.py --datum 2026-08-23   # Testlauf mit anderem "heute"

Voraussetzung: config.py existiert (Kopie von config_vorlage.py, siehe README.md).
"""
import argparse
import csv
import sys
from datetime import date, timedelta
from pathlib import Path

try:
    import config
except ImportError:
    sys.exit(
        "config.py fehlt. Kopiere config_vorlage.py zu config.py und trage "
        "deine Daten ein (siehe README.md)."
    )

from qrbill import QRBill
from stdnum.ch import esr
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics import renderPDF

ORDNER = Path(__file__).resolve().parent
RHYTHMUS_MONATE = {
    "monatlich": 1,
    "1 monat": 1,
    "quartal": 3,
    "3 monate": 3,
    "3monate": 3,
    "halbjahr": 6,
    "6 monate": 6,
    "6monate": 6,
}


def parse_rhythmus(text):
    schluessel = text.strip().lower()
    if schluessel not in RHYTHMUS_MONATE:
        raise ValueError(
            f"Unbekannter Rhythmus '{text}'. Erlaubt: monatlich, 3 monate, 6 monate."
        )
    return RHYTHMUS_MONATE[schluessel]


def parse_datum(text):
    return date.fromisoformat(text.strip())


def monate_addieren(d, anzahl_monate):
    monat_index = d.month - 1 + anzahl_monate
    jahr = d.year + monat_index // 12
    monat = monat_index % 12 + 1
    letzter_tag_im_monat = [
        31, 29 if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0) else 28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
    ][monat - 1]
    tag = min(d.day, letzter_tag_im_monat)
    return date(jahr, monat, tag)


def naechste_faelligkeiten(start, letzte_rechnung, monate, bis_datum):
    """Liefert alle Faelligkeitstermine <= bis_datum, die noch nicht abgerechnet sind."""
    if letzte_rechnung is None:
        naechste = start
    else:
        naechste = monate_addieren(letzte_rechnung, monate)
    termine = []
    absicherung = 0
    while naechste <= bis_datum and absicherung < 24:
        termine.append(naechste)
        naechste = monate_addieren(naechste, monate)
        absicherung += 1
    return termine


def lade_kunden(pfad):
    with open(pfad, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames), list(reader)


def speichere_kunden(pfad, fieldnames, zeilen):
    with open(pfad, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(zeilen)


def referenznummer(referenz_id):
    """Baut aus einer Kundennummer eine gueltige 27-stellige QRR-Referenz
    (26 Ziffern + Pruefziffer)."""
    basis = "".join(ch for ch in referenz_id if ch.isdigit())
    if not basis:
        raise ValueError(f"Referenz_ID '{referenz_id}' enthaelt keine Ziffern.")
    basis = basis[-26:].zfill(26)
    pruefziffer = esr.calc_check_digit(basis)
    return basis + pruefziffer


def erstelle_pdf(kunde, faelligkeit, periode_start, ausgabe_pfad):
    reference_number = None
    if config.IST_QR_IBAN:
        referenz_id = (kunde.get("Referenz_ID") or "").strip()
        if not referenz_id:
            raise ValueError(
                f"Kunde '{kunde['Name']}' hat keine Referenz_ID, aber IST_QR_IBAN=True."
            )
        reference_number = referenznummer(referenz_id)

    notiz_teile = [
        f"Fernhilfe {periode_start.strftime('%d.%m.%Y')} - {faelligkeit.strftime('%d.%m.%Y')}"
    ]
    if kunde.get("Notiz"):
        notiz_teile.append(kunde["Notiz"].strip())
    zusatzinfo = " / ".join(t for t in notiz_teile if t)[:140]

    bill = QRBill(
        account=config.IBAN.replace(" ", ""),
        creditor={
            "name": config.ABSENDER_NAME,
            "street": config.ABSENDER_STRASSE,
            "house_num": config.ABSENDER_HAUSNUMMER,
            "pcode": config.ABSENDER_PLZ,
            "city": config.ABSENDER_ORT,
            "country": config.ABSENDER_LAND,
        },
        amount=f"{float(kunde['Betrag']):.2f}",
        currency=config.WAEHRUNG,
        debtor={
            "name": kunde["Name"],
            "street": kunde["Strasse"],
            "house_num": kunde.get("Hausnummer", ""),
            "pcode": kunde["PLZ"],
            "city": kunde["Ort"],
            "country": kunde.get("Land") or "CH",
        },
        reference_number=reference_number,
        additional_information=zusatzinfo,
        language=config.SPRACHE,
    )

    slip_svg = ausgabe_pfad.with_suffix(".slip.svg")
    bill.as_svg(str(slip_svg), full_page=False)
    zeichnung = svg2rlg(str(slip_svg))
    slip_svg.unlink()

    c = canvas.Canvas(str(ausgabe_pfad), pagesize=A4)
    breite, hoehe = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(20 * mm, hoehe - 25 * mm, "RECHNUNG")

    c.setFont("Helvetica", 9)
    absender_zeilen = [
        config.ABSENDER_NAME,
        f"{config.ABSENDER_STRASSE} {config.ABSENDER_HAUSNUMMER}",
        f"{config.ABSENDER_PLZ} {config.ABSENDER_ORT}",
    ]
    y = hoehe - 40 * mm
    for zeile in absender_zeilen:
        c.drawString(20 * mm, y, zeile)
        y -= 5 * mm

    empfaenger_zeilen = [
        kunde["Name"],
        f"{kunde['Strasse']} {kunde.get('Hausnummer', '')}".strip(),
        f"{kunde['PLZ']} {kunde['Ort']}",
    ]
    y = hoehe - 40 * mm
    for zeile in empfaenger_zeilen:
        c.drawString(120 * mm, y, zeile)
        y -= 5 * mm

    y = hoehe - 70 * mm
    c.setFont("Helvetica", 10)
    c.drawString(20 * mm, y, f"Rechnungsdatum: {faelligkeit.strftime('%d.%m.%Y')}")
    y -= 6 * mm
    c.drawString(
        20 * mm,
        y,
        f"Leistungszeitraum: {periode_start.strftime('%d.%m.%Y')} - {faelligkeit.strftime('%d.%m.%Y')}",
    )
    y -= 6 * mm
    if kunde.get("Notiz"):
        c.drawString(20 * mm, y, kunde["Notiz"].strip())
        y -= 6 * mm
    y -= 6 * mm

    c.setFont("Helvetica-Bold", 11)
    c.drawString(20 * mm, y, f"Betrag: {config.WAEHRUNG} {float(kunde['Betrag']):.2f}")
    y -= 10 * mm

    c.setFont("Helvetica", 9)
    c.drawString(
        20 * mm,
        y,
        f"Zahlbar innert {config.ZAHLUNGSFRIST_TAGE} Tagen. Vielen Dank!",
    )

    renderPDF.draw(zeichnung, c, 0, 0)
    c.showPage()
    c.save()


def slug(text):
    ersetzt = "".join(ch if ch.isalnum() else "-" for ch in text.strip().lower())
    while "--" in ersetzt:
        ersetzt = ersetzt.replace("--", "-")
    return ersetzt.strip("-")


def hauptlauf(heute, dry_run):
    kunden_pfad = ORDNER / config.KUNDEN_DATEI
    if not kunden_pfad.exists():
        sys.exit(
            f"{kunden_pfad.name} fehlt. Kopiere kunden_vorlage.csv zu "
            f"{config.KUNDEN_DATEI} und trage deine Kunden ein."
        )

    fieldnames, kunden = lade_kunden(kunden_pfad)
    woche_start = heute + timedelta(days=1)
    woche_ende = woche_start + timedelta(days=6)

    ausgabe_ordner = ORDNER / config.AUSGABE_ORDNER
    ausgabe_ordner.mkdir(exist_ok=True)
    protokoll_pfad = ORDNER / config.PROTOKOLL_DATEI
    protokoll_neu = not protokoll_pfad.exists()

    erstellte = []
    fehler = []

    for kunde in kunden:
        if (kunde.get("Aktiv") or "").strip().upper() != "JA":
            continue
        try:
            monate = parse_rhythmus(kunde["Rhythmus"])
            start = parse_datum(kunde["Start"])
            letzte = parse_datum(kunde["Letzte_Rechnung"]) if kunde.get("Letzte_Rechnung") else None
            faelligkeiten = naechste_faelligkeiten(start, letzte, monate, woche_ende)
        except ValueError as e:
            fehler.append(f"{kunde.get('Name', '?')}: {e}")
            continue

        for faelligkeit in faelligkeiten:
            periode_start = letzte if letzte else start
            dateiname = f"{faelligkeit.isoformat()}_{slug(kunde['Name'])}.pdf"
            ausgabe_pfad = ausgabe_ordner / dateiname

            if not dry_run:
                try:
                    erstelle_pdf(kunde, faelligkeit, periode_start, ausgabe_pfad)
                except Exception as e:
                    fehler.append(f"{kunde['Name']} ({faelligkeit}): {e}")
                    continue

            erstellte.append((kunde["Name"], faelligkeit, kunde["Betrag"], dateiname))
            kunde["Letzte_Rechnung"] = faelligkeit.isoformat()
            letzte = faelligkeit

    if not dry_run and erstellte:
        speichere_kunden(kunden_pfad, fieldnames, kunden)
        with open(protokoll_pfad, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if protokoll_neu:
                writer.writerow(["Lauf_Datum", "Kunde", "Faelligkeit", "Betrag", "Datei"])
            for name, faelligkeit, betrag, dateiname in erstellte:
                writer.writerow([heute.isoformat(), name, faelligkeit.isoformat(), betrag, dateiname])

    print(f"Rechnungslauf {heute.isoformat()} - Woche {woche_start} bis {woche_ende}")
    if dry_run:
        print("(Testlauf - es wurde nichts gespeichert)")
    if erstellte:
        print(f"{len(erstellte)} Rechnung(en) faellig:")
        for name, faelligkeit, betrag, dateiname in erstellte:
            print(f"  - {name}: CHF {betrag} faellig {faelligkeit.isoformat()} -> {dateiname}")
    else:
        print("Keine Rechnungen faellig diese Woche.")
    if fehler:
        print("Fehler:")
        for f in fehler:
            print(f"  - {f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--datum", type=parse_datum, default=date.today(), help="Testdatum (YYYY-MM-DD) statt heute")
    parser.add_argument("--dry-run", action="store_true", help="nur anzeigen, nichts erstellen oder speichern")
    args = parser.parse_args()
    hauptlauf(args.datum, args.dry_run)
