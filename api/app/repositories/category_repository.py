
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models.category import Category
from app.schemas.category import CategoryCreate

class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_all(self) -> List[Category]:
        return await self.db.query(Category).all()

    async def get_by_id(self, category_id: int) -> Optional[Category]:
        return await self.db.query(Category).filter(Category.id == category_id).first()

    async def get_by_slug(self, slug: str) -> Optional[Category]:
        return await self.db.query(Category).filter(Category.slug == slug).first()

    async def create(self, category_data: CategoryCreate) -> Category:
        db_category = Category(**category_data.model_dump())
        self.db.add(db_category)
        await self.db.commit()
        await self.db.refresh(db_category)
        return db_category
