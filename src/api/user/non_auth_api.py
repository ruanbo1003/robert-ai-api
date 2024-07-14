
import uuid
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from libs.encrypt import EncryptUtil
from orm.postgres.database import get_db
from orm.postgres.util.user import UserOrmUtil
from libs.response import ApiResponse
from .schema import UserSignup, UserExist, UserLogin


api_router = APIRouter()


@api_router.post("/login")
def signup(response: Response, login_user: UserLogin, db: Session = Depends(get_db)):
    user = UserOrmUtil.get_user_by_name(db, login_user.name)
    if not user:
        return ApiResponse(code=1001, message="username not exists.")

    auth_token = uuid.uuid4().hex
    UserOrmUtil.update_token(db, login_user.name, auth_token)
    response.set_cookie(key="authToken", value=auth_token, samesite='lax', secure=False, path='/', max_age=60*60*24*7,)
    return {
        'token': auth_token
    }


@api_router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    # print("signup:", user)

    user.password = EncryptUtil.hash_password(user.password)
    ret = UserOrmUtil.create_user(db, user)
    return ret


@api_router.post("/exist")
def signup(user: UserExist, db: Session = Depends(get_db)):
    user = UserOrmUtil.get_user_by_name(db, user.name)
    if user:
        return {'exist': True}
    else:
        return {'exist': False}
