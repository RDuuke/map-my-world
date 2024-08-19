from fastapi import APIRouter, status

from internal.category import CategoryRepository
from internal.category.use_case import CategoryCreateUseCase
from internal.common.client import MongoDBClient
from src.api.handler.category import CategoryCreateHandler
from src.api.handler.category.schema import CategoryCreateSchema

router_category = APIRouter()
mongo_client = MongoDBClient()


@router_category.post("/category", status_code=status.HTTP_201_CREATED, tags=['category'])
async def create_location(schema: CategoryCreateSchema):
    """
        description: This endpoint allows you to create a new category in the system. It receives the category name in the request body in JSON format.
        Before creating the category, it checks if a category with the same name already exists.
        If a category with the same name already exists, a 409 (Conflict) error is returned.
    """
    await mongo_client.connect()

    repository = CategoryRepository(client=mongo_client)
    use_case = CategoryCreateUseCase(repository=repository)
    handler = CategoryCreateHandler(use_case=use_case)

    await handler.execute(schema=schema)
