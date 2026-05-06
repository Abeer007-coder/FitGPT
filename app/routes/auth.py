print("AUTH FILE LOADED")
from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app import models
from app.schemas import UserCreate, UserLogin
from app.services.auth_service import hash_password
from app.services.auth_service import verify_password, create_access_token
from app.services.auth_service import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate):
    db = SessionLocal()

    hashed_pwd = hash_password(user.password)

    new_user = models.User(
        email=user.email,
        password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    return {"message": "User created"}



from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()

    db_user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email")

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }