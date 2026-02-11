from aiogram import F, Router

from handlers.language import set_language

router = Router()


router.callback_query.register(set_language, F.data.startswith("lang_"))
