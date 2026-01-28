# Sim Update Receiver

A minimal FastAPI project that exposes a `POST /sim-update` webhook. It logs every JSON payload it receives and echoes a simple acknowledgement. This is configured to deploy on Vercel.

## Structure

- `api/index.py`: FastAPI app that handles `/sim-update` posts and logs payloads.
- `requirements.txt`: Pins `fastapi` and `uvicorn[standard]` for Vercel.
- `vercel.json`: Vercel configuration that routes requests to Python runtime.
- `tests/test_sim_update.py`: Smoke test using `TestClient`.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.index:app --reload
```

Then `POST` JSON to `http://localhost:8000/sim-update` (e.g., `curl -X POST -H 'Content-Type: application/json' -d '{"status": "ok"}' http://localhost:8000/sim-update`).

## Testing

```bash
pytest tests/test_sim_update.py
```

## Deployment

Deploy the repo to Vercel (either via the Vercel CLI or GitHub integration). Vercel will use `vercel.json` to run `api/index.py` on Python 3.11 and expose `/sim-update` at the project root.
