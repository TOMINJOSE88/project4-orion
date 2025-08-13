def run_dummy_inference(file_path: str):
    return {
        "video_info": {
            "file_name": file_path,
            "frame_rate": 30,
            "resolution": "1920x1080"
        },
        "tracking_results": [
            {
                "player_id": 1,
                "bbox": [100, 150, 50, 80],
                "center": [125, 190],
                "confidence": 0.95
            }
        ]
    }
