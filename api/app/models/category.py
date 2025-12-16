from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


if TYPE_CHECKING:
    from .product import Product


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    products: Mapped[List["Product"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
