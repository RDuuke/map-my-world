from typing import Optional

from internal.common.client import MongoDBClient
from internal.review.model import Review


class ReviewRepository:

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["review"]

    async def create(self, review: Review) -> None:
        await self.collection.insert_one(review.to_dict())

    async def find_by_location_and_category(self, review: Review) -> Optional[Review]:
        response = await self.collection.find_one({
            "location_id": review.location_id, "category_id": review.category_id
        })

        if response:
            return Review(**response)

        return None
