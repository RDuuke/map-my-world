from internal.category.command.create_command import CategoryCreateCommand
from internal.category.use_case import CategoryCreateUseCase
from src.api.handler import BaseHandler
from src.api.handler.category.schema import CategoryCreateSchema


class CategoryCreateHandler(BaseHandler):
    """
    Handler for creating new categories.
    """

    def __init__(self, use_case: CategoryCreateUseCase):
        """
        Initializes the CategoryCreateHandler with the provided use case.

        Args:
            use_case (CategoryCreateUseCase): The use case responsible for handling the category creation logic.
        """
        self.use_case = use_case

    @BaseHandler.handle_exceptions
    async def execute(self, schema: CategoryCreateSchema):
        """
        Handles the creation of a new category.

        Converts the input `CategoryCreateSchema` into a `CategoryCreateCommand` and delegates the actual
        creation logic to the associated `CategoryCreateUseCase`.

        Args:
            schema (CategoryCreateSchema): The schema containing the data for the new category.
        """

        command = CategoryCreateCommand.from_dict(schema.__dict__)
        await self.use_case.execute(command=command)
