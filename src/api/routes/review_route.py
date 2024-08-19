from datetime import datetime
from typing import List
from fastapi import APIRouter, status
from pydantic import UUID4

from internal.common.client import MongoDBClient
from internal.review import ReviewRepository
from internal.review.model import Review
from internal.review.use_case import ReviewCreateUseCase, ReviewUpdateLastReviewUseCase, ReviewRecommendationUseCase
from src.api.handler.reviewed import ReviewRecommendationHandler, \
    ReviewCreateHandler, CreateUpdateLastReviewedHandler
from src.api.handler.reviewed.schema import ReviewCreateSchema

router_review = APIRouter()
mongo_client = MongoDBClient()


@router_review.post("/review", status_code=status.HTTP_201_CREATED, tags=['review'])
async def create_review(schema: ReviewCreateSchema):
    """
       description: This endpoint allows you to create a new review, associating a specific location with a category.
       It checks if a review for the same location and category already exists. If it does, a 409 Conflict error is returned.
       Otherwise, a new review is created and stored in the database.
    """
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewCreateUseCase(repository=repository)
    handler = ReviewCreateHandler(use_case=use_case)

    await handler.execute(schema=schema)


@router_review.put("/review/{uuid}", status_code=status.HTTP_201_CREATED, tags=['review'])
async def add_last_reviewed(uuid: UUID4):
    """
        description: This endpoint allows you to mark a review as recently viewed by updating its `last_reviewed` field to the current datetime.
        It expects the UUID of the review to be updated as a path parameter.
        If the review with the specified UUID is not found, a 404 Not Found error is returned.
        Otherwise, the `last_reviewed` field is updated and a 201 Created status code is returned.
    """

    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewUpdateLastReviewUseCase(repository=repository)
    handler = CreateUpdateLastReviewedHandler(use_case=use_case)
    await handler.execute(uuid=uuid)


@router_review.get("/review/recommendations", response_model=List[Review], tags=['review'])
async def recommendations(deadline: datetime):
    """
        description: This endpoint fetches a list of location-category combinations that have either:
        - Never been reviewed (`last_reviewed` is null).
        - Been reviewed before a specified deadline (`last_reviewed` is older than the `deadline`).

        The endpoint prioritizes combinations that have never been reviewed and limits the results to a maximum of 10.
        """
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewRecommendationUseCase(repository=repository)
    handler = ReviewRecommendationHandler(use_case=use_case)
    return await handler.execute(deadline=deadline)
