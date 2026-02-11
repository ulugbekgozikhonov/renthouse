from aiogram import Dispatcher
from aiogram.utils.i18n.middleware import SimpleI18nMiddleware

from i18n import i18n
from routes.commands import router as commands_router

dp = Dispatcher()

dp.message.outer_middleware(SimpleI18nMiddleware(i18n))
dp.include_router(commands_router)
