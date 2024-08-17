from internal.location.model import Location
from internal.location.use_case import LocationCreateUseCase
from src.handler import BaseHandler


class LocationCreateHandler(BaseHandler):

    def __init__(self, use_case: LocationCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, location: Location):
        await self.use_case.execute(location=location)

