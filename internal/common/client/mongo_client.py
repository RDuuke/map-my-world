import os

from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBClient:
    """
    A class to manage asynchronous connections to a MongoDB database.
    """

    def __init__(self):
        """
        Initializes the MongoDBClient.

        Sets the `client` and `db` attributes to None initially.
        """
        self.client = None
        self.db = None

    async def connect(self):
        """
        Establishes the connection to the MongoDB database.

        Retrieves the MongoDB connection URI from the 'MONGO_URI' environment variable
        or defaults to 'mongodb://localhost:27017' if not set.
        Creates an AsyncIOMotorClient instance using the URI and connects to the 'map_my_world_db' database.
        """
        mongo_uri = os.environ.get('MONGO_URI', "mongodb://localhost:27017")
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client["map_my_world_db"]

    async def close(self):
        """
        Closes the MongoDB connection if it's open.
        """
        if self.client:
            self.client.close()
