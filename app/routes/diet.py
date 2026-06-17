from fastapi import APIRouter
from pydantic import BaseModel
import google.generativeai as genai
import time
from google.api_core.exceptions import ResourceExhausted

router = APIRouter()

class DietRequest(BaseModel):
    food_type: str

@router.post("/diet")
def generate_diet(req: DietRequest):

    prompt = f"""
    Create a complete one-day diet plan.

    Food Preference: {req.food_type}

    Include:

    Breakfast
    Mid Morning Snack
    Lunch
    Evening Snack
    Dinner

    Mention calories for each meal.

    Format in markdown.
    """

    model = genai.GenerativeModel("gemini-3.1-flash-lite")
    try:
        response = model.generate_content(prompt)
        return {
            "success": True,
            "reply": response.text
        }
    except ResourceExhausted:
        return {
            "success": False,
            "reply": "⚠️ Gemini API quota exceeded. Please try again later."
        }