from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReviewRecommendationsQuery:
    """
    Represents the query parameters for fetching review recommendations.
    """

    deadline: datetime
    """
    The cutoff datetime for considering a review as "old".
    Reviews with a 'last_reviewed' date before this deadline will be included in the recommendations.
    """
