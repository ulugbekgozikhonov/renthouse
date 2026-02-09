import asyncio

from bot import bot
from dispatcher import dp


def on_startup():
    print("Bot is started...")


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)  # type: ignore


asyncio.run(main())
