from fastapi import HTTPException, status

from internal.location import LocationRepository
from internal.location.model import Location


class LocationCreateUseCase:
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    async def execute(self, location: Location) -> None:
        existing_location = await self.repository.find_by_coordinate(location=location)

        if existing_location:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        await self.repository.create(location=location)
