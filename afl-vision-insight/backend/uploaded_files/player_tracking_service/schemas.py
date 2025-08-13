from pydantic import BaseModel
from typing import List, Dict, Any

class InferenceRequest(BaseModel):
    file_path: str

class InferenceResponse(BaseModel):
    video_info: Dict[str, Any]
    tracking_results: List[Dict[str, Any]]
