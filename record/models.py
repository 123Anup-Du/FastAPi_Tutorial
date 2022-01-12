from sqlalchemy.sql.schema import ForeignKey
from .database import base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class record(base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True, index=True)
    Subject= Column(String)
    #Marks = Column(Integer)
    Remarks = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    creator = relationship('user', back_populates='records')


class user(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    records = relationship('record', back_populates='creator')

