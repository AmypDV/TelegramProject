import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.user_handlers import router_user
from handlers.command_handlers import router_command

import logging
import sys


logging.basicConfig(level=logging.INFO,
                    format='#%(levelname)-8s [%(asctime)s] - %(filename)s:%(lineno)d - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)]
                    )

# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_routers(router_command, router_user)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())