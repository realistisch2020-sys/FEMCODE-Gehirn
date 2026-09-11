"""Holt neue Kommentare der letzten Instagram-Posts in eine Prüf-Queue.

Postet nie selbst etwas — jeder abgeholte Kommentar landet mit
status="needs_review". draft_reply bleibt leer, bis jemand ihn über
approve.py setzt und freigibt; erst dann sendet reply_comments.py etwas.
"""
from common import COMMENTS_QUEUE, graph_request, load_json, log, now_iso, require_env, save_json

RECENT_MEDIA_LIMIT = 5


def main() -> None:
    env = require_env("IG_ACCESS_TOKEN", "IG_BUSINESS_ACCOUNT_ID")
    token = env["IG_ACCESS_TOKEN"]

    media = graph_request(
        "GET", f"{env['IG_BUSINESS_ACCOUNT_ID']}/media", token,
        fields="id,timestamp", limit=RECENT_MEDIA_LIMIT,
    ).get("data", [])

    queue = load_json(COMMENTS_QUEUE)
    known_ids = {c["comment_id"] for c in queue}
    added = 0

    for post in media:
        comments = graph_request(
            "GET", f"{post['id']}/comments", token,
            fields="id,text,username,timestamp",
        ).get("data", [])
        for comment in comments:
            if comment["id"] in known_ids:
                continue
            queue.append({
                "comment_id": comment["id"],
                "media_id": post["id"],
                "platform": "instagram",
                "author": comment.get("username", ""),
                "text": comment.get("text", ""),
                "draft_reply": "",
                "status": "needs_review",
                "fetched_at": now_iso(),
            })
            added += 1

    save_json(COMMENTS_QUEUE, queue)
    log(f"{added} neue Kommentare zur Prüfung hinzugefügt.")


if __name__ == "__main__":
    main()
