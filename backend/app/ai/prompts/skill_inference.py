def build_skill_inference_prompt(normalized_profile: dict) -> str:
    signals = normalized_profile["signals"]
    summary = normalized_profile["raw_summary"]

    return f"""
You are an expert career psychologist and skill assessor.

Given the following behavioral signals and background summary, infer the user's
core skills, strengths, weaknesses, and working style.

Behavioral Signals:
{signals}

Background Summary:
{summary}

Respond ONLY in valid JSON with the following structure:
{{
  "core_skills": [string],
  "soft_skills": [string],
  "strengths": [string],
  "weaknesses": [string],
  "learning_style": string
}}
"""
