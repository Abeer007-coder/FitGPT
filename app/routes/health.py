from fastapi import APIRouter
from app.schemas import HealthInput
from app.services.bmi_service import calculate_bmi
from app.database import SessionLocal
from app import models
from app.routes.auth import get_current_user
from fastapi import Depends


router = APIRouter()

@router.post("/analyze")
def analyze_health(data: HealthInput, user=Depends(get_current_user)):

    db = SessionLocal()

    height_m = data.height / 100
    bmi = data.weight / (height_m ** 2)

    # BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # BMR
    if data.gender.lower() == "male":
        bmr = 10 * data.weight + 6.25 * data.height - 5 * data.age + 5
    else:
        bmr = 10 * data.weight + 6.25 * data.height - 5 * data.age - 161

    # Activity multiplier
    activity_map = {
        "low": 1.2,
        "moderate": 1.55,
        "high": 1.9
    }

    activity_factor = activity_map.get(data.activity_level.lower(), 1.2)

    daily_calories = bmr * activity_factor

    # Goal adjustment
    if data.goal.lower() == "lose":
        target_calories = daily_calories - 500
        advice = "Calorie deficit, cardio + light strength training"
    elif data.goal.lower() == "gain":
        target_calories = daily_calories + 500
        advice = "Calorie surplus, focus on strength training"
    else:
        target_calories = daily_calories
        advice = "Maintain your current routine"

    # Save to DB
    record = models.HealthRecord(
        age=data.age,
        gender=data.gender,
        height=data.height,
        weight=data.weight,
        bmi=bmi,
        category=category,
        calories=target_calories,
        user_email=user
    )

    db.add(record)
    db.commit()

    return {
        "bmi": round(bmi, 2),
        "category": category,
        "bmr": round(bmr, 2),
        "activity_level": data.activity_level,
        "maintenance_calories": round(daily_calories, 2),
        "target_calories": round(target_calories, 2),
        "goal": data.goal,
        "advice": advice
    }
@router.get("/records")
def get_records():
    db = SessionLocal()
    records = db.query(models.HealthRecord).all()
    return records
@router.get("/progress")
def get_progress():
    db = SessionLocal()
    data = db.query(models.HealthRecord).all()

    return [
        {
            "date": r.id,
            "weight": r.weight,
            "bmi": r.bmi
        } for r in data
    ]

    return {
        "bmi": bmi,
        "category": category,
        "calories": calories,
        "message": "Data saved successfully"
    }
@router.get("/history")
def get_history(user=Depends(get_current_user)):
    db = SessionLocal()

    data = db.query(models.HealthRecord).filter(
        models.HealthRecord.user_email == user
    ).all()

    return data