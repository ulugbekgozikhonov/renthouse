from aiogram import Dispatcher

from routes.commands import router as commands_router
from routes.language import router as language_router

from middlewares.i18n import i18n_middleware



dp = Dispatcher()
dp.update.outer_middleware(i18n_middleware)

dp.include_router(commands_router)
dp.include_router(language_router)
