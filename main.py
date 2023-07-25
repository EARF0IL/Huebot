from os import environ
import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from logging import basicConfig, INFO
from dotenv import load_dotenv
import main_router

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
load_dotenv()


async def main():
    bot = Bot(environ.get("BOT_TOKEN"))
    dispatcher = Dispatcher()
    dispatcher.include_router(main_router.router)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    basicConfig(level=INFO)
    asyncio.run(main())

# TODO: make accent check for Ё
