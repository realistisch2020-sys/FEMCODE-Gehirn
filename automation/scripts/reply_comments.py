"""Sendet Antworten auf Kommentare, die ein Mensch freigegeben hat.

Fasst nur Einträge mit status == "approved" und nicht-leerem draft_reply an.
Ohne vorherige Freigabe über approve.py wird nichts gesendet.
"""
from common import COMMENTS_QUEUE, graph_request, load_json, log, now_iso, require_env, save_json


def main() -> None:
    env = require_env("IG_ACCESS_TOKEN")
    queue = load_json(COMMENTS_QUEUE)
    pending = [c for c in queue if c["status"] == "approved" and c.get("draft_reply")]

    if not pending:
        log("Keine freigegebenen Kommentar-Antworten in der Queue.")
        return

    for comment in pending:
        try:
            graph_request(
                "POST", f"{comment['comment_id']}/replies", env["IG_ACCESS_TOKEN"],
                message=comment["draft_reply"],
            )
            comment["status"] = "replied"
            comment["replied_at"] = now_iso()
            log(f"Antwort gesendet auf Kommentar {comment['comment_id']}")
        except Exception as exc:
            log(f"Fehler bei Antwort auf {comment['comment_id']}: {exc}")

    save_json(COMMENTS_QUEUE, queue)


if __name__ == "__main__":
    main()
