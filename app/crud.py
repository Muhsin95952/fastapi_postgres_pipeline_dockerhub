from sqlalchemy.orm import Session
from . import models, schemas


def get_posts(db: Session):
    return db.query(models.Post).all()


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    if post:
        db.delete(post)
        db.commit()
    return post
