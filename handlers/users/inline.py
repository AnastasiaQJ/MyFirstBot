import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_datas import callback
from keyboards.inline.choice_buttons import choice, first_keyboard, second_keyboard
from loader import dp


@dp.message_handler(Command("question"))
async def show_question(message: Message):
    await message.answer(text="Что лучше?",
                         reply_markup=choice)


@dp.callback_query_handler(callback.filter(choice_name="first"))
async def choice_first(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    quantity = callback_data.get("quantity")

    await call.message.answer(f"Выбрано Первое, осталось {quantity}",
                              reply_markup=first_keyboard)


@dp.callback_query_handler(callback.filter(choice_name="second"))
async def choice_second(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    quantity = callback_data.get("quantity")

    await call.message.answer(f"Выбрано второе, осталось {quantity}",
                              reply_markup=second_keyboard)\


@dp.callback_query_handler(text="cancel")
async def cancel_inline_keyboard(call: CallbackQuery):
    await call.answer("Выбрана отмена", show_alert=True)
    await call.message.edit_reply_markup()