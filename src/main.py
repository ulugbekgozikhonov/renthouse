import asyncio

from bot import bot
from database import engine, redis
from dispatcher import dp


def on_startup():
    print("Bot is started...")


async def on_shutdown():
    await engine.dispose()
    await redis.aclose()


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)  # type: ignore


asyncio.run(main())
