from passlib.context import CryptContext
pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")#creating an instance of CryptContext

def hash(password: str):
    return pwd_context.hash(password)#hashing the password

def verify(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)#verifying the password