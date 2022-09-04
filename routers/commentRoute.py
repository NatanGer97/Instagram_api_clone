from fastapi import  *
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from db import commentRepo
from routers.schemas import *
from db.models import *


router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.get('/all/{postId}')
def get_comments(postId: int, db: Session = Depends(get_db)):
    return commentRepo.get_all(db,postId)

@router.post('')
def createNewComment(req: CommentDAO, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return commentRepo.create(db,req)