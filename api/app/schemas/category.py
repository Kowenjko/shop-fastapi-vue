from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Category name")
    slug: str = Field(
        ..., min_length=2, max_length=100, description="URL-friendly category name"
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique category identifier")

    class Config:
        from_attributes = True
