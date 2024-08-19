from internal.review.command import ReviewCreateCommand
from internal.review.use_case import ReviewCreateUseCase
from src.api.handler import BaseHandler
from src.api.handler.reviewed.schema import ReviewCreateSchema


class ReviewCreateHandler(BaseHandler):

    def __init__(self, use_case: ReviewCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, schema: ReviewCreateSchema):

        command = ReviewCreateCommand.from_dict(data=schema.__dict__)

        await self.use_case.execute(command=command)

