from fastapi import HTTPException, status

from internal.category.command import CategoryCreateCommand
from internal.category.model import Category
from internal.category.repository import CategoryRepository


class CategoryCreateUseCase:
    """
    Use case responsible for creating new categories.
    """

    def __init__(self, repository: CategoryRepository):
        """
        Initializes the CategoryCreateUseCase with the provided repository.

        Args:
            repository (CategoryRepository): The repository used to interact with the category data.
        """
        self.repository = repository

    async def execute(self, command: CategoryCreateCommand) -> None:
        """
        Executes the category creation logic.

        Checks if a category with the same name already exists. If it does, raises an HTTP 409 Conflict exception.
        Otherwise, creates a new `Category` object and persists it using the repository.

        Args:
            command (CategoryCreateCommand): The command object containing the category's name.

        Raises:
            HTTPException(status_code=409): If a category with the same name already exists.
        """
        existing_category = await self.repository.find_by_name(name=command.name)

        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        category = Category.create({
            "name": command.name
        })

        await self.repository.create(category=category)
