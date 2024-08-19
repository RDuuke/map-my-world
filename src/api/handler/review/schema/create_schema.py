from pydantic import BaseModel, UUID4


class ReviewCreateSchema(BaseModel):
    location_id: UUID4
    category_id: UUID4

