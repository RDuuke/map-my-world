from dataclasses import dataclass
from typing import Dict


@dataclass
class LocationCreateCommand:
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, data: Dict) -> 'LocationCreateCommand':
        return cls(
            latitude=data.get('latitude'),
            longitude=data.get('longitude')
        )