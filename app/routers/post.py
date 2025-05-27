from .. import models, schemas, oauth2
from fastapi import FastAPI, Response, HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import List
from ..oauth2 import get_current_user
from typing import Optional

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user:str = Depends(get_current_user),Limit:int =10, Skip:int =0,search:Optional[str] = ""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(Skip).all()# if you only want users to see their own all posts,posts = db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
    return posts


# @router.post("", response_model=schemas.Post)
@router.post("", response_model=schemas.Post)
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user:str= Depends(get_current_user)
):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    if post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
async def update_post(
    id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
