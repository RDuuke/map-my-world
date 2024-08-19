from fastapi import HTTPException, status
from internal.review import ReviewRepository
from internal.review.command import ReviewCommand
from internal.review.model import Review


class ReviewCreateUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    async def execute(self, command: ReviewCommand):

        existing_review = await self.repository.find_by_location_and_category(
            location_id=command.location_id, category_id=command.category_id
        )

        if existing_review:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        review = Review.create(command.__dict__)

        await self.repository.create(review)
