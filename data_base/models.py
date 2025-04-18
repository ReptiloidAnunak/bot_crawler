import asyncio
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from settings import DATABASE_URL

Base = declarative_base()


def create_engine_db() -> AsyncEngine:
    engine = create_async_engine(DATABASE_URL, echo=True)
    return engine


class TelegramUser(Base):
    __tablename__ = 'tg_user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    url = Column(String)
    price = Column(Float)
    price_xpath = Column(String)

    def __str__(self):
        return f"{self.title} {self.url}"

    def convert_to_content_msg_str(self) -> str:
        return (f'🔰 Product:\n'
        f'<strong>title: {self.title}</strong>\n'
        f'<strong>url</strong>: {self.url}\n'
        f'<strong>price_xpath</strong>: {self.price_xpath}\n\n\n'
        f'<strong>price</strong>: {self.price}\n'
        f'__________________________________')

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_tables())
