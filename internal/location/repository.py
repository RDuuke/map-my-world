from typing import Optional

from internal.location.model import Location
from internal.common.client import MongoDBClient


class LocationRepository:

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["category"]

    async def create(self, location: Location) -> None:
        await self.collection.insert_one(location.to_dict())

    async def find_by_coordinate(self, location: Location) -> Optional[Location]:
        response = await self.collection.find_one({
            "latitude": location.latitude, "longitude": location.longitude
        })

        if location:
            return Location(**response)

        return None
