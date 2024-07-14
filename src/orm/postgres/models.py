
from sqlalchemy import Boolean, Column, Integer, String, Date

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    token = Column(String, unique=True, index=True)
    login_time = Column(Date)
