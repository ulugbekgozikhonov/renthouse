from aiogram.types import Message


async def start_handler(msg: Message):
    await msg.answer("Welcome to the world!")
