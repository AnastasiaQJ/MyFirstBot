from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1234567890"),
            KeyboardButton(text="Прислать номер телефона", request_contact=True),
        ],
        [
            KeyboardButton(text="Тык"),
            KeyboardButton(text="Пык"),
        ],
    ],
    resize_keyboard=True
)