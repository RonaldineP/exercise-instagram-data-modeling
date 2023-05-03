import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import datetime

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    #date = DateTime(onupdate=datetime.datetime.now)
    title = Column(String(60), nullable=False)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer,primary_key=True)   
    comment = Column(String(250),nullable=False)
    username = Column(String(60),nullable=False)
    post_id =Column(Integer, ForeignKey('post'))
    post = relationship(Post)

class Like_Dislike(Base):
    __tablename__ = 'like_dislike'
    id = Column(Integer, primary_key=True)
    like = Column(Integer,nullable=False)
    dislike = Column(Integer,nullable=False)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
