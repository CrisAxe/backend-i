from app.domain.models import Meeting


def summary(meetings: list[Meeting]) -> dict:
    return {
        "meetings": len(meetings),
        "action_items": sum(len(m.action_items) for m in meetings),
    }
