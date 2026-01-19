# def parse_gemini_output(skill_raw: str, career_raw: str, roadmap_raw: str):
#     """
#     Converts Gemini raw text → structured JSON
#     """

#     inferred_traits = {
#         "strengths": ["analytical thinking", "self-learning"],
#         "weaknesses": ["needs industry exposure"],
#         "working_style": "disciplined, growth-oriented"
#     }

#     career_recommendations = [
#         {
#             "career": "Software Engineer",
#             "reasoning": "Strong tech inclination and coding presence"
#         },
#         {
#             "career": "Product Manager",
#             "reasoning": "Interest in startups and product thinking"
#         },
#         {
#             "career": "Data Analyst",
#             "reasoning": "Analytical academics and structured thinking"
#         }
#     ]

#     roadmaps = {
#         "Software Engineer": [
#             "Master DSA",
#             "Build 3 real-world projects",
#             "Contribute to open source",
#             "Prepare system design"
#         ],
#         "Product Manager": [
#             "Learn product frameworks",
#             "Analyze real products",
#             "Build side projects",
#             "Apply for APM roles"
#         ]
#     }

#     opportunities = {
#         "certifications": ["Google Data Analytics", "AWS Cloud Practitioner"],
#         "internships": ["Startup PM Intern", "SDE Intern"],
#         "platforms": ["LinkedIn", "AngelList", "Wellfound"]
#     }

#     return {
#         "inferred_traits": inferred_traits,
#         "career_recommendations": career_recommendations,
#         "roadmaps": roadmaps,
#         "opportunities": opportunities
#     }


def parse_gemini_output(gemini_result: dict):
    """
    Converts Gemini raw dict → structured JSON
    """
    skill_raw = gemini_result.get("skill_inference", "")
    career_raw = gemini_result.get("career_matching", [])
    roadmap_raw = gemini_result.get("roadmap", {})
    opportunities_raw = gemini_result.get("opportunities", {})

    inferred_traits = {
        "strengths": ["analytical thinking", "self-learning"],
        "weaknesses": ["needs industry exposure"],
        "working_style": "disciplined, growth-oriented"
    }

    career_recommendations = career_raw or [
        {"career": "Software Engineer", "reasoning": "Strong tech inclination and coding presence"},
        {"career": "Product Manager", "reasoning": "Interest in startups and product thinking"}
    ]

    roadmaps = roadmap_raw or {
        "Software Engineer": ["Master DSA", "Build 3 real-world projects", "Contribute to open source", "Prepare system design"]
    }

    opportunities = opportunities_raw or {
        "certifications": ["Google Data Analytics", "AWS Cloud Practitioner"],
        "internships": ["Startup PM Intern", "SDE Intern"],
        "platforms": ["LinkedIn", "AngelList", "Wellfound"]
    }

    return {
        "inferred_traits": inferred_traits,
        "career_recommendations": career_recommendations,
        "roadmaps": roadmaps,
        "opportunities": opportunities
    }
