from fastapi import APIRouter
import backend.routes.metrics_store as store

router = APIRouter()

@router.get("/api/v1/metrics")
async def get_metrics():
    return {
        "status": "success",
        "metrics": store.metrics_store
    }
