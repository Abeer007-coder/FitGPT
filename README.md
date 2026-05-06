
# Fitness AI API

A FastAPI-based backend application for fitness analysis with JWT authentication.

## Features
- User Signup & Login (JWT Auth)
- BMI & BMR Calculation
- Calorie Recommendations
- Activity-based analysis
- Protected Routes
- User History Tracking

## Tech Stack
- FastAPI
- Python
- SQLAlchemy
- SQLite
- JWT (OAuth2)
- Passlib (bcrypt)

## API Endpoints
- POST /signup
- POST /login
- POST /analyze
- GET /history

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
