from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.api.schemas import MeetingCreate, MeetingRead

router = APIRouter(prefix="/meetings", tags=["meetings"])

DB: dict[str, dict] = {}


@router.post("", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate):
    meeting_id = str(len(DB) + 1)
    DB[meeting_id] = {"id": meeting_id, **payload.model_dump()}
    return DB[meeting_id]


@router.get("", response_model=dict)
def list_meetings(
    owner: Optional[str] = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    items = list(DB.values())

    if owner:
        items = [m for m in items if m["owner"] == owner]

    items = sorted(items, key=lambda x: x["date"])

    total = len(items)
    paginated = items[offset : offset + limit]

    return {"total": total, "items": paginated}


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_meeting(meeting_id: str):
    item = DB.get(meeting_id)
    if not item:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return item
