from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(
        ..., gt=0, description="Product price (must be greater than 0)"
    )
    image_url: Optional[str] = Field(None, description="Product image URL")


class ProductCreate(ProductBase):
    category_ids: List[int] = Field(
        ..., description="List of category IDs for the product"
    )


class ProductResponse(BaseModel):
    id: int = Field(..., description="Unique product ID")
    name: str
    description: Optional[str]
    price: float
    image_url: Optional[str]
    created_at: datetime

    # ← many-to-many
    categories: List[CategoryResponse] = Field(
        ..., description="List of categories this product belongs to"
    )

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int = Field(..., description="Total number of products")
