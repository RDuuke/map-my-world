from fastapi import APIRouter, status

from internal.common.client import MongoDBClient
from internal.location import LocationRepository
from internal.location.use_case import LocationCreateUseCase
from src.api.handler.location.schemas import LocationCreateSchema
from src.api.handler.location import LocationCreateHandler

router_location = APIRouter()
mongo_client = MongoDBClient()


@router_location.post("/location", status_code=status.HTTP_201_CREATED, tags=['location'])
async def create_location(schema: LocationCreateSchema):
    """
        description: This endpoint allows you to create a new location in the system. It receives the location data in the request body in JSON format.
         Before creating the location, it checks if a location with the same coordinates (latitude and longitude) already exists.
         If a location with the same coordinates already exists, a 409 (Conflict) error is returned.
    """

    await mongo_client.connect()
    repository = LocationRepository(client=mongo_client)
    use_case = LocationCreateUseCase(repository=repository)
    handler = LocationCreateHandler(use_case=use_case)

    await handler.execute(schema=schema)
