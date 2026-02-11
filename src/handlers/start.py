from aiogram.types import Message
from aiogram.utils.i18n import gettext


async def start_handler(msg: Message):
    text = gettext("welcome").format(
        name=msg.from_user.full_name # type: ignore
        ) + "\n\n" + gettext("start_help")
    await msg.answer(text)

    
