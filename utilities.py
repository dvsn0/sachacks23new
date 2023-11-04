from typing import Any, Dict, List


def print_emotions(emotions: List[Dict[str, Any]]) -> None:
    emotion_map = {e["name"]: e["score"] for e in emotions}
    count = 0
    totalValence = 0
    for emotion in ["Sadness", "Anger", "Anxiety", "Distress", "Disappointment"]:
        totalValence = totalValence + round(emotion_map[emotion], 2)
        count += 1
    return totalValence / count
    