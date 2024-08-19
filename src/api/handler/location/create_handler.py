from internal.location.command import LocationCreateCommand
from internal.location.use_case import LocationCreateUseCase
from src.api.handler import BaseHandler
from src.api.handler.location.schemas import LocationCreateSchema


class LocationCreateHandler(BaseHandler):

    def __init__(self, use_case: LocationCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, schema: LocationCreateSchema):
        command = LocationCreateCommand.from_dict(data=schema.__dict__)
        await self.use_case.execute(command=command)

