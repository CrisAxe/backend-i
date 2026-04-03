from fastapi import APIRouter, HTTPException

from app.api.schemas import MeetingCreate, MeetingRead
from app.services.meeting_service import (
    create_meeting,
    list_meetings,
    get_meeting,
    update_meeting,
)
from app.core.errors import NotFoundError

router = APIRouter(prefix="/meetings", tags=["meetings"])


@router.post("", response_model=MeetingRead, status_code=201)
def create(payload: MeetingCreate):
    return create_meeting(payload.title, payload.date, payload.owner)


@router.get("", response_model=list[MeetingRead])
def list_all():
    return list_meetings()


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_one(meeting_id: str):
    try:
        return get_meeting(meeting_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.put("/{meeting_id}", response_model=MeetingRead)
def update(meeting_id: str, payload: MeetingCreate):
    try:
        return update_meeting(meeting_id, payload.title, payload.date, payload.owner)
    except NotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
