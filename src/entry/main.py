
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from api.url import api_router, non_auth_api_router

from libs.response import ApiResponse
from orm.postgres import models
from orm.postgres.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI(default_response_class=ApiResponse)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(non_auth_api_router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
