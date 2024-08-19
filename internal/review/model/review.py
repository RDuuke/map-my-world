from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import UUID, uuid4


@dataclass
class Review:
    """
    Represents a review associated with a location and category.
    """

    uuid: UUID
    """
    A universally unique identifier (UUID) for the review.
    """

    location_id: UUID
    """
    The UUID of the location being reviewed.
    """

    category_id: UUID
    """
    The UUID of the category associated with the review.
    """

    created: datetime
    """
    The date and time when the review was created.
    """

    last_reviewed: Optional[datetime] = None
    """
    The date and time when the review was last viewed (optional).
    """

    @classmethod
    def create(cls, data: Dict) -> 'Review':
        """
        Creates a new Review instance from a dictionary of data.

        Args:
            data: A dictionary containing the location_id and category_id for the review.

        Returns:
            A new Review instance with a generated UUID, the provided location_id and category_id,
            and the current datetime as the creation time.
        """
        return cls(
            uuid=uuid4(),
            location_id=data.get('location_id'),
            category_id=data.get('category_id'),
            created=datetime.now()
        )

    @classmethod
    def from_dict(cls, data: Dict) -> 'Review':
        """
        Creates a Review instance from a dictionary, handling potential ISO-formatted date strings.

        Args:
            data: A dictionary representing a review, potentially with 'last_reviewed' and 'created'
                  fields in ISO 8601 format.

        Returns:
            A Review instance with data extracted from the dictionary,
            converting ISO date strings to datetime objects if necessary.
        """
        if isinstance(data.get('last_reviewed'), str):
            data['last_reviewed'] = datetime.fromisoformat(data.get('last_reviewed'))

        return cls(
            uuid=UUID(data.get('uuid')),
            location_id=UUID(data.get('location_id')),
            category_id=UUID(data.get('category_id')),
            created=datetime.fromisoformat(data.get('created')),
            last_reviewed=data['last_reviewed']
        )

    def to_dict(self) -> Dict:
        """
        Converts the Review object into a dictionary representation suitable for storage or serialization.

        Returns:
            A dictionary containing the review's ID, location ID, category ID,
            creation date, and last reviewed date (if available), with dates formatted in ISO 8601.
        """
        return {
            "_id": str(self.uuid),
            "location_id": str(self.location_id),
            "category_id": str(self.category_id),
            "created": self.created.isoformat(),
            "last_reviewed": self.last_reviewed.isoformat() if self.last_reviewed is not None else None
        }
