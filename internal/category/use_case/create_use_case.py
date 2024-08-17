from datetime import datetime

from fastapi import HTTPException, status

from internal.category import CategoryRepository
from internal.category.model import Category


class CategoryCreateUseCase:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def execute(self, category: Category) -> None:
        existing_category = await self.repository.find_by_name(category=category)

        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT
            )

        category.created = datetime.now()
        await self.repository.create(category=category)
