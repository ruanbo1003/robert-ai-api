
from typing import Annotated
from fastapi import Header, HTTPException


async def get_auth_token_header(auth_token: Annotated[str, Header()]):
    if auth_token != "robert123":
        raise HTTPException(status_code=400, detail="Auth-Token header invalid")
