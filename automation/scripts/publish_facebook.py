"""Veröffentlicht freigegebene Posts aus der Content-Queue auf einer Facebook-Page.

Hauptformat: Bild-Posts (image_url -> /photos). Video optional
(video_url -> /videos, einfache Route, nicht das native Reels-Tab).
Ohne beides: reiner Text-Post. Fasst nur status == "approved" und
platform == "facebook" an. Braucht FB_PAGE_ID + FB_PAGE_ACCESS_TOKEN.
"""
from common import CONTENT_QUEUE, graph_request, load_json, log, now_iso, require_env, save_json


def build_message(item: dict) -> str:
    parts = [item.get("caption", "").strip()]
    if item.get("cta"):
        parts.append(item["cta"])
    if item.get("hashtags"):
        parts.append(" ".join(item["hashtags"]))
    return "\n\n".join(p for p in parts if p)


def main() -> None:
    env = require_env("FB_PAGE_ID", "FB_PAGE_ACCESS_TOKEN")
    queue = load_json(CONTENT_QUEUE)
    pending = [i for i in queue if i["status"] == "approved" and i.get("platform") == "facebook"]

    if not pending:
        log("Keine freigegebenen Facebook-Posts in der Queue.")
        return

    for item in pending:
        message = build_message(item)
        try:
            if item.get("image_url"):
                result = graph_request(
                    "POST", f"{env['FB_PAGE_ID']}/photos", env["FB_PAGE_ACCESS_TOKEN"],
                    url=item["image_url"], caption=message,
                )
            elif item.get("video_url"):
                result = graph_request(
                    "POST", f"{env['FB_PAGE_ID']}/videos", env["FB_PAGE_ACCESS_TOKEN"],
                    file_url=item["video_url"], description=message,
                )
            else:
                result = graph_request(
                    "POST", f"{env['FB_PAGE_ID']}/feed", env["FB_PAGE_ACCESS_TOKEN"],
                    message=message,
                )
            item["status"] = "posted"
            item["posted_at"] = now_iso()
            item["media_id"] = result["id"]
            log(f"Facebook-Post veröffentlicht: {item['id']} -> {result['id']}")
        except Exception as exc:
            item["status"] = "failed"
            item["fehler"] = str(exc)
            log(f"Fehler beim Posten von {item['id']}: {exc}")

    save_json(CONTENT_QUEUE, queue)


if __name__ == "__main__":
    main()
