from urllib import request
from fastapi import APIRouter,Depends,HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import *
from Hashing import Hash
from auth.oauth2 import create_access_token
router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(req: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credentials')
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='incorrect password')
    access_token = create_access_token(data={'username': user.username})
    
    return {
        'access_token' : access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }