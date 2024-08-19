from internal.review.command import AddLastReviewedCommand
from internal.review.use_case import AddReviewUseCase
from src.api.handler import BaseHandler


class AddReviewedHandler(BaseHandler):

    def __init__(self, use_case: AddReviewUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, command: AddLastReviewedCommand):
        await self.use_case.execute(command=command)

