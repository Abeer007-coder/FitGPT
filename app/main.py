from fastapi import FastAPI
from app.routes import health
from app.database import engine, Base
from app import models
from app.routes import auth



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Fitness AI API is running 🚀"}
print("AUTH ROUTES LOADED")