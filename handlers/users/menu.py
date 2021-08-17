from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Что интересует?",
                         reply_markup=menu)


@dp.message_handler(text="1234567890")
async def get_answer(message: types.Message):
    await message.answer(f"Значит, {message.text}, ну ок.",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Прислать номер телефона")
async def get_answer(message: types.Message):
    await message.answer(reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Тык", "Пык"]))
async def get_answer(message: types.Message):
    await message.answer(f"О, {message.text}, ладно.",
                         reply_markup=ReplyKeyboardRemove())
