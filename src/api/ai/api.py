import os

from fastapi import APIRouter
import google.generativeai as genai
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from api.ai.schema import AiTranslate
from libs.env import Env
from libs.response import ApiResponse

router = APIRouter()


@router.post("/translate")
def translate(data: AiTranslate):
    if data.model == "DeepSeek":
        base_url, api_key = os.getenv("DEEPSEEK_KEY").split('[:]')
        model = "deepseek-chat"
    else:
        base_url, api_key = os.getenv("OPENAI_KEY").split('[:]')
        model = "gpt-4o"

    model = ChatOpenAI(
        openai_api_base=base_url,
        api_key=api_key,
        model=model,
        max_tokens=8192
    )

    translate_template = (
        f"You are a skilled translator, if someone enters English, you translate it to Chinese, "
        f"and if someone enters Chinese, translate it to English, try to make the translate briefly. ")
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", translate_template),
            ("user", "{text}")
        ]
    )
    prompt = prompt_template.invoke(
        {
            "text": data.content
        }
    )
    resp = model.invoke(prompt)
    # print(resp.content)
    return ApiResponse(content=resp.content)


@router.post("/thousands_why")
def thousands(data: AiTranslate):
    if not data.content:
        return ApiResponse(code=1002, message="please enter your content.")

    scene = "坐在摩托车上快速行驶中，能感受到有风吹在脸上"
    question = "风是哪来的呢？"
    prompt = f""""
        你是一个育儿专家，可以回答儿童的问题，你的回复可以使通俗易懂，并使儿童保持好奇心。现在有一个场景:{scene}, 一个 3 岁的儿童问: {question},请给出你的回复。
    """
    genai.configure(api_key=Env.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return ApiResponse(content=response.text)
