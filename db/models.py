from .database import Base
from sqlalchemy import *
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(Text)
    email = Column(Text)
    password = Column(Text)
    items = relationship('DbPost', back_populates='user')
    
class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    img_url = Column(Text)
    img_url_type = Column(Text)
    caption = Column(Text)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='items')
    comments = relationship('DbComment', back_populates='post')

    
class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True, index = True)
    text = Column(Text)
    username = Column(Text)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("DbPost", back_populates="comments")