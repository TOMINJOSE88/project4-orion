# tracker.py

import random

def track_players(video_id: str, frame_number: int, total_players: int = 5):
    """
    Generate dummy tracking results for a given frame in a video.
    
    Parameters:
        video_id (str): Unique identifier for the video
        frame_number (int): Frame number being processed
        total_players (int): Number of players to simulate tracking for

    Returns:
        dict: Tracking results for the frame
    """
    results = {
        "video_id": video_id,
        "frame_number": frame_number,
        "players": []
    }

    for player_id in range(1, total_players + 1):
        width = random.randint(40, 60)
        height = random.randint(80, 100)
        center_x = random.randint(100, 500)
        center_y = random.randint(100, 400)

        player_data = {
            "player_id": f"P{player_id}",
            "bbox": {
                "x": center_x - width // 2,
                "y": center_y - height // 2,
                "width": width,
                "height": height
            },
            "center": {
                "x": center_x,
                "y": center_y
            },
            "confidence": round(random.uniform(0.7, 1.0), 2)
        }

        results["players"].append(player_data)

    return results
