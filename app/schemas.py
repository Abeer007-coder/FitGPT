from pydantic import BaseModel
from typing import Optional

class HealthInput(BaseModel):
    age: int
    gender: str
    height: float
    weight: float
    activity_level: Optional[str] = None
    goal: Optional[str] = None
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str    