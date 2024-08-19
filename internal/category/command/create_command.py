from dataclasses import dataclass
from typing import Dict


@dataclass
class CategoryCreateCommand:
    """
       Represents the data needed to create a new category.
    """

    name: str
    """
    The name of the category. Must be a string (str).
    """

    @classmethod
    def from_dict(cls, data: Dict) -> 'CategoryCreateCommand':
        """
            Creates an instance of CategoryCreateCommand from a dictionary.

            This class method allows you to construct a `CategoryCreateCommand` object from a dictionary
            containing the necessary data. It is useful for processing data received in JSON format,
            for example, in an HTTP request to a FastAPI endpoint.

            Args:
                data (Dict): A dictionary containing the category data,
                             including at least the 'name' key.

            Returns:
                An instance of CategoryCreateCommand with the data extracted from the dictionary.
        """
        return cls(
            name=data.get('name')
        )
