from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, database, schemas
from ..hashing import hash



def create_user(request:schemas.user, db:Session):
    hashedPassword = hash.bcrypt(request.password)
    new_user = models.user(name =request.name,email=request.email,password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db:Session):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'User name with id {id} not found')
    return user