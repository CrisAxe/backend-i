import logging
from uuid import uuid4

from app.core.validators import validate_iso_date
from app.domain.models import Meeting
from app.storage.json_repository import load_meetings, save_meetings

logger = logging.getLogger(__name__)


def create_meeting(title: str, date: str, owner: str) -> Meeting:
    logger.info("Validating meeting date", extra={"date": date})
    validate_iso_date(date)

    logger.info("Loading existing meetings")
    meetings = load_meetings()

    meeting = Meeting(id=str(uuid4()), title=title, date=date, owner=owner)
    logger.info(
        "Creating meeting",
        extra={"id": meeting.id, "title": title, "date": date, "owner": owner},
    )

    meetings.append(meeting)
    save_meetings(meetings)
    logger.info("Meeting saved", extra={"id": meeting.id})
    return meeting


def list_meetings() -> list[Meeting]:
    logger.info("Listing meetings")
    return load_meetings()
