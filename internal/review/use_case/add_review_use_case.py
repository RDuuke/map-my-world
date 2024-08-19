from datetime import datetime

from fastapi import HTTPException, status
from internal.review import ReviewRepository
from internal.review.command import AddLastReviewedCommand


class AddReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    async def execute(self, command: AddLastReviewedCommand):
        review = await self.repository.find_by_id(
            id=command.id
        )

        if review is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )

        review.last_reviewed = datetime.now()

        await self.repository.update(review=review)
