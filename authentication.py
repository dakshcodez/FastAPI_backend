from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Dict
from models import User

users_db: Dict[str, Dict] = {}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return User(**user)
