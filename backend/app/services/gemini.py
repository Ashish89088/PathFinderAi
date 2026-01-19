def analyze_career(profile: dict):
    return {
        "career_fields": ["Software Engineering", "Product Management"],
        "reasoning": "Strong analytical skills, consistency in coding platforms",
        "roadmap": {
            "short_term": ["DSA", "Projects"],
            "mid_term": ["Internships", "Certifications"],
            "long_term": ["Specialization", "Leadership"]
        }
    }


import time

def call_gemini(normalized_profile: dict) -> dict:
    """
    Mock Gemini 3 call.
    Replace this with real Gemini SDK later.
    """
    start = time.time()

    # simulate latency
    time.sleep(1)

    result = {
        "skill_inference": "User shows strong analytical thinking and discipline.",
        "career_matching": [
            {
                "career": "Software Engineer",
                "reason": "High tech inclination and coding presence"
            },
            {
                "career": "Product Manager",
                "reason": "Interest in startups and product thinking"
            }
        ],
        "roadmap": {
            "Software Engineer": [
                "Master DSA",
                "Build 3 real-world projects",
                "Apply for internships"
            ]
        },
        "opportunities": {
            "certifications": ["Google Cloud", "AWS"],
            "events": ["Hackathons", "Tech Meetups"]
        }
    }

    print(f"Gemini latency: {round(time.time() - start, 2)}s")

    return result

