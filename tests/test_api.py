from fastapi.testclient import TestClient

from src.web_service.main import app

client = TestClient(app)


def test_health_check():
    assert client.get("/").json() == {"health_check": "App up and running!"}


def test_predict_rejects_bad_input():
    response = client.post("/predict", json={"sex": "X", "length": -1})
    assert response.status_code == 422
