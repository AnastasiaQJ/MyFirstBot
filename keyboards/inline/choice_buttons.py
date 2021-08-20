from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import callback
from data.config import LINK_THIS, LINK_THEN

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Первое",
                                 callback_data="tap:first:5"),
            InlineKeyboardButton(text="Второе",
                                 callback_data="tap:second:10"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)


first_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Смотри тут", url=LINK_THIS)
        ]
    ]
)

second_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Смотри тут", url=LINK_THEN)
        ]
    ]
)