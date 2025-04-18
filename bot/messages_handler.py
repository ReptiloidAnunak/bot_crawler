

import os.path

from aiogram.types import Message
import aiofiles
from settings import DOWNLOAD_EXCEL_DIR, EXCEL_FORMATS, BOT_MSG_REQUEST_DOC
from tools import read_excel_table_get_content_msg, count_prod_avg_price_by_source


async def messages_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    if message.text == '/start':
        await message.answer('Hello! 👋🤖 \nI`m <strong>CoolCrawler Bot</strong> !', parse_mode='html')
        await message.answer(BOT_MSG_REQUEST_DOC)
        return
    if not message.document:
        await message.answer("❗️You should send excel-file")
        return

    filename = message.document.file_name

    if not any(filename.endswith(f) for f in EXCEL_FORMATS):
        await message.answer(f"🚫 Неверный формат файла: {filename}")
        return

    file_path = os.path.join(DOWNLOAD_EXCEL_DIR, filename)
    file_obj = await message.bot.download(message.document)

    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(file_obj.read())

    await message.answer(f"✅ Файл загружен: {filename}")
    avg_prices_msg = await count_prod_avg_price_by_source()
    content_excel_msg = await read_excel_table_get_content_msg(file_path)

    await message.answer(content_excel_msg, parse_mode='html')
    await message.answer(avg_prices_msg, parse_mode='html')


