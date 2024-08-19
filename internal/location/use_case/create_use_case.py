from fastapi import HTTPException, status

from internal.location import LocationRepository
from internal.location.command import LocationCommand
from internal.location.model import Location


class LocationCreateUseCase:
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    async def execute(self, command: LocationCommand) -> None:
        existing_location = await self.repository.find_by_coordinate(
            latitude=command.latitude,
            longitude=command.longitude
        )

        if existing_location:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        location = Location.create(command.__dict__)
        await self.repository.create(location=location)
