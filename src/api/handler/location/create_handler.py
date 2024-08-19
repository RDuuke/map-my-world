from internal.location.command import LocationCommand
from internal.location.use_case import LocationCreateUseCase
from src.api.handler import BaseHandler


class LocationCreateHandler(BaseHandler):

    def __init__(self, use_case: LocationCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, command: LocationCommand):
        await self.use_case.execute(command=command)

