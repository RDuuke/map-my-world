from fastapi import HTTPException, status

from internal.location.command import LocationCreateCommand
from internal.location.use_case import LocationCreateUseCase
from src.api.handler import BaseHandler
from src.api.handler.location.schemas import LocationCreateSchema


class LocationCreateHandler(BaseHandler):
    """
    Handler for creating new locations.
    """

    def __init__(self, use_case: LocationCreateUseCase):
        """
        Initializes the LocationCreateHandler with the provided use case.

        Args:
            use_case (LocationCreateUseCase): The use case responsible for handling the location creation logic.
        """
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, schema: LocationCreateSchema):
        """
        Handles the creation of a new location.

        Converts the input `LocationCreateSchema` into a `LocationCreateCommand` and delegates the actual
        creation logic to the associated `LocationCreateUseCase`.

        Args:
            schema (LocationCreateSchema): The schema containing the data for the new location.
        """
        command = LocationCreateCommand.from_dict(data=schema.__dict__)
        await self.use_case.execute(command=command)
