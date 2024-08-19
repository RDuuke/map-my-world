from datetime import datetime

from internal.review.query import ReviewRecommendationsQuery
from internal.review.use_case import ReviewRecommendationUseCase
from src.api.handler import BaseHandler


class ReviewRecommendationHandler(BaseHandler):
    """
    Handler for fetching review recommendations.
    """

    def __init__(self, use_case: ReviewRecommendationUseCase):
        """
        Initializes the ReviewRecommendationHandler with the provided use case.

        Args:
            use_case (ReviewRecommendationUseCase): The use case responsible for generating review recommendations.
        """
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, deadline: datetime):
        """
        Handles the retrieval of review recommendations.

        Creates a `ReviewRecommendationsQuery` from the provided deadline and delegates the actual
        recommendation logic to the associated `ReviewRecommendationUseCase`.

        Args:
            deadline (datetime): The cutoff datetime for considering a review as "old".

        Returns:
            A list of `Review` objects representing the recommended location-category combinations.
        """
        query = ReviewRecommendationsQuery(deadline=deadline)
        return await self.use_case.execute(query=query)
