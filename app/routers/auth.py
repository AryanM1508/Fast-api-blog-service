from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, schemas, utils,oauth2


router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credentials:schemas.UserLogin ,db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return{"access token":access_token,"token type":"bearer"}
