from datetime import datetime
from typing import List

from internal.review import ReviewRepository
from internal.review.model import Review


class ReviewRecommendationUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    async def execute(self, deadline: datetime) -> List[Review]:
        return await self.repository.find_unreviewed_old(deadline=deadline)
