from dataclasses import dataclass
from typing import Dict
from uuid import UUID


@dataclass
class ReviewCreateCommand:
    """
    Represents the data required to create a new review.
    """

    location_id: UUID
    """
    The UUID of the location being reviewed.
    """

    category_id: UUID
    """
    The UUID of the category associated with the review.
    """

    @classmethod
    def from_dict(cls, data: Dict) -> 'ReviewCreateCommand':
        """
        Creates an instance of ReviewCreateCommand from a dictionary.

        This class method allows you to construct a `ReviewCreateCommand` object from a dictionary
        containing the necessary data. It is useful for processing data received in JSON format,
        for example, in an HTTP request to a FastAPI endpoint.

        Args:
            data (Dict): A dictionary containing the review data,
                         including at least the 'location_id' and 'category_id' keys.

        Returns:
            An instance of ReviewCreateCommand with the data extracted from the dictionary.
        """
        return cls(
            location_id=data.get('location_id'),
            category_id=data.get('category_id')
        )
