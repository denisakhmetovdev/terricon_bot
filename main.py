import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.config.default import bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()


async def bot_start():
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}")


if __name__ == "__main__":
    asyncio.run(bot_start())
