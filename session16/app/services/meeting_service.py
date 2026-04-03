from uuid import uuid4

from app.core.errors import NotFoundError
from app.domain.models import Meeting
from app.storage.json_repository import load_all, save_all


def create_meeting(title: str, date: str, owner: str) -> Meeting:
    meetings = load_all()
    meeting = Meeting(id=str(uuid4()), title=title, date=date, owner=owner)
    meetings.append(meeting)
    save_all(meetings)
    return meeting


def list_meetings() -> list[Meeting]:
    return load_all()


def get_meeting(meeting_id: str) -> Meeting:
    meetings = load_all()
    for m in meetings:
        if m.id == meeting_id:
            return m
    raise NotFoundError(f"Meeting {meeting_id} not found")


def update_meeting(meeting_id: str, title: str, date: str, owner: str) -> Meeting:
    meetings = load_all()
    for idx, m in enumerate(meetings):
        if m.id == meeting_id:
            updated = Meeting(id=meeting_id, title=title, date=date, owner=owner)
            meetings[idx] = updated
            save_all(meetings)
            return updated

    raise NotFoundError(f"Meeting {meeting_id} not found")
