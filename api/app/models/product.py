from typing import TYPE_CHECKING

from sqlalchemy import String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func
from .base import Base
from .category_product_association import category_product_association

if TYPE_CHECKING:
    from .category import Category


class Product(Base):

    name: Mapped[str] = mapped_column(
        String(100), unique=False, nullable=False, index=True
    )
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    price: Mapped[float] = mapped_column(Float, default=0.0, server_default="0.0")
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    image_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.utcnow
    )

    category: Mapped[list["Category"]] = relationship(
        secondary=category_product_association,
        back_populates="products",
    )

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
