from typing import List

from internal.category.model import Category
from internal.category.use_case import CategoryGetAllUseCase
from src.api.handler import BaseHandler


class CategoryGetAllHandler(BaseHandler):

    def __init__(self, use_case: CategoryGetAllUseCase):
        self.use_case = use_case

    async def execute(self) -> List[Category]:
        return await self.use_case.execute()
