from datetime import datetime

from internal.review.use_case import ReviewRecommendationUseCase
from src.handler import BaseHandler


class ReviewRecommendationHandler(BaseHandler):

    def __init__(self, use_case: ReviewRecommendationUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, deadline: datetime):
        return await self.use_case.execute(deadline=deadline)
