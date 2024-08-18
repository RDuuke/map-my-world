from internal.review.use_case import AddReviewUseCase
from src.handler import BaseHandler


class AddReviewedHandler(BaseHandler):

    def __init__(self, use_case: AddReviewUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, review_id: str):
        await self.use_case.execute(review_id=review_id)

