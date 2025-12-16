from app.schemas.category import CategoryCreate
from app.services.category_service import CategoryService


categories_data = [
    {"name": "Electronics", "slug": "electronics"},
    {"name": "Clothing", "slug": "clothing"},
    {"name": "Books", "slug": "books"},
    {"name": "Home & Garden", "slug": "home-garden"},
]


async def seed_categories(session):
    service = CategoryService(session)

    print("📁 Creating categories...")

    for data in categories_data:
        category = CategoryCreate(**data)
        await service.create_category(category)

    print(f"✅ Created {len(categories_data)} categories")
