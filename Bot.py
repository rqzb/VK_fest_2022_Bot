import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import TELEGRAM

from Users.main import register_start
from Users.scenes import register_scenes


async def main():
    bot = Bot(token=TELEGRAM)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_start(dp)
    register_scenes(dp)

    await dp.start_polling()


if __name__ == '__main__':
    print("Bot is running...")

    asyncio.run(main())
