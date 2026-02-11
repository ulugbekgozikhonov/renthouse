from aiogram.types import Message
from aiogram.utils.i18n import gettext


async def start_handler(msg: Message):
    await msg.answer(gettext("start_message"))
