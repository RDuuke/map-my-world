import abc
from abc import ABC
from typing import Optional, List

from internal.location.model import Location


class LocationRepository(ABC):
    """
    An abstract base class defining the interface for interacting with location data.

    This class establishes a contract for concrete implementations of location repositories,
    ensuring they provide the necessary methods for creating and retrieving locations.
    """

    @abc.abstractmethod
    async def get_all(self) -> List[Location]:
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, location: Location) -> None:
        """
        Creates a new location.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for persisting the provided `location` object to the underlying data store.

        Args:
            location (Location): The location object to be created.

        Returns:
            None
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def find_by_coordinate(self, latitude: float, longitude: float) -> Optional[Location]:
        """
        Finds a location by its coordinates.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for retrieving a `Location` object from the underlying data store
        based on the provided `latitude` and `longitude`.

        Args:
            latitude (float): The latitude of the location to search for.
            longitude (float): The longitude of the location to search for.

        Returns:
            The `Location` object if found, or None if no location with the given coordinates exists.
        """
        raise NotImplementedError
