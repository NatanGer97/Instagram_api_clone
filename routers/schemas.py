from typing import List
from  datetime import datetime
from pydantic import *

class UserDAO(BaseModel):
    username: str
    email: str
    password: str

class UserDTO(BaseModel):
    username: str
    email: str    
    class Config():
        orm_mode = True;
        
        
class PostDAO(BaseModel):
    img_url: str
    img_url_type: str
    caption: str
    creator_id: int

class User(BaseModel):
    username: str
    class Config():
        orm_mode = True
        
class Comment(BaseModel):
    # comment which will be part of each post
    username: str
    text: str
    timestamp: datetime
    class Config():
        orm_mode = True
    

class PostDTO(BaseModel):
    id: int
    img_url: str
    img_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]    
    class Config():
        orm_mode = True
        
class UserAuth(BaseModel):
    id: int
    username: str
    email: str
    
class CommentDAO(BaseModel):
    username:str
    text: str
    post_id: int
