from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext
from aiogram.fsm.context import FSMContext
from middlewares.i18n import i18n_middleware


from keyboards.inline.language import language_keyboard


async def language_handler(msg: Message):
    await msg.answer(
        gettext("language_select"),
        reply_markup=language_keyboard()
    )



async def set_language(callback: CallbackQuery, state: FSMContext):
    locale = callback.data.replace("lang_", "") # type: ignore
    await i18n_middleware.set_locale(state, locale)
    text = gettext("language_changed", locale=locale).format(locale=locale)
    await callback.answer(text)
    await callback.message.edit_text(text, reply_markup=None) # type: ignore