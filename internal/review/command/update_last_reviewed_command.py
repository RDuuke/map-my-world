from dataclasses import dataclass
from uuid import UUID


@dataclass
class ReviewUpdateLastReviewedCommand:
    uuid: UUID
