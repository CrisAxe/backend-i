from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas import MeetingCreate, MeetingRead
from app.core.auth import require_api_key

router = APIRouter(
    prefix="/meetings",
    tags=["meetings"],
    dependencies=[Depends(require_api_key)],
)

# In-memory DB
DB: dict[str, dict] = {}


@router.post("", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate):
    meeting_id = str(len(DB) + 1)
    DB[meeting_id] = {"id": meeting_id, **payload.model_dump()}
    return DB[meeting_id]


@router.get("", response_model=list[MeetingRead])
def list_meetings():
    return list(DB.values())


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_meeting(meeting_id: str):
    item = DB.get(meeting_id)
    if not item:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return item
