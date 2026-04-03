from fastapi import APIRouter, HTTPException, status
from app.api.schemas import MeetingCreate, MeetingRead

router = APIRouter(prefix="/meetings", tags=["meetings"])


DB: dict[str, dict] = {}


@router.post("", response_model=MeetingRead, status_code=status.HTTP_201_CREATED)
def create_meeting(payload: MeetingCreate):
    meeting_id = str(len(DB) + 1)
    DB[meeting_id] = {"id": meeting_id, **payload.model_dump()}
    return DB[meeting_id]


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_meeting(meeting_id: str):
    item = DB.get(meeting_id)
    if not item:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return item


@router.put("/{meeting_id}", response_model=MeetingRead)
def update_meeting(meeting_id: str, payload: MeetingCreate):
    item = DB.get(meeting_id)
    if not item:
        raise HTTPException(status_code=404, detail="Meeting not found")

    updated = {"id": meeting_id, **payload.model_dump()}
    DB[meeting_id] = updated
    return updated
