from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мои настройки")
        ],
        [
            KeyboardButton(text="Добавить хештэги"),
            KeyboardButton(text="Добавить профили"),
        ],
    ],
    resize_keyboard=True
)

