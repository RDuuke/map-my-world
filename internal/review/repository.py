from datetime import datetime, timedelta
from typing import Optional, List
from uuid import UUID

from internal.common.client import MongoDBClient
from internal.common.repository import BaseRepository
from internal.review.model import Review


class ReviewRepository(BaseRepository):

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["location_category_reviewed"]

    async def create(self, review: Review) -> None:
        await self.collection.insert_one(review.to_dict())

    async def update(self, review: Review) -> None:
        await self.collection.update_one(
            {"_id": str(review.uuid)},
            {"$set": {"last_reviewed": review.last_reviewed.isoformat()}}
        )

    async def find_by_location_and_category(self, location_id: UUID, category_id: UUID) -> Optional[Review]:
        response = await self.collection.find_one({
            "location_id": str(location_id), "category_id": str(category_id)
        })
        if response:
            return Review.from_dict(self.rename_id(response))

        return None

    async def find_by_id(self, uuid: UUID) -> Optional[Review]:
        response = await self.collection.find_one({
            "_id": str(uuid)
        })

        if response:
            return Review.from_dict(self.rename_id(response))

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

        return [Review.from_dict(self.rename_id(review)) for review in response]
