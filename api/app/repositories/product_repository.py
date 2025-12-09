from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from ..models.product import Product
from ..schemas.product import ProductCreate


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[Product]:
        # return self.db.query(Product).options(joinedload(Product.category)).all()
        stmt = select(Product).order_by(Product.id)
        result: Result = await self.session.execute(stmt)
        products = result.scalars().all()

        return list(products)

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return (
            self.session.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id == product_id)
            .first()
        )

    def get_by_category(self, category_id: int) -> List[Product]:
        return (
            self.session.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.category_id == category_id)
            .all()
        )

    def create(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return db_product

    def get_multiple_by_ids(self, product_ids: List[int]) -> List[Product]:
        return (
            self.session.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id.in_(product_ids))
            .all()
        )
