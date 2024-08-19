from fastapi import HTTPException, status

from internal.location.command import LocationCreateCommand
from internal.location.model import Location
from internal.location.repository import LocationRepository


class LocationCreateUseCase:
    """
    Use case responsible for creating new locations.
    """

    def __init__(self, repository: LocationRepository):
        """
        Initializes the LocationCreateUseCase with the provided repository.

        Args:
            repository (LocationRepository): The repository used to interact with location data.
        """
        self.repository = repository

    async def execute(self, command: LocationCreateCommand) -> None:
        """
        Executes the location creation logic.

        Checks if a location with the same coordinates already exists. If it does, raises an HTTP 409 Conflict exception.
        Otherwise, creates a new `Location` object and persists it using the repository.

        Args:
            command (LocationCreateCommand): The command object containing the location's latitude and longitude.

        Raises:
            HTTPException(status_code=409): If a location with the same coordinates already exists.
        """
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
