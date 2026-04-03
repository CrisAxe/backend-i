from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_meeting():
    payload = {
        "title": "Planning",
        "date": "2026-03-10",
        "owner": "Cristian"
    }
    response = client.post("/meetings", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Planning"
    assert data["owner"] == "Cristian"
    assert "id" in data


def test_list_meetings():
    response = client.get("/meetings")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_meeting_not_found():
    response = client.get("/meetings/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Meeting not found"
