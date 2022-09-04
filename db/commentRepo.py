from datetime import datetime
from sqlite3 import Timestamp
from sqlalchemy.orm import Session
from db.models import DbComment
from routers.schemas import CommentDAO

def create(db: Session, req: CommentDAO):
    newComment = DbComment(
        text = req.text,
        username = req.username,
        post_id = req.post_id,
        timestamp = datetime.now()
    )
    
    db.add(newComment)
    db.commit()
    db.refresh(newComment)
    return newComment

def get_all(db: Session, post_id: int):
    return db.query(DbComment).filter(DbComment.id == post_id).all()