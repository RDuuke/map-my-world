from datetime import datetime
from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, status, Depends
from pydantic import UUID4

from internal.review.model import Review
from src.api.handler.review import ReviewRecommendationHandler, \
    ReviewCreateHandler, ReviewUpdateLastReviewedHandler
from src.api.handler.review.schema import ReviewCreateSchema
from src.app.config.dependencies.review.dependency_container import ReviewDependencyContainer

router_review = APIRouter()


@router_review.post("/review", status_code=status.HTTP_201_CREATED, tags=['review'])
@inject
async def create_review(schema: ReviewCreateSchema,
                        handler: ReviewCreateHandler = Depends(Provide[ReviewDependencyContainer.review_create_handler])):
    await handler.execute(schema=schema)


@router_review.put("/review/{uuid}", status_code=status.HTTP_201_CREATED, tags=['review'])
@inject
async def add_last_reviewed(uuid: UUID4,
                            handler: ReviewUpdateLastReviewedHandler = Depends(Provide[ReviewDependencyContainer.review_update_last_reviewed_handler])):
    """
        description: This endpoint allows you to mark a review as recently viewed by updating its `last_reviewed` field to the current datetime.
        It expects the UUID of the review to be updated as a path parameter.
        If the review with the specified UUID is not found, a 404 Not Found error is returned.
        Otherwise, the `last_reviewed` field is updated and a 201 Created status code is returned.
    """
    await handler.execute(uuid=uuid)


@router_review.get("/review/recommendations", response_model=List[Review], tags=['review'])
@inject
async def recommendations(deadline: datetime,
                          handler: ReviewRecommendationHandler = Depends(Provide[ReviewDependencyContainer.review_recommendation_handler])):
    """
        description: This endpoint fetches a list of location-category combinations that have either:
        - Never been review (`last_reviewed` is null).
        - Been review before a specified deadline (`last_reviewed` is older than the `deadline`).

        The endpoint prioritizes combinations that have never been review and limits the results to a maximum of 10.
    """
    return await handler.execute(deadline=deadline)
