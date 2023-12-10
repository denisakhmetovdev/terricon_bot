from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


admin_main_ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить всех пользователей", callback_data="get_users")
        ],
        [
            InlineKeyboardButton(text="Создать опрос", callback_data="create_questionnaire")
        ],
        [
            InlineKeyboardButton(text="← Назад", callback_data="simple_gui")
        ]
    ]
)
