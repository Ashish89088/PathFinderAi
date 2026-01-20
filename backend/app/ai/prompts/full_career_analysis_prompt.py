def build_full_career_analysis_prompt(normalized_profile: dict) -> str:
    print("Building full career analysis prompt with profile:", normalized_profile)
    return f"""
You are an expert AI career advisor.

User normalized profile signals:
{normalized_profile}

Your task is to internally:
1. Infer key skills and traits
2. Match best career paths
3. Create a roadmap for each career
4. Suggest relevant opportunities aligned with the roadmap

Return JSON ONLY in the following format:

{{
  "skill_inference": {{
    "strengths": [],
    "weaknesses": [],
    "working_style": ""
  }},
  "career_matching": [
    {{
      "career": "",
      "reason": ""
    }}
  ],
  "roadmaps": {{
    "Career Name": []
  }},
  "opportunities": {{
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
}}

Rules:
- Be concise but high quality
- Align roadmaps and opportunities with career reasoning
- Do not include explanations outside JSON
"""
