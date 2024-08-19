from internal.review.command import ReviewCommand
from internal.review.use_case import ReviewCreateUseCase
from src.api.handler import BaseHandler


class ReviewCreateHandler(BaseHandler):

    def __init__(self, use_case: ReviewCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, command: ReviewCommand):
        await self.use_case.execute(command=command)

