async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)

    # Устанавливаем дефолтные команды
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    # Уведомляет про запуск
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

if __name__ == '__main__':
    from aiogram import executor
    from handlers.users import dp


    executor.start_polling(dp, on_startup=on_startup)