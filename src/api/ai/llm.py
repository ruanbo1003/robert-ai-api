
from fastapi import APIRouter


router = APIRouter()


@router.post("/chat/openai")
def openai_chat():
    return {
        "reply": "openai"
    }


@router.post("/chat/gemini")
def gemini_chat():
    return {
        "reply": "gemini"
    }
