from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models.category import Category
from app.schemas.category import CategoryCreate


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[Category]:
        stmt = select(Category).order_by(Category.id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_id(self, category_id: int) -> Optional[Category]:
        stmt = select(Category).filter(Category.id == category_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str) -> Optional[Category]:
        stmt = select(Category).filter(Category.slug == slug)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, category_data: CategoryCreate) -> Category:
        db_category = Category(**category_data.model_dump())
        self.session.add(db_category)
        await self.session.commit()
        await self.session.refresh(db_category)
        return db_category
