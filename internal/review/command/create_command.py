from dataclasses import dataclass
from typing import Dict
from uuid import UUID


@dataclass
class ReviewCreateCommand:
    location_id: UUID
    category_id: UUID

    @classmethod
    def from_dict(cls, data: Dict) -> 'ReviewCreateCommand':
        return cls(
            location_id=data.get('location_id'),
            category_id=data.get('category_id')
        )
