from dataclasses import dataclass
from typing import Dict


@dataclass
class LocationCreateCommand:
    """
    Represents the data required to create a new location.
    """

    latitude: float
    """
    The latitude of the location. Must be a floating-point number (float).
    """

    longitude: float
    """
    The longitude of the location. Must be a floating-point number (float).
    """

    @classmethod
    def from_dict(cls, data: Dict) -> 'LocationCreateCommand':
        """
        Creates an instance of LocationCreateCommand from a dictionary.

        This class method allows you to construct a `LocationCreateCommand` object from a dictionary
        containing the necessary data. It is useful for processing data received in JSON format,
        for example, in an HTTP request to a FastAPI endpoint.

        Args:
            data (Dict): A dictionary containing the location data,
                         including at least the 'latitude' and 'longitude' keys.

        Returns:
            An instance of LocationCreateCommand with the data extracted from the dictionary.
        """
        return cls(
            latitude=data.get('latitude'),
            longitude=data.get('longitude')
        )
