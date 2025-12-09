from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, Dict

from app.db_helper import db_helper

from app.services.cart_service import CartService
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartResponse
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/cart",
    tags=["cart"]
)

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

@router.post("/add", status_code=status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest, session:  Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    service = CartService(session)
    item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = service.add_to_cart(request.cart, item)
    return {"cart": updated_cart}

@router.post("", response_model=CartResponse, status_code=status.HTTP_200_OK)
def get_cart(cart_data: Dict[int, int], session:  Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    service = CartService(session)
    return service.get_cart_details(cart_data)

@router.put("/update", status_code=status.HTTP_200_OK)
def update_cart_item(request: UpdateCartRequest, session:  Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    service = CartService(session)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = service.update_cart_item(request.cart, item)
    return {"cart": updated_cart}

@router.delete("/remove/{product_id}", status_code=status.HTTP_200_OK)
def remove_from_cart(product_id: int, request: RemoveFromCartRequest, session:  Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    service = CartService(session)
    updated_cart = service.remove_from_cart(request.cart, product_id)
    return {"cart": updated_cart}
