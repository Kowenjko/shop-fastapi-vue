from typing import TYPE_CHECKING
from sqlalchemy import String, Text, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func
from .base import Base
from .category_product_association import category_product_association

if TYPE_CHECKING:
    from .category import Category


class Product(Base):

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    price: Mapped[float] = mapped_column(Float, default=0.0, server_default="0.0")
    image_url: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    categories: Mapped[list["Category"]] = relationship(
        secondary=category_product_association,
        back_populates="products",
    )

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
