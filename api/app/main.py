from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.db_helper import db_helper
from typing import AsyncGenerator

from contextlib import asynccontextmanager

from fastapi.responses import ORJSONResponse
from app.routes import products_router, categories_router, cart_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # # startup

    yield
    # shutdown

    await db_helper.dispose()


app = FastAPI(
    title=settings.app_name,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
    debug=settings.debug,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")

app.include_router(products_router)
app.include_router(categories_router)
app.include_router(cart_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to fastapi shop API",
        "docs": "api/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
