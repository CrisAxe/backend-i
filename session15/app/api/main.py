from fastapi import FastAPI
from app.api.routers.meetings import router as meetings_router
from app.core.logging_config import configure_logging
from app.core.middleware import request_tracing_middleware

configure_logging()

app = FastAPI(title="Meeting Note Assistant API - Session 15")


app.middleware("http")(request_tracing_middleware)

app.include_router(meetings_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
