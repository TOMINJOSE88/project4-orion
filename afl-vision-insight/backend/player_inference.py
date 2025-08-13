from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import random

router = APIRouter()

class PlayerInferenceResponse(BaseModel):
    label: str
    confidence: float
    timestamp: str

class PlayerMetricsResponse(BaseModel):
    player_inference_calls: int
    last_player_result: PlayerInferenceResponse | None

metrics_store = {
    "player_inference_calls": 0,
    "last_player_result": None
}

@router.post("/player", response_model=PlayerInferenceResponse)
async def infer_player():
    result = {
        "label": "player",
        "confidence": round(random.uniform(0.8, 0.99), 2),
        "timestamp": datetime.utcnow().isoformat()
    }
    metrics_store["player_inference_calls"] += 1
    metrics_store["last_player_result"] = result
    return result

@router.get("/metrics", response_model=PlayerMetricsResponse)
async def get_metrics():
    return {
        "player_inference_calls": metrics_store["player_inference_calls"],
        "last_player_result": metrics_store["last_player_result"]
    }
