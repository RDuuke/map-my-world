from pydantic import UUID4

from internal.review.command import ReviewUpdateLastReviewedCommand
from internal.review.use_case import ReviewUpdateLastReviewUseCase
from src.api.handler import BaseHandler


class ReviewUpdateLastReviewedHandler(BaseHandler):
    """
    Handler for updating the 'last_reviewed' field of a review.
    """

    def __init__(self, use_case: ReviewUpdateLastReviewUseCase):
        """
        Initializes the ReviewUpdateLastReviewedHandler with the provided use case.

        Args:
            use_case (ReviewUpdateLastReviewUseCase): The use case responsible for handling the review update logic.
        """
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, uuid: UUID4):
        """
        Handles the update of a review's 'last_reviewed' field.

        Creates a `ReviewUpdateLastReviewedCommand` from the provided UUID and delegates the actual
        update logic to the associated `ReviewUpdateLastReviewUseCase`.

        Args:
            uuid (UUID4): The UUID of the review to be updated.
        """

        command = ReviewUpdateLastReviewedCommand(uuid=uuid)
        await self.use_case.execute(command=command)
