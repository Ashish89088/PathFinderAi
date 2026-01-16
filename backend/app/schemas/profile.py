from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class ProfileCreate(BaseModel):
    name: str
    age: Optional[int] = None
    academics: Optional[Dict[str, Any]] = None
    interests: Optional[List[str]] = None
    hobbies: Optional[List[str]] = None
    platforms: Optional[Dict[str, Any]] = None

    


class ProfileResponse(BaseModel):
    user_id: str
    profile_id: str
    message: str
