import asyncio

from aiogram import Bot

from bot import bot
from database import engine, redis
from dispatcher import dp


async def on_startup(bot: Bot):
    me = await bot.get_me()
    print(f"https://t.me/{me.username} is started...")


async def on_shutdown():
    await engine.dispose()
    await redis.aclose()


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)  # type: ignore


asyncio.run(main())
