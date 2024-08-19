from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import uuid4, UUID


@dataclass
class Category:
    """
    Represents a category with a unique identifier, name, creation date, and optional update date.
    """

    uuid: UUID
    """
    A universally unique identifier (UUID) for the category.
    """

    name: str
    """
    The name of the category.
    """

    created: datetime
    """
    The date and time when the category was created.
    """

    updated: Optional[datetime] = None
    """
    The date and time when the category was last updated (optional).
    """

    @classmethod
    def create(cls, data: Dict) -> 'Category':
        """
        Creates a new Category instance from a dictionary of data.

        Args:
            data: A dictionary containing the category's name.

        Returns:
            A new Category instance with a generated UUID, the provided name, and the current datetime as the creation time.
        """
        return cls(
            uuid=uuid4(),
            name=data.get('name'),
            created=datetime.now()
        )

    def to_dict(self) -> Dict:
        """
        Converts the Category object into a dictionary representation suitable for storage or serialization.

        Returns:
            A dictionary containing the category's ID, name, creation date, and update date (if available).
        """
        return {
            "_id": str(self.uuid),
            "name": self.name,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated is not None else None
        }
