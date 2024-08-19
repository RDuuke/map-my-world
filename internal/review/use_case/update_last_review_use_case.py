from datetime import datetime

from fastapi import HTTPException, status
from internal.review import ReviewRepository
from internal.review.command import ReviewUpdateLastReviewedCommand


class ReviewUpdateLastReviewUseCase:
    """
    Use case responsible for updating the 'last_reviewed' field of a review.
    """

    def __init__(self, repository: ReviewRepository):
        """
        Initializes the ReviewUpdateLastReviewUseCase with the provided repository.

        Args:
            repository (ReviewRepository): The repository used to interact with review data.
        """
        self.repository = repository

    async def execute(self, command: ReviewUpdateLastReviewedCommand):
        """
        Executes the logic to update the 'last_reviewed' field of a review.

        Finds the review by its UUID. If the review is not found, raises an HTTP 404 Not Found exception.
        Otherwise, updates the `last_reviewed` field to the current datetime and saves the changes using the repository.

        Args:
            command (ReviewUpdateLastReviewedCommand): The command object containing the UUID of the review to be updated.

        Raises:
            HTTPException(status_code=404): If the review with the specified UUID is not found.
        """
        review = await self.repository.find_by_id(
            uuid=command.uuid
        )

        if review is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )

        review.last_reviewed = datetime.now()

        await self.repository.update(review=review)
