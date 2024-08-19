from dataclasses import dataclass
from typing import Dict


@dataclass
class CategoryCreateCommand:
    name: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'CategoryCreateCommand':
        return cls(
            name=data.get('name')
        )
