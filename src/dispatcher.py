from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n.middleware import SimpleI18nMiddleware

from database import redis
from i18n import i18n
from routes.commands import router as commands_router

storage = RedisStorage(redis)

dp = Dispatcher(storage=storage)

dp.message.outer_middleware(SimpleI18nMiddleware(i18n))
dp.include_router(commands_router)
