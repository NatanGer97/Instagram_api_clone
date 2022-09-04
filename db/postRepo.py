
from fastapi import HTTPException, status
from random import seed
from routers.schemas import *
from db.models import *
from sqlalchemy.orm.session import Session
from Hashing import Hash

def create_post(db: Session, req: PostDAO):
    new_post = DbPost(
        img_url = req.img_url,
        img_url_type = req.img_url_type,
        caption = req.caption,
        timestamp = datetime.now(),
        user_id = req.creator_id
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


def get_all_posts(db: Session):
    return db.query(DbPost).all();
    



def delete_post(db: Session, postId: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == postId).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Post with id {id} not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
            detail='Only post creator can delete post')

    db.delete(post)
    db.commit()
    return 'ok'