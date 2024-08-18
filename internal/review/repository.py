from datetime import datetime, timedelta
from typing import Optional, List

from internal.common.client import MongoDBClient
from internal.review.model import Review


class ReviewRepository:

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["location_category_reviewed"]

    async def create(self, review: Review) -> None:
        await self.collection.insert_one(review.to_dict())

    async def update(self, review: Review) -> None:
        await self.collection.update_one(
            {"_id": review.id},
            {"$set": {"last_reviewed": review.last_reviewed.isoformat()}}
        )

    async def find_by_location_and_category(self, review: Review) -> Optional[Review]:
        response = await self.collection.find_one({
            "location_id": review.location_id, "category_id": review.category_id
        })

        if response:
            return Review(**response)

        return None

    async def find_by_id(self, review_id: str) -> Optional[Review]:
        response = await self.collection.find_one({
            "_id": review_id
        })

        if response:
            return Review(**response)

        return None

    async def find_unreviewed_old(self, deadline: datetime) -> List[Review]:
        thirty_last_day = deadline - timedelta(days=30)
        query = {
            "$or": [
                {"last_reviewed": None},
                {"last_reviewed": {"$lte": deadline.isoformat(), "$gte": thirty_last_day.isoformat()}}
            ]
        }

        response = await self.collection.find(query).limit(10).to_list(None)

        return [Review(**review) for review in response]
