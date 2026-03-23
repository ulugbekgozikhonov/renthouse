from aiogram import Router
from aiogram.filters import Command

from handlers.user import start_handler

router = Router()

router.message.register(Command("start"), start_handler)
