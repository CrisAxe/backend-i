from fastapi import FastAPI
from app.api.schemas import MeetingCreate, MeetingRead

app = FastAPI(title="Meeting Note Assistant API")

DB: dict[str, dict] = {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/meetings", response_model=list[MeetingRead])
def list_meetings() -> list[MeetingRead]:
    return list(DB.values())


@app.post("/meetings", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate) -> MeetingRead:
    meeting_id = str(len(DB) + 1)
    item = {"id": meeting_id, **payload.model_dump()}
    DB[meeting_id] = item
    return item
