from pydantic import BaseModel


class CategoryCommand(BaseModel):
    name: str
