import os

from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBClient:

    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        mongo_uri = os.environ.get('MONGO_URI', "mongodb://localhost:27017")
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client["map_my_world_db"]
        print(self.db)

    async def close(self):
        if self.client:
            self.client.close()
