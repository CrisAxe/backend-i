from fastapi import FastAPI
from app.api.routers.meetings import router as meetings_router

app = FastAPI(title="Meeting Note Assistant API - Session 16")

app.include_router(meetings_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
