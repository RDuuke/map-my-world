from fastapi import APIRouter, Body

from internal.location import LocationRepository
from internal.location.model import Location
from internal.location.use_case import LocationCreateUseCase
from internal.common.client import MongoDBClient
from src.handler.location import LocationCreateHandler

router = APIRouter()
mongo_client = MongoDBClient()


@router.post("/location", status_code=201, tags=['location'])
async def create_location(location: Location = Body(...)):
    await mongo_client.connect()

    repository = LocationRepository(client=mongo_client)
    use_case = LocationCreateUseCase(repository=repository)
    handler = LocationCreateHandler(use_case=use_case)

    await handler.execute(location=location)
