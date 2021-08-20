from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Начать диалог"),
            types.BotCommand("help", "Получить справку"),
            types.BotCommand("menu", "Открыть меню"),
            types.BotCommand("question", "Ответить на вопрос"),
        ]
    )