"""Gemeinsame Helfer für die Social-Automation-Skripte."""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
AUTOMATION_DIR = ROOT / "automation"
CONTENT_QUEUE = AUTOMATION_DIR / "content_queue.json"
COMMENTS_QUEUE = AUTOMATION_DIR / "comments_queue.json"
LOG_FILE = ROOT / "outputs" / "social-log.md"

GRAPH_API_VERSION = "v21.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


def load_json(path: Path) -> list:
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def log(message: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"- {now_iso()} — {message}\n")
    print(message)


def require_env(*names: str) -> dict:
    """Holt Pflicht-Env-Vars oder bricht mit einer klaren Fehlermeldung ab."""
    values = {name: os.environ.get(name) for name in names}
    missing = [name for name, value in values.items() if not value]
    if missing:
        sys.exit(
            "Fehlende Umgebungsvariablen: " + ", ".join(missing) +
            " — als Secret hinterlegen, siehe automation/README.md"
        )
    return values


def graph_request(method: str, path: str, access_token: str, **params) -> dict:
    """Ruft die Meta Graph API auf und wirft bei Fehlern mit der Response mit.

    Hinweis: Feldnamen/Endpunkte sind nach bestem Wissen aus Sekundärquellen
    zusammengestellt (developers.facebook.com war in dieser Umgebung nicht
    direkt abrufbar). Vor dem ersten echten Lauf gegen die aktuelle Meta-Doku
    gegenchecken — siehe automation/README.md.
    """
    url = f"{GRAPH_API_BASE}/{path}"
    params = {**params, "access_token": access_token}
    if method == "GET":
        response = requests.get(url, params=params, timeout=30)
    else:
        response = requests.post(url, data=params, timeout=30)
    if not response.ok:
        raise RuntimeError(f"Graph API Fehler ({response.status_code}) bei {path}: {response.text}")
    return response.json()
