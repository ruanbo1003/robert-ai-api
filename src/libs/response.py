
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Any


class ApiResponse(JSONResponse):
    def __init__(self, content: Any = None, code: int = 0, message: str = "", **kwargs):
        self.custom_content = {
            "code": code,
            "message": message,
            "data": content
        }
        super().__init__(content=self.custom_content, **kwargs)
