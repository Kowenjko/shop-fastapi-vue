import asyncio
from app.core.db_helper import db_helper
from app.seed.categories import seed_categories
from app.seed.products import seed_products


async def seed_all():
    # Берём фабрику сессий (асинхронно)
    async_session_maker = db_helper.session_factory

    print("🚀 Starting database seed...")

    async with async_session_maker() as session:
        await seed_categories(session)

    print("🎉 Seeding complete!")

    try:
        # Берём фабрику сессий (асинхронно)
        async_session_maker = db_helper.session_factory

        print("🚀 Starting database seed...")

        async with async_session_maker() as session:
            await seed_categories(session)
            await seed_products(session)

        print("🎉 Database seeding completed successfully!")
    except Exception as e:
        print(f"Error disposing engine: {e}")
    finally:
        await db_helper.engine.dispose()


if __name__ == "__main__":
    asyncio.run(seed_all())
