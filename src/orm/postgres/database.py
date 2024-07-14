from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from libs.env import Env

SQLALCHEMY_DATABASE_URL = Env.POSTGRES_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# each instance of SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a Base class use the function declarative_base()
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
