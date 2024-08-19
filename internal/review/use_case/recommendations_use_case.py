from typing import List

from internal.review import ReviewRepository
from internal.review.model import Review
from internal.review.query import ReviewRecommendationsQuery


class ReviewRecommendationUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    async def execute(self, query: ReviewRecommendationsQuery) -> List[Review]:
        return await self.repository.find_unreviewed_old(deadline=query.deadline)
