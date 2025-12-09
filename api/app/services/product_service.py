from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import HTTPException, status

from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductResponse, ProductListResponse, ProductCreate


class ProductService:
    def __init__(self, session: AsyncSession):
        self.product_repository = ProductRepository(session)
        self.category_repository = CategoryRepository(session)

    async def get_all_products(self) -> ProductListResponse:
        products = await self.product_repository.get_all()

        # Якщо продуктів нема
        if not products:
            return ProductListResponse(products=[], total=0)

        products_response = [ProductResponse.model_validate(prod) for prod in products]

        return ProductListResponse(
            products=products_response, total=len(products_response)
        )

    async def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = await self.product_repository.get_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found",
            )

        return ProductResponse.model_validate(product)

    async def get_products_by_category(self, category_id: int) -> ProductListResponse:
        # Перевіряємо чи існує категорія
        category = await self.category_repository.get_by_id(category_id)

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found",
            )

        # Отримуємо продукти
        products = await self.product_repository.get_by_category(category_id)

        products_response = [ProductResponse.model_validate(prod) for prod in products]

        return ProductListResponse(
            products=products_response, total=len(products_response)
        )

    async def create_product(self, product_data: ProductCreate) -> ProductResponse:
        # Перевіряємо чи існує категорія
        category = await self.category_repository.get_by_id(product_data.category_id)

        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with id {product_data.category_id} does not exist",
            )

        # Створюємо продукт
        product = await self.product_repository.create(product_data)

        return ProductResponse.model_validate(product)
