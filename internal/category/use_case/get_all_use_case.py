from typing import List

from internal.category.model import Category
from internal.category.repository import CategoryRepository


class CategoryGetAllUseCase:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def execute(self) -> List[Category]:
        return await self.repository.get_all()
