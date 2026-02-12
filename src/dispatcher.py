from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from database import redis
from routes.commands import router as commands_router

storage = RedisStorage(redis)

dp = Dispatcher(storage=storage)

dp.include_router(commands_router)
