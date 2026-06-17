from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-3.1-flash-lite")

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    try:
        response = model.generate_content(req.message)

        return {
            "success": True,
            "reply": response.text
        }

    except ResourceExhausted:
        return {
            "success": False,
            "reply": "⚠️ Gemini API quota exceeded. Please try again later."
        }