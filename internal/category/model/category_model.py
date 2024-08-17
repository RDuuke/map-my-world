from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel, Field


class Category(BaseModel):
    id: str = Field(alias="_id")
    name: str
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,
            "name": self.name,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated is not None else None
        }
