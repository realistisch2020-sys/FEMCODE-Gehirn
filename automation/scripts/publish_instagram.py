"""Veröffentlicht freigegebene Reels aus der Content-Queue auf Instagram.

Fasst nur Einträge mit status == "approved", platform == "instagram" und
gesetztem video_url an. Braucht IG_ACCESS_TOKEN + IG_BUSINESS_ACCOUNT_ID
(siehe automation/README.md für den Weg dorthin).

Ablauf laut Meta Content Publishing API: Media-Container anlegen, auf
Verarbeitung warten (FINISHED), dann veröffentlichen.
"""
import time

from common import CONTENT_QUEUE, graph_request, load_json, log, now_iso, require_env, save_json

POLL_INTERVAL_SECONDS = 15
POLL_TIMEOUT_SECONDS = 300


def publish_one(item: dict, ig_user_id: str, token: str) -> None:
    caption = f"{item['caption']}\n\n{' '.join(item.get('hashtags', []))}".strip()
    container = graph_request(
        "POST", f"{ig_user_id}/media", token,
        media_type="REELS",
        video_url=item["video_url"],
        caption=caption,
        share_to_feed="true",
    )
    creation_id = container["id"]

    waited = 0
    while waited < POLL_TIMEOUT_SECONDS:
        status = graph_request("GET", creation_id, token, fields="status_code")
        code = status.get("status_code")
        if code == "FINISHED":
            break
        if code == "ERROR":
            raise RuntimeError(f"Video-Verarbeitung fehlgeschlagen für {item['id']}: {status}")
        time.sleep(POLL_INTERVAL_SECONDS)
        waited += POLL_INTERVAL_SECONDS
    else:
        raise TimeoutError(f"Video-Verarbeitung nicht fertig nach {POLL_TIMEOUT_SECONDS}s: {item['id']}")

    result = graph_request("POST", f"{ig_user_id}/media_publish", token, creation_id=creation_id)
    item["status"] = "posted"
    item["posted_at"] = now_iso()
    item["media_id"] = result["id"]
    log(f"Instagram Reel veröffentlicht: {item['id']} -> media_id {result['id']}")


def main() -> None:
    env = require_env("IG_ACCESS_TOKEN", "IG_BUSINESS_ACCOUNT_ID")
    queue = load_json(CONTENT_QUEUE)
    pending = [i for i in queue if i["status"] == "approved" and i.get("platform") == "instagram"]

    if not pending:
        log("Keine freigegebenen Instagram-Posts in der Queue.")
        return

    for item in pending:
        if not item.get("video_url"):
            log(f"Übersprungen (kein video_url gesetzt): {item['id']}")
            continue
        try:
            publish_one(item, env["IG_BUSINESS_ACCOUNT_ID"], env["IG_ACCESS_TOKEN"])
        except Exception as exc:
            log(f"Fehler beim Posten von {item['id']}: {exc}")

    save_json(CONTENT_QUEUE, queue)


if __name__ == "__main__":
    main()
