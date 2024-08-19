import abc
from abc import ABC
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from internal.review.model import Review


class ReviewRepository(ABC):
    """
    An abstract base class defining the interface for interacting with review data.

    This class establishes a contract for concrete implementations of review repositories,
    ensuring they provide the necessary methods for creating, updating, and retrieving reviews.
    """

    @abc.abstractmethod
    async def create(self, review: Review) -> None:
        """
        Creates a new review.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for persisting the provided `review` object to the underlying data store.

        Args:
            review (Review): The review object to be created.

        Returns:
            None
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, review: Review) -> None:
        """
        Updates an existing review.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for updating the provided `review` object in the underlying data store.

        Args:
            review (Review): The review object to be updated.

        Returns:
            None
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def find_by_location_and_category(self, location_id: UUID, category_id: UUID) -> Optional[Review]:
        """
        Finds a review by its associated location and category.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for retrieving a `Review` object from the underlying data store
        based on the provided `location_id` and `category_id`.

        Args:
            location_id (UUID): The UUID of the location associated with the review.
            category_id (UUID): The UUID of the category associated with the review.

        Returns:
            The `Review` object if found, or None if no review with the given location and category exists.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def find_by_id(self, uuid: UUID) -> Optional[Review]:
        """
        Finds a review by its UUID.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for retrieving a `Review` object from the underlying data store based on the provided `uuid`.

        Args:
            uuid (UUID): The UUID of the review to search for.

        Returns:
            The `Review` object if found, or None if no review with the given UUID exists.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def find_unreviewed_old(self, deadline: datetime) -> List[Review]:
        """
        Finds unreviewed or old reviews.

        This is an abstract method that must be implemented by concrete subclasses.
        It is responsible for retrieving a list of `Review` objects from the underlying data store
        that are either unreviewed (last_reviewed is None) or have a last_reviewed date before the given `deadline`.

        Args:
            deadline (datetime): The cutoff datetime for considering a review as "old".

        Returns:
            A list of `Review` objects that meet the criteria.
        """
        raise NotImplementedError
