from fastapi import FastAPI
from .import models
from app.database import engine
from app import models
from app.routers import post,user,auth
from .config import settings

models.Base.metadata.create_all(bind=engine)


app= FastAPI()#created an instance of FastAPI


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

