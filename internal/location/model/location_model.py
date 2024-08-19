from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import UUID, uuid4


@dataclass
class Location:
    uuid: UUID
    latitude: float
    longitude: float
    created: datetime
    updated: Optional[datetime] = None

    @classmethod
    def create(cls, data: Dict) -> 'Location':
        return cls(
            uuid=uuid4(),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            created=datetime.now()
        )

    def to_dict(self) -> Dict:
        return {
            "_id": str(self.uuid),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated is not None else None
        }
