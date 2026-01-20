# AI Orchestrator (Prompt Chaining)

from app.ai.gemini_client import GeminiClient
from app.ai.prompts.skill_inference import build_skill_inference_prompt
from app.ai.prompts.career_matching import build_career_matching_prompt
from app.ai.prompts.roadmap_builder import build_roadmap_prompt


def run_career_ai_pipeline(normalized_profile: dict) -> dict:
    client = GeminiClient()

    try:
        skill_prompt = build_skill_inference_prompt(normalized_profile)
        skill_response = client.generate(skill_prompt)

        career_prompt = build_career_matching_prompt(skill_response)
        career_response = client.generate(career_prompt)

        roadmap_prompt = build_roadmap_prompt(career_response)
        roadmap_response = client.generate(roadmap_prompt)

        return {
            "status": "success",
            "skill_inference": skill_response,
            "career_matching": career_response,
            "roadmap": roadmap_response
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }

