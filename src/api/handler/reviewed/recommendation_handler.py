from internal.review.query import ReviewRecommendationsQuery
from internal.review.use_case import ReviewRecommendationUseCase
from src.api.handler import BaseHandler


class ReviewRecommendationHandler(BaseHandler):

    def __init__(self, use_case: ReviewRecommendationUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, query: ReviewRecommendationsQuery):
        return await self.use_case.execute(query=query)
