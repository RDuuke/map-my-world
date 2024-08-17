from internal.category.model import Category
from internal.category.use_case import CategoryCreateUseCase
from src.handler import BaseHandler


class CategoryCreateHandler(BaseHandler):

    def __init__(self, use_case: CategoryCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, category: Category):
        await self.use_case.execute(category=category)

