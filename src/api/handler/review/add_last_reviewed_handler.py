from pydantic import UUID4

from internal.review.command import ReviewUpdateLastReviewedCommand
from internal.review.use_case import ReviewUpdateLastReviewUseCase
from src.api.handler import BaseHandler


class CreateUpdateLastReviewedHandler(BaseHandler):

    def __init__(self, use_case: ReviewUpdateLastReviewUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, uuid: UUID4):

        command = ReviewUpdateLastReviewedCommand(uuid=uuid)

        await self.use_case.execute(command=command)

