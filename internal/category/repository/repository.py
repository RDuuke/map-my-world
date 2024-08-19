import abc
from abc import ABC
from typing import Optional, List

from internal.category.model import Category


class CategoryRepository(ABC):
    """
    An abstract base class defining the interface for interacting with category data.

    This class establishes the contract for concrete implementations of category repositories,
    ensuring they provide the necessary methods for creating and retrieving categories.
    """

    @abc.abstractmethod
    async def get_all(self) -> List[Category]:
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, category: Category) -> None:
        """
        Creates a new category.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for persisting the provided `category` object to the underlying data store.

        Args:
            category (Category): The category object to be created.

        Returns:
            None
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def find_by_name(self, name: str) -> Optional[Category]:
        """
        Finds a category by its name.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for retrieving a `Category` object from the underlying data store based on the provided `name`.

        Args:
            name (str): The name of the category to search for.

        Returns:
            The `Category` object if found, or None if no category with the given name exists.
        """
        raise NotImplementedError
