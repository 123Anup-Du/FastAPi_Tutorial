from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..repository import user 
from ..hashing import hash



router = APIRouter(
    prefix = '/User',
    tags= ['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.showuser)
def create_user(request: schemas.user, db:Session= Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.showuser)
def get_user(id=int, db:Session = Depends(get_db)):
    return user.show(id,db)