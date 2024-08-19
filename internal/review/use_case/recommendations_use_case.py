from typing import List

from internal.review.model import Review
from internal.review.query import ReviewRecommendationsQuery
from internal.review.repository import ReviewRepository


class ReviewRecommendationUseCase:
    """
    Use case for generating review recommendations.
    """

    def __init__(self, repository: ReviewRepository):
        """
        Initializes the ReviewRecommendationUseCase with the provided repository.

        Args:
            repository (ReviewRepository): The repository used to fetch review data.
        """
        self.repository = repository

    async def execute(self, query: ReviewRecommendationsQuery) -> List[Review]:
        """
        Executes the recommendation logic to find unreviewed or old reviews.

        Args:
            query (ReviewRecommendationsQuery): The query object containing the deadline for filtering reviews.

        Returns:
            A list of `Review` objects that meet the recommendation criteria (unreviewed or older than the deadline).
        """
        return await self.repository.find_unreviewed_old(deadline=query.deadline)
