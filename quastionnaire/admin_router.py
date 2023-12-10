from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.config.default import admin1

admin_router = Router()


@admin_router.message(Command("admin"))
async def get_admin_permissions(message: Message):
    if int(admin1) == message.from_user.id:
        await message.answer("Доступ администратора получен", reply_markup=...)
    else:
        await message.answer("Я тебя не понимаю. Для того, чтобы узнать что я умею введи /help")
