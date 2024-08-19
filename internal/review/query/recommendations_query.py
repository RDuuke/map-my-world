from datetime import datetime

from pydantic import BaseModel


class ReviewRecommendationsQuery(BaseModel):
    deadline: datetime
