from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from src.config.default import admin1
from src.database.db_queries import get_all_users
from src.quastionnaire.keyboards.admin_kbs import admin_main_ikb

admin_router = Router()


@admin_router.message(Command("admin"))
async def get_admin_permissions(message: Message):
    if int(admin1) == message.from_user.id:
        await message.answer("Доступ администратора получен", reply_markup=admin_main_ikb)
    else:
        await message.answer("Я тебя не понимаю. Для того, чтобы узнать что я умею введи /help")


@admin_router.callback_query(F.data == "get_users")
async def get_users_callback(callback: CallbackQuery, bot: Bot):
    all_users = await get_all_users()
    if all_users:
        users_info = "\n".join([f"ID: {user[0]}, tg_id: {user[1]}, Name: {user[2]}" for user in all_users])
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.message.answer(f"Все пользователи:\n{users_info}", reply_markup=admin_main_ikb)

    else:
        await callback.answer("No users found.")
    await callback.answer("")
