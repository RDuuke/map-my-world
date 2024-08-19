from pydantic import BaseModel, UUID4


class AddLastReviewedCommand(BaseModel):
    uuid: UUID4

