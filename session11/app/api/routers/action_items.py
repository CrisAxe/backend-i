from fastapi import APIRouter, HTTPException, status
from app.api.schemas import ActionItemCreate, ActionItemRead

router = APIRouter(prefix="/meetings", tags=["action-items"])

# In-memory DB for action items
# Key: meeting_id → List[action_item]
ACTION_DB: dict[str, list[dict]] = {}


@router.post("/{meeting_id}/action-items", response_model=ActionItemRead, status_code=status.HTTP_201_CREATED)
def create_action_item(meeting_id: str, payload: ActionItemCreate):
    # Create new action item
    items = ACTION_DB.get(meeting_id, [])
    item_id = str(len(items) + 1)

    item = {"id": item_id, **payload.model_dump()}
    ACTION_DB.setdefault(meeting_id, []).append(item)

    return item


@router.get("/{meeting_id}/action-items", response_model=list[ActionItemRead])
def list_action_items(meeting_id: str):
    return ACTION_DB.get(meeting_id, [])
