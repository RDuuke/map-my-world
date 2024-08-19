from typing import List

from internal.location.model import Location
from internal.location.use_case import LocationGetAllUseCase
from src.api.handler import BaseHandler


class LocationGetAllHandler(BaseHandler):

    def __init__(self, use_case: LocationGetAllUseCase):
        self.use_case = use_case

    async def execute(self) -> List[Location]:
        return await self.use_case.execute()
