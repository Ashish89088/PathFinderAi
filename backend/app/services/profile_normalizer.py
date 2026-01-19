from typing import Dict, Any, List

TECH_KEYWORDS = [
    "ai", "machine learning", "backend", "frontend",
    "programming", "coding", "software", "data"
]

CREATIVE_KEYWORDS = [
    "design", "art", "music", "writing", "content",
    "video", "photography"
]

SPORTS_KEYWORDS = [
    "cricket", "football", "sports", "gym", "fitness"
]


def score_from_keywords(values: List[str], keywords: List[str]) -> float:
    if not values:
        return 0.0

    count = 0
    for v in values:
        v_lower = v.lower()
        if any(k in v_lower for k in keywords):
            count += 1

    return round(min(count / len(values), 1.0), 2)

def normalize_profile(profile: Dict[str, Any]) -> Dict[str, Any]:
    # interests = profile.get("interests", []) or []
    # hobbies = profile.get("hobbies", []) or []
    # academics = profile.get("academics", {}) or {}
    # platforms = profile.get("platforms", {}) or {}
    interests = profile.interests or []
    hobbies = profile.hobbies or []
    academics = profile.academics or []
    platforms = profile.platforms or []

    tech_score = score_from_keywords(interests, TECH_KEYWORDS)
    creative_score = score_from_keywords(hobbies, CREATIVE_KEYWORDS)
    sports_score = score_from_keywords(hobbies, SPORTS_KEYWORDS)

    discipline_score = 0.5
    if "cgpa" in academics:
        try:
            cgpa = float(academics["cgpa"])
            discipline_score = min(cgpa / 10, 1.0)
        except:
            pass

    coding_presence = 0.0
    if platforms.get("leetcode") or platforms.get("github"):
        coding_presence = 0.8

    return {
        "signals": {
            "tech_inclination": tech_score,
            "creativity": creative_score,
            "sports_orientation": sports_score,
            "discipline": round(discipline_score, 2),
            "coding_presence": coding_presence
        },
        "raw_summary": {
            "interests": interests,
            "hobbies": hobbies,
            "academics": academics,
            "platforms": list(platforms.keys())
        }
    }
