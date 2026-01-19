def build_roadmap_prompt(career_match: dict) -> str:
    return f"""
You are a career roadmap strategist.

For the selected career paths below, create a step-by-step roadmap.

Career Matches:
{career_match}

For EACH career, include:
- Beginner → Advanced roadmap
- Exams (if any)
- Certifications
- Courses
- Hackathons / events
- Entry-level opportunities

Respond ONLY in valid JSON:
{{
  "roadmaps": [
    {{
      "career_field": string,
      "steps": [string],
      "exams": [string],
      "certifications": [string],
      "courses": [string],
      "events": [string],
      "opportunities": [string]
    }}
  ]
}}
"""
