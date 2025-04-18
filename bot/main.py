import asyncio
import logging
import os.path
import sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from data_base.models import create_tables
from bot.messages_handler import messages_handler
from settings import BOT_MSG_REQUEST_DOC

load_dotenv()
TOKEN = os.getenv("TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
dp.message.register(messages_handler)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(BOT_MSG_REQUEST_DOC)


async def main() -> None:
    await create_tables()
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())