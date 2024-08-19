from typing import Optional

from internal.category.model import Category
from internal.common.client import MongoDBClient
from internal.common.repository import BaseRepository


class CategoryRepository(BaseRepository):

    def __init__(self, client: MongoDBClient):
        self.client = client
        self.collection = self.client.db["categories"]

    async def create(self, category: Category) -> None:
        await self.collection.insert_one(category.to_dict())

    async def find_by_name(self, name: str) -> Optional[Category]:

        response = await self.collection.find_one({
            "name": name
        })
        if response:
            return Category(**self.rename_id(response))

        return None
