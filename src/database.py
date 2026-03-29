from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from settings import settings

engine = create_async_engine(str(settings.postgres_url))
async_session = async_sessionmaker(engine, expire_on_commit=False)

redis = Redis.from_url(str(settings.redis_url))  # type: ignore
