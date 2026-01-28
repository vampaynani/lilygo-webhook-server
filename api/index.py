from __future__ import annotations

import logging

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("sim-update")

app = FastAPI(title="Sim Update Receiver")


@app.post("/sim-update")
async def receive_sim_update(request: Request) -> JSONResponse:
    payload = await request.json()
    logger.info("sim-update payload received: %s", payload)
    return JSONResponse({"status": "ok"})
