from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import health, auth, chat
from app.database import engine, Base
from app.routes import diet


# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(health.router)
app.include_router(chat.router)
app.include_router(diet.router)


@app.get("/")
def home():
    return {
        "message": "FitGPT AI API is running 🚀"
    }

print("AUTH ROUTES LOADED")