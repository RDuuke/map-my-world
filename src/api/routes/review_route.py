from fastapi import APIRouter, Body

from internal.common.client import MongoDBClient
from internal.review import ReviewRepository
from internal.review.model import Review
from internal.review.use_case import ReviewCreateUseCase
from src.handler.location_category_reviewed import LocationCategoryReviewedCreateHandler

router_review = APIRouter()
mongo_client = MongoDBClient()


@router_review.post("/review", status_code=201, tags=['location'])
async def create_location(review: Review = Body(...)):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewCreateUseCase(repository=repository)
    handler = LocationCategoryReviewedCreateHandler(use_case=use_case)

    await handler.execute(review=review)
