from aiogram import Dispatcher

from routes.commands import router as commands_router

dp = Dispatcher()

dp.include_router(commands_router)
