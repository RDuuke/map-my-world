from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, status, Depends

from internal.category.model import Category
from src.api.handler.category import CategoryCreateHandler, CategoryGetAllHandler
from src.api.handler.category.schema import CategoryCreateSchema
from src.app.config.dependencies.category.dependency_container import CategoryDependencyContainer

router_category = APIRouter()


@router_category.post("/category", status_code=status.HTTP_201_CREATED, tags=['category'])
@inject
async def create_category(
        schema: CategoryCreateSchema,
        handler: CategoryCreateHandler = Depends(Provide[CategoryDependencyContainer.category_create_handler])):
    """
        description: This endpoint allows you to create a new category in the system. It receives the category name in the request body in JSON format.
        Before creating the category, it checks if a category with the same name already exists.
        If a category with the same name already exists, a 409 (Conflict) error is returned.
    """
    await handler.execute(schema=schema)


@router_category.get("/category", response_model=List[Category], tags=['category'])
@inject
async def get_all_location(
        handler: CategoryGetAllHandler = Depends(Provide[CategoryDependencyContainer.category_get_all_handler])):
    return await handler.execute()
