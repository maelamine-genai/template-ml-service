from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Template ML Service", version="0.1.0")

# --- basic health ---
@app.get("/healthz")
def healthz() -> dict[str, bool]:
    return {"ok": True}

# --- friendly root (points to docs) ---
@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "template-ml-service",
        "status": "ok",
        "docs": "/docs",
        "health": "/healthz",
        "infer": "/v1/infer"
    }

# --- placeholder inference route you can reuse in templates ---
class InferenceIn(BaseModel):
    query: str
    top_k: Optional[int] = 3

class InferenceOut(BaseModel):
    answer: str
    latency_ms: int

@app.post("/v1/infer", response_model=InferenceOut)
def infer(x: InferenceIn) -> InferenceOut:
    # wire this to a pipeline later
    return InferenceOut(answer=f"you said: {x.query}", latency_ms=1)
