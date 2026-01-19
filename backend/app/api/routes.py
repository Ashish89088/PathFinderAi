from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.profile import ProfileCreate, ProfileResponse
from app.models.user import User
from app.models.profile import Profile
from app.core.database import SessionLocal
from uuid import UUID


from app.services.profile_normalizer import normalize_profile
from app.ai.orchestrator import run_career_ai_pipeline
from app.services.gemini import call_gemini
from app.services.career_analysis_service import save_career_analysis


router = APIRouter(prefix="/api", tags=["Profile"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/profile", response_model=ProfileResponse)
def submit_profile(data: ProfileCreate, db: Session = Depends(get_db)):

    # 1. Create User
    user = User(
        name=data.name,
        age=data.age
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # 2. Create Profile
    profile = Profile(
        user_id=user.id,
        academics=data.academics,
        interests=data.interests,
        hobbies=data.hobbies,
        platforms=data.platforms
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)

    normalized_data = normalize_profile({
        "interests": data.interests,
        "hobbies": data.hobbies,
        "academics": data.academics,
        "platforms": data.platforms
    })

    print("NORMALIZED PROFILE:", normalized_data)

    ai_result = run_career_ai_pipeline(normalized_data)

    print("AI RESULT:", ai_result)



    return {
        "user_id": str(user.id),
        "profile_id": str(profile.id),
        "message": "Profile data stored successfully"
    }

from app.models.profile import Profile
    

@router.post("/analyze-profile")
# def analyze_profile(
#     user_id: UUID,
#     db: Session = Depends(get_db)
# ):
def analyze_profile(user_id: UUID, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # 1. Load normalized profile
    # normalized_profile = get_normalized_profile(user_id)
    normalized_profile = normalize_profile(profile)

    # 2. Call Gemini
    gemini_result = call_gemini(normalized_profile)

    # 3. Save analysis
    analysis = save_career_analysis(
        db=db,
        user_id=user_id,
        profile_id=None,
        gemini_result=gemini_result
    )

    # 4. Return frontend-safe response
    return {
        "status": "success",
        "analysis_id": str(analysis.id),
        "inferred_traits": analysis.inferred_traits,
        "career_recommendations": analysis.career_recommendations,
        "roadmaps": analysis.roadmaps,
        "opportunities": analysis.opportunities
    }

