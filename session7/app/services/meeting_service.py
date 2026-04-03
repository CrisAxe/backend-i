from uuid import uuid4

from app.core.validators import validate_iso_date
from app.core.errors import NotFoundError
from app.domain.models import Meeting
from app.storage.json_repository import load_meetings, save_meetings


def create_meeting(title: str, date: str, owner: str) -> Meeting:
    validate_iso_date(date)

    meetings = load_meetings()
    meeting = Meeting(id=str(uuid4()), title=title, date=date, owner=owner)
    meetings.append(meeting)
    save_meetings(meetings)
    return meeting


def list_meetings() -> list[Meeting]:
    return load_meetings()


def get_meeting(meeting_id: str) -> Meeting:
    meetings = load_meetings()
    for m in meetings:
        if m.id == meeting_id:
            return m
    raise NotFoundError(f"Meeting {meeting_id} not found")


def delete_meeting(meeting_id: str) -> None:
    meetings = load_meetings()
    new_list = [m for m in meetings if m.id != meeting_id]

    if len(new_list) == len(meetings):
        raise NotFoundError(f"Meeting {meeting_id} not found")

    save_meetings(new_list)
