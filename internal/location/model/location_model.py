from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel, Field


class Location(BaseModel):
    id: str = Field(alias="_id")
    latitude: float = Field(lt=90, gt=-90)
    longitude: float = Field(lt=180, gt=-180)
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    def to_dict(self) -> Dict:
        return {
            "_id" : self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created": self.created.isoformat() if self.created is not None else None,
            "updated": self.updated.isoformat() if self.updated is not None else None
        }
