from typing import Optional

from internal.common.repository import BaseRepository
from internal.location.model import Location
from internal.common.client import MongoDBClient
from internal.location.repository import LocationRepository


class LocationMongoRepository(LocationRepository, BaseRepository):
    """
    Concrete implementation of the LocationRepository interface for MongoDB.

    This class handles interactions with the 'locations' collection in MongoDB
    to perform operations like creating and retrieving locations.
    """

    def __init__(self, client: MongoDBClient):
        """
        Initializes the LocationMongoRepository with the provided MongoDB client.

        Args:
            client (MongoDBClient): An instance of the MongoDBClient class for database access.
        """
        self.client = client
        self.collection = self.client.db["locations"]  # Get a reference to the 'locations' collection

    async def create(self, location: Location) -> None:
        """
        Creates a new location in the MongoDB database.

        Args:
            location (Location): The Location object to be created.
        """
        await self.collection.insert_one(location.to_dict())

    async def find_by_coordinate(self, latitude: float, longitude: float) -> Optional[Location]:
        """
        Finds a location by its coordinates in the MongoDB database.

        Args:
            latitude (float): The latitude of the location to search for.
            longitude (float): The longitude of the location to search for.

        Returns:
            The Location object if found, or None if no location with the given coordinates exists.
        """
