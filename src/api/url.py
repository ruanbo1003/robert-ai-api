
from fastapi import APIRouter, Depends
from api.user import api as UserApi
from api.user import non_auth_api as NonAuthUserApi
from api.ai import api as AiApi
from api.test import api as TestApi
from api.test import non_auth_api as NonAuthTestApi
from api.bookmark import api as BookmarkApi

from .dependencies import get_auth_token_header


# router must have the `Auth-Token` header
api_router = APIRouter(dependencies=[Depends(get_auth_token_header)])

# test apis
api_router.include_router(TestApi.router, prefix='/api/test', tags=['test'])
# user
api_router.include_router(UserApi.api_router, prefix='/api/user', tags=['user'])
# ai
api_router.include_router(AiApi.router, prefix='/api/ai', tags=['ai'])
# bookmark
api_router.include_router(BookmarkApi.api_router, prefix='/api/bookmark', tags=['bookmark'])


# router do not need the `Auth-Token` header
non_auth_api_router = APIRouter()
# test
non_auth_api_router.include_router(NonAuthTestApi.api_router, prefix='/api/test', tags=['non-auth-test'])
# user
non_auth_api_router.include_router(NonAuthUserApi.api_router, prefix='/api/user', tags=['non-auth-user'])
