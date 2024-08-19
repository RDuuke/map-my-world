from internal.category.command.create_command import CategoryCreateCommand
from internal.category.use_case import CategoryCreateUseCase
from src.api.handler import BaseHandler
from src.api.handler.category.schema import CategoryCreateSchema


class CategoryCreateHandler(BaseHandler):

    def __init__(self, use_case: CategoryCreateUseCase):
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, schema: CategoryCreateSchema):

        command = CategoryCreateCommand.from_dict(schema.__dict__)
        await self.use_case.execute(command=command)
