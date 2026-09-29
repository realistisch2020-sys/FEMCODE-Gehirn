"""Content-Kalender-Builder: erzeugt aus den Hooks fertige, geplante Posts.

Liest automation/data/hooks_buch1.json, rendert pro Hook ein Bild (Text-
Overlay-Generator) nach outputs/social-images/ und legt je einen Instagram-
und einen Facebook-Eintrag mit status="draft" in der Content-Queue an.
Postet nichts -- das bleibt bei approve.py + den publish-Skripten.

image_url zeigt auf die vorgesehene GitHub-Pages-URL. Die Datei liegt dort
erst, sobald outputs/social-images/ auf den gh-pages-Branch übertragen
wurde -- das passiert nicht automatisch, siehe automation/README.md.
"""
import json
import uuid
from datetime import date, timedelta

from common import AUTOMATION_DIR, CONTENT_QUEUE, ROOT, load_json, log, now_iso, save_json
from render_image import render

HOOKS_FILE = AUTOMATION_DIR / "data" / "hooks_buch1.json"
BOOKS_FILE = AUTOMATION_DIR / "books.json"
IMAGES_DIR = AUTOMATION_DIR / "assets" / "images"
OUTPUT_DIR = ROOT / "outputs" / "social-images"

PAGES_BASE_URL = "https://realistisch2020-sys.github.io/FEMCODE-Gehirn"

# Zwei Quellbilder bisher -- Pain-Point-Motiv fuer die Wund-Punkt-Kategorien,
# Petras eigenes Portrait fuer die direkten/fordernden Aussagen. Mehr Fotos
# von Petra wuerden die Wiederholung im Feed spuerbar reduzieren.
PILLAR_TO_IMAGE = {
    "Selbstverlust": "erschoepfte-frau-stock.jpg",
    "Funktionieren": "erschoepfte-frau-stock.jpg",
    "Schuldgefühle": "erschoepfte-frau-stock.jpg",
    "Beziehungsmüdigkeit": "erschoepfte-frau-stock.jpg",
    "Grenzen": "petra-portrait.jpg",
    "Loslassen": "petra-portrait.jpg",
    "Verkaufsimpuls": "petra-portrait.jpg",
}

PILLAR_CLOSER = {
    "Selbstverlust": 'Genau davon handelt „{titel}".',
    "Schuldgefühle": 'Wenn du das kennst, ist „{titel}" für dich.',
    "Funktionieren": 'Mehr davon in „{titel}".',
    "Beziehungsmüdigkeit": 'Darüber schreibe ich in „{titel}".',
    "Grenzen": 'Mehr dazu in „{titel}".',
    "Loslassen": 'Genau darum geht\'s in „{titel}".',
    "Verkaufsimpuls": 'Jetzt lesen: „{titel}".',
}


def build(start_date: date = None, book_key: str = "hauptbuch") -> int:
    hooks = json.loads(HOOKS_FILE.read_text(encoding="utf-8"))
    books = json.loads(BOOKS_FILE.read_text(encoding="utf-8"))
    book = books[book_key]
    titel = book["titel"]
    link = book.get("amazon_taschenbuch") or books["autorenseite"]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    queue = load_json(CONTENT_QUEUE)
    existing_ids = {item["id"] for item in queue}

    current_date = start_date or (date.today() + timedelta(days=1))
    added = 0

    for i, entry in enumerate(hooks, start=1):
        hook = entry["hook"]
        kategorie = entry["kategorie"]
        background = IMAGES_DIR / PILLAR_TO_IMAGE.get(kategorie, "petra-portrait.jpg")
        filename = f"{book_key}-{i:02d}.jpg"
        output_path = OUTPUT_DIR / filename
        render(str(background), hook, str(output_path), footer=titel)

        closer = PILLAR_CLOSER.get(kategorie, "").format(titel=titel)
        caption = f"{hook}\n\n{closer}".strip()
        image_url = f"{PAGES_BASE_URL}/social-images/{filename}"
        datum = current_date.isoformat()

        for platform in ("instagram", "facebook"):
            post_id = uuid.uuid4().hex[:8]
            while post_id in existing_ids:
                post_id = uuid.uuid4().hex[:8]
            existing_ids.add(post_id)
            cta = "Jetzt lesen — Link in Bio" if platform == "instagram" else f"Jetzt lesen: {link}"
            queue.append({
                "id": post_id,
                "track": "buecher",
                "buch": book_key,
                "kategorie": kategorie,
                "platform": platform,
                "type": "image",
                "hook": hook,
                "skript": None,
                "overlay_text": hook,
                "caption": caption,
                "cta": cta,
                "link": link,
                "hashtags": [],
                "video_url": None,
                "image_url": image_url,
                "image_local_path": str(output_path.relative_to(ROOT)),
                "datum": datum,
                "status": "draft",
                "created_at": now_iso(),
                "posted_at": None,
                "media_id": None,
                "fehler": None,
            })
            added += 1
        current_date += timedelta(days=1)

    save_json(CONTENT_QUEUE, queue)
    log(f"{added} neue geplante Posts erzeugt ({len(hooks)} Hooks x 2 Plattformen), Bilder in {OUTPUT_DIR}")
    return added


if __name__ == "__main__":
    build()
