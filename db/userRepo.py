
from routers.schemas import *
from fastapi import HTTPException, status
from db.models import *
from sqlalchemy.orm.session import Session
from Hashing import Hash

def create_user(db: Session, req: UserDAO):
    newUser = DbUser(
        username = req.username,
        email = req.email,
        password =  Hash.bcrypt(req.password),
    )
    
    db.add(newUser)
    db.commit()
    db.refresh(newUser);
    
    return newUser

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id:{username} not found')
    return user