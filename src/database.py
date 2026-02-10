from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import DEBUG, POSTGRES_URL

engine = create_async_engine(POSTGRES_URL, echo=bool(DEBUG))
async_session = async_sessionmaker(engine, expire_on_commit=False)
