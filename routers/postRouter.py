
from random import random
import shutil
from typing import List
from fastapi import APIRouter
from routers.schemas import PostDAO, PostDTO, UserDAO, UserDTO
from sqlalchemy.orm.session import Session
from fastapi import Depends,HTTPException, status,UploadFile,File
from db.database import get_db
import db.postRepo as postRepo
import random,string
from routers.schemas import *
from auth.oauth2 import get_current_user
from typing import List

router = APIRouter(prefix='/post', tags=['post'])
image_url_types = ['absolute', 'relative']

@router.post('', response_model=PostDTO)
def create_post(req: PostDAO, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if req.img_url_type not in image_url_types:
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Parameter img type is not valid')
    return postRepo.create_post(db,req)

@router.get('/all',response_model=List[PostDTO])
def get_all_posts(db: Session = Depends(get_db)):
    return postRepo.get_all_posts(db=db)

@router.post('/image')
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for _ in range(3))
    new_prefix = f'_{rand_str}.'
    filename = new_prefix.join(image.filename.rsplit('.',1))
    
    path = f'images/{filename}'
    
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
        
        return {'filename': path}
    
@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
  return postRepo.delete_post(db, id, current_user.id)

    
        
