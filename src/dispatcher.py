from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n.middleware import FSMI18nMiddleware

from database import redis
from i18n import i18n
from messages import MessageServiceMiddleware
from routes.commands import router as commands_router

storage = RedisStorage(redis)

dp = Dispatcher(storage=storage)

dp.message.outer_middleware(FSMI18nMiddleware(i18n))
dp.message.outer_middleware(MessageServiceMiddleware())
dp.include_router(commands_router)
