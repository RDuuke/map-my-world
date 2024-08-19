from pydantic import BaseModel, Field


class LocationCommand(BaseModel):
    latitude: float = Field(lt=90, gt=-90)
    longitude: float = Field(lt=180, gt=-180)
