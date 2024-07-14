
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from orm.postgres.database import get_db
from orm.postgres.util.user import UserOrmUtil


api_router = APIRouter()


@api_router.post("/logout")
def signup(response: Response, db: Session = Depends(get_db)):
    # auth_token = uuid.uuid4().hex
    response.delete_cookie(key="authToken", path='/', samesite='lax', secure=False)
    return True


@api_router.get("/{user_id}")
def user_info(user_id: int, db: Session = Depends(get_db)):
    # return {
    #     "email": 'a@g.com',
    #     "name": 'robert',
    # }
    user = UserOrmUtil.get_user(db, user_id)
    return {
        'id': user.id,
        'name': user.name,
        'is_active': user.is_active
    }
