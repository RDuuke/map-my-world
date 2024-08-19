from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import UUID, uuid4


@dataclass
class Location:
    """
    Represents a geographical location with latitude, longitude, and timestamps.
    """

    uuid: UUID
    """
    A universally unique identifier (UUID) for the location.
    """

    latitude: float
    """
    The latitude coordinate of the location (a floating-point number).
    """

    longitude: float
    """
    The longitude coordinate of the location (a floating-point number).
    """

    created: datetime
    """
    The date and time when the location record was created.
    """

    updated: Optional[datetime] = None
    """
    The date and time when the location record was last updated (optional).
    """

    @classmethod
    def create(cls, data: Dict) -> 'Location':
        """
        Creates a new Location instance from a dictionary of data.

        Args:
            data: A dictionary containing the location's latitude and longitude.

        Returns:
            A new Location instance with a generated UUID, the provided latitude and longitude, and the current datetime as the creation time.
        """
        return cls(
            uuid=uuid4(),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            created=datetime.now()
        )

    def to_dict(self) -> Dict:
        """
        Converts the Location object into a dictionary representation suitable for storage or serialization.

        Returns:
            A dictionary containing the location's ID, latitude, longitude, creation date, and update date (if available).
        """
        return {
            "_id": str(self.uuid),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated is not None else None
        }
