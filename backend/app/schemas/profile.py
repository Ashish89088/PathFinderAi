from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class ProfileCreate(BaseModel):
    name: str
    age: Optional[int]

    academics: Dict[str, Any]
    interests: List[str]
    hobbies: List[str]
    platforms: Dict[str, Any]

class ProfileResponse(BaseModel):
    user_id: str
    profile_id: str
    message: str
