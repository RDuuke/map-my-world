from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel, Field

from internal.category.model import Category
from internal.location.model import Location


class Review(BaseModel):
    id: str = Field(alias="_id")
    location_id: str
    category_id: str
    last_reviewed: Optional[datetime] = None
    created: Optional[datetime] = None

    location: Optional[Location] = None
    category: Optional[Category] = None

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,
            "location_id": self.location_id,
            "category_id": self.category_id,
            "created": self.created.isoformat(),
            "last_reviewed": self.last_reviewed.isoformat() if self.last_reviewed is not None else None
        }
