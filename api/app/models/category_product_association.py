from sqlalchemy import Column, ForeignKey, Table


from .base import Base

category_product_association = Table(
    "category_product_association",
    Base.metadata,
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)
