from fastapi import APIRouter
from app.core.config import settings


from .products import router as products_router
from .categories import router as categories_router
from .cart import router as cart_router

router = APIRouter(prefix=settings.api.prefix)

router.include_router(products_router, prefix=settings.api.products)
router.include_router(categories_router, prefix=settings.api.categories)
router.include_router(cart_router, prefix=settings.api.cart)
