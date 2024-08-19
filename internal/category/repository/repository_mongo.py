from typing import Optional

from internal.category.model import Category
from internal.category.repository.repository import CategoryRepository
from internal.common.client import MongoDBClient
from internal.common.repository import BaseRepository


class CategoryMongoRepository(CategoryRepository, BaseRepository):
    """
    Concrete implementation of the CategoryRepository interface for MongoDB.

    This class handles the interaction with the 'categories' collection in MongoDB
    to perform operations like creating and retrieving categories.
    """

    def __init__(self, client: MongoDBClient):
        """
        Initializes the CategoryMongoRepository with the provided MongoDB client.

        Args:
            client (MongoDBClient): An instance of the MongoDBClient class for database access.
        """
        self.client = client
        self.collection = self.client.db["categories"]  # Get a reference to the 'categories' collection

    async def create(self, category: Category) -> None:
        """
        Creates a new category in the MongoDB database.

        Args:
            category (Category): The Category object to be created.
        """
        await self.collection.insert_one(category.to_dict())

    async def find_by_name(self, name: str) -> Optional[Category]:
        """
        Finds a category by its name in the MongoDB database.

        Args:
            name (str): The name of the category to search for.

        Returns:
            The Category object if found, or None if no category with the given name exists.
        """
        response = await self.collection.find_one({"name": name})
        if response:
            return Category(**self.rename_id(response))

        return None
