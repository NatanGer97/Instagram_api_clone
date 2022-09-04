
from fastapi import APIRouter

from routers.schemas import UserDAO, UserDTO
from sqlalchemy.orm.session import Session
from fastapi import Depends
from db.database import get_db
import db.userRepo as userRepo

router = APIRouter(prefix='/user', tags=['user'])

@router.post('', response_model=UserDTO)
def create_user(req: UserDAO, db: Session = Depends(get_db)):
    return userRepo.create_user(db,req)
