from pydantic import BaseModel, UUID4


class AddLastReviewedCommand(BaseModel):
    id: UUID4

