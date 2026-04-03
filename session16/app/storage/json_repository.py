import json
from pathlib import Path
from dataclasses import asdict

from app.domain.models import Meeting

DB = Path("data/meetings.json")


def load_all() -> list[Meeting]:
    if not DB.exists():
        return []

    raw = json.loads(DB.read_text(encoding="utf-8"))
    return [Meeting(**item) for item in raw]


def save_all(items: list[Meeting]) -> None:
    DB.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(m) for m in items]
    DB.write_text(json.dumps(payload, indent=2), encoding="utf-8")
