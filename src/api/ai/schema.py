
from pydantic import BaseModel


# translate
class AiTranslate(BaseModel):
    model: str
    content: str
