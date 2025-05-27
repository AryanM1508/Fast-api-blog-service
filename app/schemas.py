from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr
class Post(BaseModel):#creating a class Post that inherits from BaseModel this is a pydantic model
    title: str
    content: str
    published: bool = True
    
    
class PostBase(BaseModel):#creating a class PostBase that inherits from BaseModel this is a pydantic model
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):#creating a class PostCreate that inherits from PostBase this is a pydantic model
    pass
class UserOut(BaseModel):#creating a class UserOut that inherits from BaseModel this is a pydantic model
    id:int
    email: str
    create_at: datetime
    class Config:
        orm_mode = True
class Post(PostBase):#creating a class Post that inherits from BaseModel this is a pydantic mode
    id:int
    owner_id: int
    owner:UserOut
    class Config:
        orm_mode = True
    
class UserCreate(BaseModel):#creating a class UserCreate that inherits from BaseModel this is a pydantic model
    email: str
    password: str
    class Config:
        orm_mode = True

        
        
class UserLogin(BaseModel):#creating a class UserLogin that inherits from BaseModel this is a pydantic model
    username: EmailStr
    password: str
    
    class Config:
        orm_mode = True


class Token(BaseModel):#creating a class Token that inherits from BaseModel this is a pydantic model
    access_token: str
    token_type: str
    
class TokenData(BaseModel):#creating a class TokenData that inherits from BaseModel this is a pydantic model
    id: int | None = None  # Using Union to allow for None type, or you can use Optional[int]
    
    class Config:
        orm_mode = True  # This allows the model to work with ORM objects