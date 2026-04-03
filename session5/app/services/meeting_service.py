from uuid import uuid4

from app.core.validators import validate_iso_date
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
