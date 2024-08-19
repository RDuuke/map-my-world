from fastapi import HTTPException, status

from internal.category import CategoryRepository
from internal.category.command import CategoryCreateCommand
from internal.category.model import Category


class CategoryCreateUseCase:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def execute(self, command: CategoryCreateCommand) -> None:
        existing_category = await self.repository.find_by_name(name=command.name)

        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        category = Category.create({
            "name": command.name
        })

        await self.repository.create(category=category)
