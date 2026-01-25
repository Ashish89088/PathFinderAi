def build_opportunities_prompt(career_match: dict, roadmap_match: dict) -> dict:
    career = career_match.get("career", "")
    reasoning = career_match.get("reason", "")

    roadmap_steps = roadmap_match.get(career, [])



    return f"""
    You are an expert career advisor and hiring mentor.

    Career:
    {career}

    Career Context:
    {reasoning}

    Roadmap Steps:
    {roadmap_steps}

    Your task:
    Generate relevant opportunities that DIRECTLY support the roadmap steps
    and help the user progress in this career.

    Rules:
    - Align certifications with roadmap skills
    - Suggest internships or roles matching the career
    - Recommend platforms useful for roadmap execution
    - Include communities/events that improve exposure

    Return JSON ONLY in this exact format:

    {{
    "certifications": [
        {{
        "name": "",
        "why": ""
        }}
    ],
    "internships_roles": [
        {{
        "role": "",
        "why": ""
        }}
    ],
    "platforms": [
        {{
        "name": "",
        "why": ""
        }}
    ],
    "events_communities": [
        {{
        "name": "",
        "why": ""
        }}
    ]
    }}
    """
