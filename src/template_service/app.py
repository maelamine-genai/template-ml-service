from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="GenAI Service")

class In(BaseModel):
    query: str

@app.get("/healthz")
def healthz():
    return {"ok": True, "ts": time.time()}

@app.post("/v1/infer")
def infer(x: In):
    # wire up to pipeline module
    return {"answer": f"you said: {x.query}", "latency_ms": 1}
