from dataclasses import dataclass
from uuid import UUID


@dataclass
class ReviewUpdateLastReviewedCommand:
    """
    Represents the data required to update the 'last_reviewed' field of a review.
    """

    uuid: UUID
    """
    The UUID of the review to be updated.
    """
