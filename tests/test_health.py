from fastapi.testclient import TestClient
from src.template_service.app import app
def test_health(): 
    c = TestClient(app)
    assert c.get("/healthz").json()["ok"] is True
