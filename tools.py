# bot/tools.py

import asyncio
import os
import re
from urllib.parse import urlparse
from lxml import html
import pandas as pd
import sqlalchemy
from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from settings import DOWNLOAD_EXCEL_DIR, DATABASE_URL
from data_base.models import TelegramUser, Product, AsyncSessionLocal, create_engine_db
from urllib import parse


def get_engine_by_extension(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.xlsx':
        return 'openpyxl'
    elif ext == '.xls':
        return 'xlrd'
    elif ext == '.ods':
        return 'odf'
    else:
        raise ValueError(f'Unsupported file extension: {ext}')


async def get_price(product):
    async with ClientSession() as session:
        async with session.get(product.url) as response:
            response_text = await response.text()
            tree = html.fromstring(response_text)

            price = tree.xpath(product.price_xpath)

            if price:
                price = price[0]
                if isinstance(price, str):
                    match_point_price = re.search("\d+.\d\d\d", price)
                    if match_point_price:
                        price = price.replace('.', '')
                    match = re.search(r"(\d+(?:[\.,]\d+)?)", price)
                    if match:
                        price = float(match.group(1).replace(",", "."))
                    else:
                        price = 0
                elif isinstance(price, (int, float)):
                    print(f"Цена: {price}")
                else:
                    price_text = price.text or ""
                    match = re.search(r"(\d+(?:[\.,]\d+)?)", price_text)
                    if match:
                        price = float(match.group(1).replace(",", "."))
                    else:
                        price = 0

                return price

            else:
                print("Цена не найдена")
                return None


async def save_product_to_db(product: Product) -> list:
    async with AsyncSessionLocal() as session:
        try:
            async with session.begin():

                    session.add(product)
                    print(f"✅ LOADED: {product}")
        except sqlalchemy.exc.IntegrityError:
            print(f'ALREADY IN DB: {product.url}')
            async with session.begin():
                product.price = await get_price(product)
                await session.commit()
        return product


async def read_excel_table_get_content_msg(path: str) -> str:
        engine = get_engine_by_extension(path)
        df = pd.read_excel(path, engine=engine)
        products = []
        for inx, row in df.iterrows():

            product = Product(title=row.iloc[0],
                              url=str(row.iloc[1]),
                              price_xpath=row.iloc[2])
            product.price = await get_price(product)

            product = await save_product_to_db(product)
            products.append(product)
        products_lst = [(product.convert_to_content_msg_str()) for product in products]
        content_message = '\n'.join(products_lst)
        return content_message


async def get_all_products():
    async with async_session() as session:
        result = await session.execute(select(Product))
        products = result.scalars().all()
        return products


async def count_prod_avg_price_by_source(max_retries: int = 5, delay: int = 2):
    async with AsyncSessionLocal() as session:
        async with session.begin():
            result_tuples_lst = []
            all_prod_urls = select(Product.url)
            result_avrg = await session.execute(all_prod_urls)
            all_urls = result_avrg.scalars().all()

            if not all_urls:
                return ("🐞 BUG: Failed to calculate average prices by site.\nPlease try sending your file again.")

            dns_lst = set([urlparse(url).hostname for url in all_urls])
            for dns in dns_lst:
                stmt = select(Product).filter(Product.url.ilike(f'%{dns}%'))
                result_avrg = await session.execute(stmt)
                products = result_avrg.scalars().all()
                prod_prices = [prod.price for prod in products if prod.price]

                if prod_prices:
                    avg = sum(prod_prices) / len(prod_prices)
                    result_tuples_lst.append((dns, round(avg, 2)))

            if result_tuples_lst:
                res_str_avg = [f"{dns}: {price}" for dns, price in result_tuples_lst]
                return "\n<strong>Average prices of products by sources:</strong>\n" + "\n".join(res_str_avg)
            else:
                if max_retries > 0:
                    await asyncio.sleep(delay)
                    return await count_prod_avg_price_by_source(max_retries - 1, delay)
                return "⚠️ Failed to load average prices after several retries."


if __name__ == "__main__":
    a = asyncio.run(count_prod_avg_price_by_source())
    print(a)
