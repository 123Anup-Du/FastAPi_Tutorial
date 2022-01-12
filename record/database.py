from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE = 'sqlite:///./record.db'

engine = create_engine(SQLALCHEMY_DATABASE, connect_args ={'check_same_thread':False})

Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()