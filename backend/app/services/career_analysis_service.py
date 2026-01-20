from sqlalchemy.orm import Session
from app.models.career_analysis import CareerAnalysis
from app.services.ai_parser import parse_gemini_output

def save_career_analysis(
    db: Session,
    user_id,
    profile_id,
    gemini_result: dict
):
    print("Gemini result:", gemini_result)

    parsed = parse_gemini_output(gemini_result)


    analysis = CareerAnalysis(
        user_id=user_id,
        inferred_traits=parsed["inferred_traits"],
        career_recommendations=parsed["career_recommendations"],
        roadmaps=parsed["roadmaps"],
        opportunities=parsed["opportunities"],
        raw_ai_output=gemini_result
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis
