from datetime import datetime

from fastapi import HTTPException, status
from internal.review import ReviewRepository
from internal.review.model import Review


class ReviewCreateUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    async def execute(self, review: Review):

        existing_review = await self.repository.find_by_location_and_category(
            review=review
        )

        if existing_review:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        review.created = datetime.now()

        await self.repository.create(review)
