
from fastapi import APIRouter

from api.ai.schema import LlmTranslate


router = APIRouter()


@router.post("/translate")
def translate(content: LlmTranslate):
    return {
        "reply": "translate"
    }


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
