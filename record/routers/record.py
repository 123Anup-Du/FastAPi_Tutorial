from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import database, schemas, models, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import record


router = APIRouter(
    prefix='/record',
    tags=['Records']
)

get_db = database.get_db


@router.get('/', response_model= List[schemas.showrecord])
def all(db: Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    return record.get(id,db)

@router.post('/',status_code=201)
def create(request:schemas.record, db:Session= Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    return record.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
def destroy(id:int, db:Session=Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    return record.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.record,db:Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    return record.update(id,request,db)

@router.get('/{id}', status_code= 200, response_model= schemas.showrecord)
def show(id:int, response:Response, db: Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    return record.show(id,db)
