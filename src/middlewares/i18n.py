from aiogram.utils.i18n import I18n, FSMI18nMiddleware


i18n = I18n(
    path="src/locales",
    default_locale="en",
    domain="messages"
)


i18n_middleware = FSMI18nMiddleware(i18n=i18n, key="locale")

