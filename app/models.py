
from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from sqlalchemy import DateTime
from datetime import datetime

created_at = Column(DateTime, default=datetime.utcnow)


class HealthRecord(Base):
    __tablename__ = "health_records"
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    bmi = Column(Float)
    category = Column(String)
    user_email = Column(String)
    calories = Column(Float)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)    