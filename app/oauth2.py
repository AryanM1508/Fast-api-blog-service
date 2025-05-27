from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from . import schemas
from fastapi import HTTPException, status,Depends, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import database, models
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#SECRET_KEY
#Algorithm
#Expiration time


SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return user_id  # ✅ This return is critical
    except JWTError:
        raise credentials_exception


def get_current_user(
    token: str ,
    db: Session = Depends(database.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    user_id = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise credentials_exception  # Optional, extra safe

    return user

    """
    This function decodes the JWT token and retrieves the current user.
    If the token is invalid or expired, it raises an exception.
    """   