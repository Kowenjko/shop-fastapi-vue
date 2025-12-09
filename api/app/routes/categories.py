from fastapi import APIRouter, Depends, status
from typing import Annotated, List
from sqlalchemy.ext.asyncio import AsyncSession

from app.db_helper import db_helper
from app.services.category_service import CategoryService
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/api/categories", tags=["Categories"])


@router.get("", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
async def get_categories(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = CategoryService(session)
    return await service.get_all_categories()


@router.get(
    "/{category_id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK
)
async def get_category(
    category_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = CategoryService(session)
    return await service.get_category_by_id(category_id)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    service = CategoryService(session)
    return await service.create_category(category_data)
