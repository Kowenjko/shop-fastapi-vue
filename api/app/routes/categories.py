from fastapi import APIRouter, Depends, status

from typing import Annotated, List
from sqlalchemy.ext.asyncio import AsyncSession

from app.db_helper import db_helper
from app.services.category_service import CategoryService
from app.schemas.category import CategoryResponse

router = APIRouter(
    prefix="/api/categories",
    tags=['categories']
)

@router.get("", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(session:  Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    service = CategoryService(session)
    return service.get_all_categories()

@router.get('/{category_id}', response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category(category_id: int, session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    service = CategoryService(session)
    return service.get_category_by_id(category_id)
