from typing import List

from internal.location.model import Location
from internal.location.repository import LocationRepository


class LocationGetAllUseCase:

    def __init__(self, repository: LocationRepository):
        self.repository = repository

    async def execute(self) -> List[Location]:
        return await self.repository.get_all()
