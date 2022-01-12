from fastapi import FastAPI, APIRouter
from .database import engine
from .routers import record,user,authentication
from . import models

app = FastAPI()

models.base.metadata.create_all(engine)



app.include_router(authentication.router)
app.include_router(record.router)
app.include_router(user.router)