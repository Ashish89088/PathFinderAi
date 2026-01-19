from pydantic import BaseModel
from typing import Optional, Dict, Any

class ProfileCreate(BaseModel):
    name: str
    age: int
    academics: Dict[str, Any]
    interests: Optional[str]
    hobbies: Optional[str]
    platforms: Dict[str, Any]

class ProfileResponse(BaseModel):
    user_id: str
    profile_id: str
    message: str
