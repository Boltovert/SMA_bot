import logging
import asyncio
import os 

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart

from src.parser_1 import news_parser


logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart("start"))
async def cmd_start(message: types.Message):
    await message.answer('''
                         Привет, я твой помощник! Я умею немного, но тебе все равно понравится!
                         Выведи команду /help и узнаешь на что я способен
                         ''')

@dp.message(Command(commands=["help"])) 
async def cmd_help(message: types.Message):
    await message.answer('''
                          1. /habr - Интересные научпоп статьи с хабра
                          2. /bus - расписание автобуса из пункта А в Б
                          3. /elec - расписание электрички из пункта А в Б
                          ''')

@dp.message(Command(commands=["habr"])) 
async def cmd_habr(message: types.Message):
    links = news_parser()  
    for link in links:
        await message.answer(link)  

@dp.message(Command(commands=["elec"])) 
async def cmd_elec(message: types.Message):

    await message.answer("Введите пункт откуда:")
    from_point = await dp.wait_for(types.Message)

    await message.answer("Введите пункт куда:")
    to_point = await dp.wait_for(types.Message)

@dp.message(Command(commands=["bus"])) 
async def cmd_elec(message: types.Message):

    await message.answer("Введите пункт откуда:")
    from_point = await dp.wait_for(types.Message)

    await message.answer("Введите пункт куда:")
    to_point = await dp.wait_for(types.Message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


