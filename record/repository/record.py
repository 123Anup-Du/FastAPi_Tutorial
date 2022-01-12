from fastapi import HTTPException, status
from sqlalchemy.orm import Session  
from .. import schemas, models

def get(id, db:Session):
    records = db.query(models.record).all()
    return records

def create(request:schemas.record,db:Session):
    new_record = models.record(Subject= request.subject, Remarks = request.remarks, user_id =1)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def destroy(id:int, db:Session):
    record= db.query(models.record).filter(models.record.id == id)
    if not record.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Record with the id {id} not found ')
    record.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:schemas.record, db:Session):
    record = db.query(models.record).filter(models.record.id == id)
    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'record with the id {id} is not found')
    record.update(request)
    db.commit()
    return update

def show(id:int, db:Session):
    record = db.query(models.record).filter(models.record.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'record details for ID {id} is not found')
    return record 