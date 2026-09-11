"""Erzeugt Reel-Entwürfe (Hook/Skript/Caption/Hashtags) für die Content-Queue.

Liest context/business.md + context/strategie.md als Markenkontext, lässt
Claude Entwürfe schreiben und hängt sie mit status="draft" an
automation/content_queue.json an. Postet nichts — dafür erst approve.py,
dann publish_instagram.py / publish_facebook.py.
"""
import argparse
import json
import sys
import uuid

import anthropic

from common import CONTENT_QUEUE, ROOT, load_json, log, now_iso, save_json

MODEL = "claude-opus-5"

TRACKS = {
    "buecher": "Bücher",
    "business": "Produkte/Business",
}

# Platzhalter-Text, den business.md ungefüllt mitbringt — solange die noch
# drinstehen, wäre jeder generierte Content generisch statt markenspezifisch.
TEMPLATE_MARKERS = [
    "Welche Produkte, Programme oder Leistungen?",
    "Für wen ist das?",
]


def read_context() -> str:
    parts = []
    for rel_path in ("context/business.md", "context/strategie.md"):
        path = ROOT / rel_path
        if path.exists():
            parts.append(f"### {rel_path}\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def is_still_template(context_text: str) -> bool:
    return any(marker in context_text for marker in TEMPLATE_MARKERS)


def build_prompt(track_label: str, count: int) -> str:
    return f"""Du schreibst Instagram/Facebook-Reel-Konzepte für die Content-Spur "{track_label}".

Liefere genau {count} Konzepte als JSON-Array, sonst nichts. Format pro Element:
{{"hook": "erste 2 Sekunden, reisst rein", "skript": "3-5 Talking Points fuers Reel", "caption": "fertige Caption inkl. CTA", "hashtags": ["#beispiel1", "#beispiel2"]}}

Nur das JSON-Array zurückgeben, kein einleitender oder erklärender Text."""


def generate(track: str, count: int) -> None:
    context_text = read_context()
    if not context_text or is_still_template(context_text):
        sys.exit(
            "context/business.md ist noch nicht ausgefüllt — Content wäre generisch.\n"
            "Erst Bücher/Produkte/Zielgruppe eintragen, dann nochmal laufen lassen."
        )

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=f"Markenkontext:\n\n{context_text}",
        messages=[{"role": "user", "content": build_prompt(TRACKS[track], count)}],
    )

    text = next((block.text for block in response.content if block.type == "text"), "")
    try:
        items = json.loads(text)
    except json.JSONDecodeError:
        sys.exit(f"Antwort war kein gültiges JSON, nichts gespeichert:\n{text}")

    queue = load_json(CONTENT_QUEUE)
    for item in items:
        queue.append({
            "id": uuid.uuid4().hex[:8],
            "track": track,
            "platform": None,        # beim Freigeben setzen: "instagram" / "facebook"
            "type": "reel",
            "hook": item.get("hook", ""),
            "skript": item.get("skript", ""),
            "caption": item.get("caption", ""),
            "hashtags": item.get("hashtags", []),
            "video_url": None,       # muss vor Freigabe gesetzt werden (Baustein 2 noch offen)
            "status": "draft",
            "created_at": now_iso(),
            "posted_at": None,
            "media_id": None,
        })
    save_json(CONTENT_QUEUE, queue)
    log(f"{len(items)} neue Entwürfe für '{track}' erzeugt.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reel-Entwürfe erzeugen")
    parser.add_argument("track", choices=TRACKS.keys())
    parser.add_argument("--count", type=int, default=4)
    args = parser.parse_args()
    generate(args.track, args.count)
