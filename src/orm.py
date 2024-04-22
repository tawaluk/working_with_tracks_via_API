import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from models import CustomBase, Track, User
from config import settings

track_engine = create_async_engine(
    url=settings.database_url_async_psycopg,
    echo=True,
)

track_session = async_sessionmaker(bind=track_engine)


async def test_case_del_and_create():
    """utility function for deleting and creating a table in the database."""
    async with track_engine.begin() as connect:
        await connect.run_sync(CustomBase.metadata.drop_all)
        await connect.run_sync(CustomBase.metadata.create_all)


async def add_track(model_instance, session=track_session):
    """create one record."""
    async with session() as async_session:
        async_session.add(model_instance)
        await async_session.commit()


if __name__ == "__main__":
    async def test_case_del_and_create():
        async with track_engine.begin() as connect:
            #await connect.run_sync(CustomBase.metadata.drop_all)
            await connect.run_sync(CustomBase.metadata.create_all)

    asyncio.run(test_case_del_and_create())
