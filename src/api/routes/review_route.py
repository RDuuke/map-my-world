from datetime import datetime
from typing import List

from fastapi import APIRouter, Body

from internal.common.client import MongoDBClient
from internal.review import ReviewRepository
from internal.review.model import Review
from internal.review.use_case import ReviewCreateUseCase, AddReviewUseCase, ReviewRecommendationUseCase
from src.handler.location_category_reviewed import LocationCategoryReviewedCreateHandler, ReviewRecommendationHandler
from src.handler.location_category_reviewed.add_review_handler import AddReviewedHandler

router_review = APIRouter()
mongo_client = MongoDBClient()


@router_review.post("/review", status_code=201, tags=['location'])
async def create_location(review: Review = Body(...)):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewCreateUseCase(repository=repository)
    handler = LocationCategoryReviewedCreateHandler(use_case=use_case)

    await handler.execute(review=review)


@router_review.put("/review/{id}", status_code=201, tags=['location'])
async def update_location(id: str):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = AddReviewUseCase(repository=repository)
    handler = AddReviewedHandler(use_case=use_case)

    await handler.execute(review_id=id)


@router_review.get("/recommendations", response_model=List[Review], tags=['recommendations'])
async def recommendations(deadline: datetime):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewRecommendationUseCase(repository=repository)
    handler = ReviewRecommendationHandler(use_case=use_case)
    return await handler.execute(deadline=deadline)
