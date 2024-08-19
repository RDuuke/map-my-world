from internal.review.command import ReviewCreateCommand
from internal.review.use_case import ReviewCreateUseCase
from src.api.handler import BaseHandler
from src.api.handler.review.schema import ReviewCreateSchema


class ReviewCreateHandler(BaseHandler):
    """
    Handler for creating new reviews.
    """

    def __init__(self, use_case: ReviewCreateUseCase):
        """
        Initializes the ReviewCreateHandler with the provided use case.

        Args:
            use_case (ReviewCreateUseCase): The use case responsible for handling the review creation logic.
        """
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, schema: ReviewCreateSchema):
        """
        Handles the creation of a new review.

        Converts the input `ReviewCreateSchema` into a `ReviewCreateCommand` and delegates the actual
        creation logic to the associated `ReviewCreateUseCase`.

        Args:
            schema (ReviewCreateSchema): The schema containing the data for the new review.
        """

        command = ReviewCreateCommand.from_dict(data=schema.__dict__)
        await self.use_case.execute(command=command)
