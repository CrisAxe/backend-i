from fastapi import FastAPI
from app.api.routers.meetings import router as meetings_router
from app.api.routers.action_items import router as action_items_router

app = FastAPI(title="Meeting Note Assistant API")

app.include_router(meetings_router)
app.include_router(action_items_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
