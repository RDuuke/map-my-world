from typing import Optional

from internal.category.model import Category
from internal.common.client import MongoDBClient


class CategoryRepository:

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["categories"]

    async def create(self, category: Category) -> None:
        await self.collection.insert_one(category.to_dict())

    async def find_by_name(self, category: Category) -> Optional[Category]:

        response = await self.collection.find_one({
            "name": category.name
        })
        if response:
            return Category(**response)

        return None
