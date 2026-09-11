"""Veröffentlicht freigegebene Posts aus der Content-Queue auf einer Facebook-Page.

Fasst nur Einträge mit status == "approved" und platform == "facebook" an.
Postet ein Video über file_url, wenn video_url gesetzt ist, sonst einen
reinen Text-Post. Braucht FB_PAGE_ID + FB_PAGE_ACCESS_TOKEN.

Hinweis: nutzt die einfache /videos-Route, nicht die Chunked-Upload-API
fürs native Reels-Tab — reicht für "Video auf der Page", nicht für denselben
Feed wie Instagram Reels (siehe automation/README.md).
"""
from common import CONTENT_QUEUE, graph_request, load_json, log, now_iso, require_env, save_json


def main() -> None:
    env = require_env("FB_PAGE_ID", "FB_PAGE_ACCESS_TOKEN")
    queue = load_json(CONTENT_QUEUE)
    pending = [i for i in queue if i["status"] == "approved" and i.get("platform") == "facebook"]

    if not pending:
        log("Keine freigegebenen Facebook-Posts in der Queue.")
        return

    for item in pending:
        message = f"{item['caption']}\n\n{' '.join(item.get('hashtags', []))}".strip()
        try:
            if item.get("video_url"):
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
            log(f"Fehler beim Posten von {item['id']}: {exc}")

    save_json(CONTENT_QUEUE, queue)


if __name__ == "__main__":
    main()
