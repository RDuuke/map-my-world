from fastapi import HTTPException, status
from internal.review import ReviewRepository
from internal.review.command import ReviewCreateCommand
from internal.review.model import Review


class ReviewCreateUseCase:
    """
    Use case responsible for creating new reviews.
    """

    def __init__(self, repository: ReviewRepository):
        """
        Initializes the ReviewCreateUseCase with the provided repository.

        Args:
            repository (ReviewRepository): The repository used to interact with review data.
        """
        self.repository = repository

    async def execute(self, command: ReviewCreateCommand):
        """
        Executes the review creation logic.

        Checks if a review for the same location and category already exists. If it does, raises an HTTP 409 Conflict exception.
        Otherwise, creates a new `Review` object and persists it using the repository.

        Args:
            command (ReviewCreateCommand): The command object containing the location_id and category_id for the review.

        Raises:
            HTTPException(status_code=409): If a review for the same location and category already exists.
        """
        existing_review = await self.repository.find_by_location_and_category(
            location_id=command.location_id, category_id=command.category_id
        )

        if existing_review:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        review = Review.create(command.__dict__)

        await self.repository.create(review)
