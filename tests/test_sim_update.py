from fastapi.testclient import TestClient

from api.index import app


def test_sim_update_endpoint_logs_and_responds_ok(monkeypatch):
    logged = {}

    def fake_info(msg, *args, **kwargs):
        logged['message'] = msg % args

    monkeypatch.setattr(app.logger, 'info', fake_info)

    client = TestClient(app)
    payload = {"service": "simulation", "status": "complete"}

    response = client.post("/sim-update", json=payload)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert logged['message'].startswith("sim-update payload received")
    assert '"service": "simulation"' in logged['message']
