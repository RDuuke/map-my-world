from internal.review.model import Review
from internal.review.use_case import ReviewCreateUseCase
from src.handler import BaseHandler


class LocationCategoryReviewedCreateHandler(BaseHandler):

    def __init__(self, use_case: ReviewCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, review: Review):
        await self.use_case.execute(review=review)

