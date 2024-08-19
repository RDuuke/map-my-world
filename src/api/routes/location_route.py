from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, status, Depends

from internal.location.model import Location
from src.api.handler.location import LocationCreateHandler, LocationGetAllHandler
from src.api.handler.location.schemas import LocationCreateSchema
from src.app.config.dependencies.location.dependency_container import LocationDependencyContainer

router_location = APIRouter()


@router_location.post("/location", status_code=status.HTTP_200_OK, tags=['location'])
@inject
async def create_location(
        schema: LocationCreateSchema,
        handler: LocationCreateHandler = Depends(Provide[LocationDependencyContainer.location_create_handler])):
    """
        description: This endpoint allows you to create a new location in the system. It receives the location data in the request body in JSON format.
        Before creating the location, it checks if a location with the same coordinates (latitude and longitude) already exists.
        If a location with the same coordinates already exists, a 409 (Conflict) error is returned.
    """
    await handler.execute(schema=schema)


@router_location.get("/location", response_model=List[Location], tags=['location'])
@inject
async def get_all_location(
        handler: LocationGetAllHandler = Depends(Provide[LocationDependencyContainer.location_get_all_handler])):
    return await handler.execute()
