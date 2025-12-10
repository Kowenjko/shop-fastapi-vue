from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, Dict

from app.core.db_helper import db_helper
from app.services.cart_service import CartService
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartResponse
from pydantic import BaseModel

router = APIRouter(tags=["Cart"])


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int] = {}


class UpdateCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int] = {}


class RemoveFromCartRequest(BaseModel):
    cart: Dict[int, int] = {}


class GetCartRequest(BaseModel):
    cart: Dict[int, int] = {}


@router.post("/add", status_code=status.HTTP_200_OK)
async def add_to_cart(
    request: AddToCartRequest,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = CartService(session)
    item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = await service.add_to_cart(request.cart, item)
    return {"cart": updated_cart}


@router.post("", response_model=CartResponse, status_code=status.HTTP_200_OK)
async def get_cart(
    request: GetCartRequest,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = CartService(session)
    return await service.get_cart_details(request.cart)


@router.put("/update", status_code=status.HTTP_200_OK)
async def update_cart_item(
    request: UpdateCartRequest,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = CartService(session)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = await service.update_cart_item(request.cart, item)
    return {"cart": updated_cart}


@router.delete("/remove/{product_id}", status_code=status.HTTP_200_OK)
async def remove_from_cart(
    product_id: int,
    request: RemoveFromCartRequest,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    service = CartService(session)
    updated_cart = await service.remove_from_cart(request.cart, product_id)
    return {"cart": updated_cart}
