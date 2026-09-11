"""Freigabe-CLI: nichts in diesem Ordner postet etwas, ohne dass es hier
erst auf "approved" gesetzt wurde.

Beispiele:
    python approve.py content list
    python approve.py content approve a1b2c3d4 --platform instagram --video-url https://...
    python approve.py comments list --status needs_review
    python approve.py comments approve f00dcafe
"""
import argparse

from common import COMMENTS_QUEUE, CONTENT_QUEUE, load_json, save_json


def list_items(queue_path, status_filter=None):
    queue = load_json(queue_path)
    shown = 0
    for item in queue:
        key = item.get("id") or item.get("comment_id")
        if status_filter and item["status"] != status_filter:
            continue
        print(f"[{key}] status={item['status']}")
        for field in ("track", "platform", "caption", "text", "draft_reply", "video_url"):
            if item.get(field):
                print(f"    {field}: {item[field]}")
        print()
        shown += 1
    if not shown:
        print("(keine Einträge)")


def set_status(queue_path, item_id, new_status, extra=None):
    queue = load_json(queue_path)
    for item in queue:
        key = item.get("id") or item.get("comment_id")
        if key == item_id:
            item["status"] = new_status
            if extra:
                item.update(extra)
            save_json(queue_path, queue)
            print(f"{item_id} -> {new_status}")
            return
    print(f"Nicht gefunden: {item_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Content- und Kommentar-Queue freigeben")
    parser.add_argument("queue", choices=["content", "comments"])
    sub = parser.add_subparsers(dest="action", required=True)

    p_list = sub.add_parser("list")
    p_list.add_argument("--status", default=None)

    p_approve = sub.add_parser("approve")
    p_approve.add_argument("id")
    p_approve.add_argument("--platform", choices=["instagram", "facebook"])
    p_approve.add_argument("--video-url")
    p_approve.add_argument("--draft-reply", help="Antworttext überschreiben (nur comments)")

    p_reject = sub.add_parser("reject")
    p_reject.add_argument("id")

    args = parser.parse_args()
    path = CONTENT_QUEUE if args.queue == "content" else COMMENTS_QUEUE

    if args.action == "list":
        list_items(path, args.status)
    elif args.action == "approve":
        extra = {}
        if getattr(args, "platform", None):
            extra["platform"] = args.platform
        if getattr(args, "video_url", None):
            extra["video_url"] = args.video_url
        if getattr(args, "draft_reply", None):
            extra["draft_reply"] = args.draft_reply
        set_status(path, args.id, "approved", extra)
    elif args.action == "reject":
        set_status(path, args.id, "rejected")
