def run_dummy_inference(file_path: str):
    # Dummy output schema
    return {
        "video_info": {
            "filename": file_path,
            "duration": 12.34,
            "fps": 30
        },
        "tracking_results": [
            {
                "player_id": 1,
                "bbox": [100, 150, 200, 250],
                "confidence": 0.95
            }
        ]
    }
