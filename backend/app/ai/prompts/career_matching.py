def build_career_matching_prompt(skill_profile: dict) -> str:
    return f"""
You are an expert career counselor.

Based on the following skill profile, suggest the TOP 3 most suitable career fields.

Skill Profile:
{skill_profile}

For each career field, explain:
- Why it fits the user
- Required skills
- Future growth potential

Respond ONLY in valid JSON:
{{
  "career_matches": [
    {{
      "career_field": string,
      "reasoning": string,
      "required_skills": [string],
      "growth_outlook": string
    }}
  ]
}}
"""
