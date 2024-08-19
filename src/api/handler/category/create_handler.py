from internal.category.command import CategoryCommand
from internal.category.use_case import CategoryCreateUseCase
from src.api.handler import BaseHandler


class CategoryCreateHandler(BaseHandler):

    def __init__(self, use_case: CategoryCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, command: CategoryCommand):
        await self.use_case.execute(command=command)

