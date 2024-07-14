
import time
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from .schema import TestAddItem
from libs.response import ApiResponse


router = APIRouter()


@router.get("/hi")
def hi():
    return {
        "reply": "hello"
    }


@router.post("/add")
def add(item: TestAddItem):
    return {
        'name': item.name
    }


@router.get('/delay')
def delay():
    time.sleep(5)
    return {
        'code': 0
    }


@router.get('/resp')
def response():
    return {
        'reply': 'ok'
    }


class TestApiUser(BaseModel):
  name: str
  age: int


@router.get('/user')
def response():
    # return User(name='ok', age=10)
    return TestApiUser(name='Jack', age=20)


@router.get('/invalid_user')
def response():
    return ApiResponse(code=1001, message="invalid user")


# for debug apis
@router.get('/debug/basic_get')
def basic_get():
    return {
        'reply': 'ok'
    }


@router.get('/debug/get_parameters')
def get_parameters(name: str, age: int):
    return {
        'name': name,
        'age': age
    }


class DebugPostData(BaseModel):
    name: str
    age: int


@router.post('/debug/post_data')
def post_data(data: DebugPostData):
    print(f"post_data:", data)

    return {
        'name': data.name,
        'email': 'a@g.com'
    }


@router.post('/debug/post_data_401')
def post_data(data: DebugPostData):
    print(f"post_data_401:", data)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key"
    )


@router.get("/get_401")
def response_401():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key"
    )
