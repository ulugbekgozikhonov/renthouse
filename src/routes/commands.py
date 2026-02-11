from aiogram import Router
from aiogram.filters import Command


from handlers.start import start_handler
from handlers.language import language_handler

router = Router()

router.message.register(start_handler, Command("start"))
router.message.register(language_handler, Command("language"))