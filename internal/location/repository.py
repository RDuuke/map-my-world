from typing import Optional

from internal.common.repository import BaseRepository
from internal.location.model import Location
from internal.common.client import MongoDBClient


class LocationRepository(BaseRepository):

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["locations"]

    async def create(self, location: Location) -> None:
        await self.collection.insert_one(location.to_dict())

    async def find_by_coordinate(self, latitude: float, longitude: float) -> Optional[Location]:

        response = await self.collection.find_one({
            "latitude": latitude, "longitude": longitude
        })
        if response:
            return Location(**self.rename_id(response))

        return None
