"""Veröffentlicht freigegebene Posts aus der Content-Queue auf Instagram.

Hauptformat: Bild-Posts (image_url gesetzt). Reels sind optionale Ergänzung
(video_url gesetzt, type == "reel") — siehe automation/README.md.
Fasst nur Einträge mit status == "approved" und platform == "instagram" an.
Braucht IG_ACCESS_TOKEN + IG_BUSINESS_ACCOUNT_ID.
"""
import time

from common import CONTENT_QUEUE, graph_request, load_json, log, now_iso, require_env, save_json

POLL_INTERVAL_SECONDS = 15
POLL_TIMEOUT_SECONDS = 300


def build_caption(item: dict) -> str:
    parts = [item.get("caption", "").strip()]
    if item.get("cta"):
        parts.append(item["cta"])
    if item.get("hashtags"):
        parts.append(" ".join(item["hashtags"]))
    return "\n\n".join(p for p in parts if p)


def publish_image(item: dict, ig_user_id: str, token: str) -> None:
    container = graph_request(
        "POST", f"{ig_user_id}/media", token,
        image_url=item["image_url"],
        caption=build_caption(item),
    )
    result = graph_request("POST", f"{ig_user_id}/media_publish", token, creation_id=container["id"])
    item["status"] = "posted"
    item["posted_at"] = now_iso()
    item["media_id"] = result["id"]
    log(f"Instagram Bild-Post veröffentlicht: {item['id']} -> media_id {result['id']}")


def publish_reel(item: dict, ig_user_id: str, token: str) -> None:
    container = graph_request(
        "POST", f"{ig_user_id}/media", token,
        media_type="REELS",
        video_url=item["video_url"],
        caption=build_caption(item),
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
        try:
            if item.get("image_url"):
                publish_image(item, env["IG_BUSINESS_ACCOUNT_ID"], env["IG_ACCESS_TOKEN"])
            elif item.get("video_url"):
                publish_reel(item, env["IG_BUSINESS_ACCOUNT_ID"], env["IG_ACCESS_TOKEN"])
            else:
                log(f"Übersprungen (weder image_url noch video_url gesetzt): {item['id']}")
        except Exception as exc:
            item["status"] = "failed"
            item["fehler"] = str(exc)
            log(f"Fehler beim Posten von {item['id']}: {exc}")

    save_json(CONTENT_QUEUE, queue)


if __name__ == "__main__":
    main()
