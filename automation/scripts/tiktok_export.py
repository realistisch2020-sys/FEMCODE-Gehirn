"""TikTok-Export: bereitet Content zum manuellen Hochladen vor, postet nichts.

TikToks Content Posting API ist restriktiver als Meta (App-Review nötig,
unaudited Apps dürfen oft nur privat/Entwurf posten) — deshalb hier bewusst
kein Auto-Posting, nur ein Export als CSV-Manifest mit Verweis auf die
bereits gerenderten Bilder aus outputs/social-images/. Cadence-Vorschlag
laut Vorgabe: 3–5 Posts/Woche manuell hochladen.

Sobald ein sauberer API-Zugang geprüft ist, kann das später automatisiert
werden — bis dahin: Bild öffnen, Caption kopieren, in der TikTok-App hochladen.
"""
import csv

from common import CONTENT_QUEUE, ROOT, load_json, log

EXPORT_FILE = ROOT / "outputs" / "tiktok-export.csv"


def export() -> int:
    queue = load_json(CONTENT_QUEUE)
    # Instagram-Einträge als Basis: Bild + Text sind plattformunabhängig gleich,
    # nur Cadence/Upload-Weg unterscheidet sich.
    items = [i for i in queue if i.get("type") == "image" and i.get("platform") == "instagram"]

    EXPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(EXPORT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["datum_vorschlag", "bild_datei", "hook", "caption", "kategorie", "link"])
        for item in items:
            writer.writerow([
                item.get("datum", ""),
                item.get("image_local_path", ""),
                item.get("hook", ""),
                item.get("caption", "").replace("\n", " / "),
                item.get("kategorie", ""),
                item.get("link", ""),
            ])

    log(f"{len(items)} Einträge für TikTok exportiert nach {EXPORT_FILE}")
    return len(items)


if __name__ == "__main__":
    export()
