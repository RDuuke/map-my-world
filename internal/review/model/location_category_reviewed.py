from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import UUID, uuid4


@dataclass
class Review:
    uuid: UUID
    location_id: UUID
    category_id: UUID
    created: datetime
    last_reviewed: Optional[datetime] = None

    @classmethod
    def create(cls, data: Dict) -> 'Review':
        return cls(
            uuid=uuid4(),
            location_id=data.get('location_id'),
            category_id=data.get('category_id'),
            created=datetime.now()
        )

    @classmethod
    def from_dict(cls, data: Dict) -> 'Review':
        if isinstance(data.get('last_reviewed'), str):
            data['last_reviewed'] = datetime.fromisoformat(data.get('last_reviewed'))

        return cls(
            uuid=UUID(data.get('uuid')),
            location_id=UUID(data.get('location_id')),
            category_id=UUID(data.get('category_id')),
            created=datetime.fromisoformat(data.get('created')),
            last_reviewed=data.get('last_reviewed')
        )

    def to_dict(self) -> Dict:
        return {
            "_id": str(self.uuid),
            "location_id": str(self.location_id),
            "category_id": str(self.category_id),
            "created": self.created.isoformat(),
            "last_reviewed": self.last_reviewed.isoformat() if self.last_reviewed is not None else None
        }

