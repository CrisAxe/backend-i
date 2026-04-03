from fastapi import FastAPI

app = FastAPI(title="Meeting Note Assistant API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/meetings")
def list_meetings() -> list[dict]:
    return []
