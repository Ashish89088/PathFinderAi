from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.profile import ProfileCreate, ProfileResponse
from app.models.user import User
from app.models.profile import Profile
from app.core.database import SessionLocal

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

    return {
        "user_id": str(user.id),
        "profile_id": str(profile.id),
        "message": "Profile data stored successfully"
    }
