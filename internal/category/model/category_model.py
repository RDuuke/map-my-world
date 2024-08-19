from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import uuid4, UUID


@dataclass
class Category:
    uuid: UUID
    name: str
    created: datetime
    updated: Optional[datetime] = None

    @classmethod
    def create(cls, data: Dict) -> 'Category':
        return cls(
            uuid=uuid4(),
            name=data.get('name'),
            created=datetime.now()
        )

    def to_dict(self) -> Dict:
        return {
            "_id": str(self.uuid),
            "name": self.name,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated is not None else None
        }
