from datetime import datetime, timedelta
from typing import Optional, List
from uuid import UUID

from internal.common.client import MongoDBClient
from internal.common.repository import BaseRepository
from internal.review.model import Review
from internal.review.repository import ReviewRepository


class ReviewMongoRepository(ReviewRepository, BaseRepository):
    """
    Concrete implementation of the ReviewRepository interface for MongoDB.

    This class handles interactions with the 'location_category_reviewed' collection in MongoDB
    to perform operations related to reviews, such as creating, updating, and retrieving reviews.
    """

    def __init__(self, client: MongoDBClient):
        """
        Initializes the ReviewMongoRepository with the provided MongoDB client.

        Args:
            client (MongoDBClient): An instance of the MongoDBClient class for database access.
        """
        self.client = client
        self.collection = self.client.db["location_category_reviewed"]

    async def create(self, review: Review) -> None:
        """
        Creates a new review in the MongoDB database.

        Args:
            review (Review): The Review object to be created.
        """
        await self.collection.insert_one(review.to_dict())

    async def update(self, review: Review) -> None:
        """
        Updates an existing review in the MongoDB database.

        Args:
            review (Review): The Review object to be updated.
        """
        await self.collection.update_one(
            {"_id": str(review.uuid)},
            {"$set": {"last_reviewed": review.last_reviewed.isoformat()}}
        )

    async def find_by_location_and_category(self, location_id: UUID, category_id: UUID) -> Optional[Review]:
        """
        Finds a review by its associated location and category in the MongoDB database.

        Args:
            location_id (UUID): The UUID of the location associated with the review.
            category_id (UUID): The UUID of the category associated with the review.

        Returns:
            The Review object if found, or None if no review with the given location and category exists.
        """
        response = await self.collection.find_one({
            "location_id": str(location_id), "category_id": str(category_id)
        })
        if response:
            return Review.from_dict(self.rename_id(response))

        return None

    async def find_by_id(self, uuid: UUID) -> Optional[Review]:
        """
        Finds a review by its UUID in the MongoDB database.

        Args:
            uuid (UUID): The UUID of the review to search for.

        Returns:
            The Review object if found, or None if no review with the given UUID exists.
        """
        response = await self.collection.find_one({
            "_id": str(uuid)
        })

        if response:
            return Review.from_dict(self.rename_id(response))

        return None

    async def find_unreviewed_old(self, deadline: datetime) -> List[Review]:
        """
        Finds unreviewed or old reviews in the MongoDB database.

        Args:
            deadline (datetime): The cutoff datetime for considering a review as "old".

        Returns:
            A list of Review objects that are either unreviewed (last_reviewed is None)
            or have a last_reviewed date before the given deadline, up to a maximum of 10 reviews.
        """
        thirty_last_day = deadline - timedelta(days=30)
        query = {
            "$or": [
                {"last_reviewed": None},
                {"last_reviewed": {"$lte": deadline.isoformat(), "$gte": thirty_last_day.isoformat()}}
            ]
        }

        response = await self.collection.find(query).limit(10).to_list(None)

        return [Review.from_dict(self.rename_id(review)) for review in response]
