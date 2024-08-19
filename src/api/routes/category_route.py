from fastapi import APIRouter, Body

from internal.category import CategoryRepository
from internal.category.command import CategoryCommand
from internal.category.use_case import CategoryCreateUseCase
from internal.common.client import MongoDBClient
from src.api.handler.category import CategoryCreateHandler

router_category = APIRouter()
mongo_client = MongoDBClient()


@router_category.post("/category", status_code=201, tags=['category'])
async def create_location(command: CategoryCommand = Body(...)):
    await mongo_client.connect()

    repository = CategoryRepository(client=mongo_client)
    use_case = CategoryCreateUseCase(repository=repository)
    handler = CategoryCreateHandler(use_case=use_case)

    await handler.execute(command=command)
