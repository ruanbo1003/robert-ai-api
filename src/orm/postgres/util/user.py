
from sqlalchemy.orm import Session
from api.user import schema as UserSchema
from orm.postgres import models


class UserOrmUtil:
    @staticmethod
    def create_user(db: Session, user: UserSchema.UserSignup):
        db_user = models.User(name=user.name, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def get_user_by_name(db: Session, name: str):
        return db.query(models.User).filter(models.User.name == name).first()
