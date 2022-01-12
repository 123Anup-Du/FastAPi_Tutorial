from pydantic import BaseModel
from typing import List, Optional




class recordbase(BaseModel):
    subject: str
    #marks: int
    remarks: str

class record(recordbase):
    class config:
        orm_mode = True


class user(BaseModel):
    name: str
    email: str
    password: str

class showuser(BaseModel):
    name: str
    email: str
    record : List[record]
    class Config:
        orm_mode = True 

class showrecord(BaseModel):
    subject: str
    #marks: int
    remarks: str
    creator: showuser

    class Config:
        orm_mode = True

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    acess_token: str
    token_type: str

class Tokendata(BaseModel):
    email: Optional[str] = None