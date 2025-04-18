import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_DIR = os.path.join(BASE_DIR, 'data_base')
DATA_BASE = os.path.join(DB_DIR, 'bot_crawler.sqlite3')
DATABASE_URL = f"sqlite+aiosqlite:///{DATA_BASE}"

DOWNLOAD_EXCEL_DIR = os.path.join(BASE_DIR, 'excel_files')

if not os.path.exists(DB_DIR):
    os.mkdir(DB_DIR)
if not os.path.exists(DOWNLOAD_EXCEL_DIR):
    os.mkdir(DOWNLOAD_EXCEL_DIR)


EXCEL_FORMATS = [
    ".xls",
    ".xlsx",
    ".xlsm",
    ".xlsb",
    ".xlt",
    ".xltx",
    ".xltm",
    ".ods"
]


BOT_MSG_REQUEST_DOC = """ 🤖 📄 Send your excel-file file (example.xls) in format:\n
<strong>title</strong> - product`s title
<strong>url</strong> - product`s url
<strong>xpath</strong> - xpath to the price element on the product`s page
                         """