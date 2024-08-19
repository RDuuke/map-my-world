from datetime import datetime
from typing import List
from fastapi import APIRouter, Body
from pydantic import UUID4

from internal.common.client import MongoDBClient
from internal.review import ReviewRepository
from internal.review.command import ReviewCommand, AddLastReviewedCommand
from internal.review.model import Review
from internal.review.query import ReviewRecommendationsQuery
from internal.review.use_case import ReviewCreateUseCase, AddReviewUseCase, ReviewRecommendationUseCase
from src.api.handler.reviewed import ReviewRecommendationHandler, \
    ReviewCreateHandler
from src.api.handler.reviewed.add_review_handler import AddReviewedHandler

router_review = APIRouter()
mongo_client = MongoDBClient()


@router_review.post("/review", status_code=201, tags=['location'])
async def create_location(command: ReviewCommand = Body(...)):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewCreateUseCase(repository=repository)
    handler = ReviewCreateHandler(use_case=use_case)

    await handler.execute(command=command)


@router_review.put("/review/{id}", status_code=201, tags=['location'])
async def update_location(id: UUID4):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = AddReviewUseCase(repository=repository)
    handler = AddReviewedHandler(use_case=use_case)
    command = AddLastReviewedCommand(id=id)
    await handler.execute(command=command)


@router_review.get("/recommendations", response_model=List[Review], tags=['recommendations'])
async def recommendations(deadline: datetime):
    await mongo_client.connect()
    repository = ReviewRepository(client=mongo_client)
    use_case = ReviewRecommendationUseCase(repository=repository)
    handler = ReviewRecommendationHandler(use_case=use_case)
    query = ReviewRecommendationsQuery(deadline=deadline)
    return await handler.execute(query=query)
