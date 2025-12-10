from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helper import db_helper
from app.services.product_service import ProductService
from app.schemas.product import ProductResponse, ProductListResponse, ProductCreate

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
async def get_products(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = ProductService(session)
    return await service.get_all_products()


@router.get(
    "/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK
)
async def get_product(
    product_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = ProductService(session)
    return await service.get_product_by_id(product_id)


@router.get(
    "/category/{category_id}",
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_products_by_category(
    category_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = ProductService(session)
    return await service.get_products_by_category(category_id)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    service = ProductService(session)
    return await service.create_product(product_data)
