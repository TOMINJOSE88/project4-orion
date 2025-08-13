from fastapi import FastAPI, UploadFile, File, Form
from . import tracker, model, dummy_model  

app = FastAPI()

@app.post("/inference/player")
async def dummy_inference(file: UploadFile = File(...), frame_id: str = Form(...)):
    return {
        "video_info": {
            "frame_id": frame_id or "123",
            "width": 1920,
            "height": 1080
        },
        "tracking_results": [
            {
                "player_id": "player1",
                "bbox": [100, 150, 200, 300],
                "center": [150, 225],
                "confidence": 0.85
            }
        ]
    }
