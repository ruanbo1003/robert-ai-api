
from fastapi import APIRouter, Response

api_router = APIRouter()


@api_router.get("/non_auth_1")
def signup(response: Response):
    return {
        'token': "abc"
    }
