import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.config.default import bot_token
from src.database.db_queries import create_user, get_all_users
from src.database.db_tables import db_tables

bot = Bot(token=bot_token)
dp = Dispatcher()


async def bot_start():

    await db_tables()

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


@dp.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        name = f"{last_name} {first_name}"
    else:
        name = first_name
    await create_user(user_id=user_id, user_name=name)

    all_users = await get_all_users()
    if all_users:
        users_info = "\n".join([f"ID: {user[0]}, tg_id: {user[1]}, Name: {user[2]}" for user in all_users])
        await message.answer(f"Все пользователи:\n{users_info}")
    else:
        await message.answer("No users found.")

    await message.answer(f"Привет, {message.from_user.first_name}")


if __name__ == "__main__":
    asyncio.run(bot_start())
