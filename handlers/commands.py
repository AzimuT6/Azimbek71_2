from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot
from datetime import datetime
import random

router_commands = Router()


@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Привет мир!')

    await bot.send_message(chat_id=995712956, 
                           text=f'Привет! {message.from_user.full_name} \nТвой телеграм ID > {message.from_user.id}')


@router_commands.message(F.text == 'привет')
async def hello_handler(message: Message):
    await message.answer('Салам')


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM5auCySPyaBYsHzBJnxxDp79pfm1sAAqirAAKFa_lIF38CcJWB3Wg9BA')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM1auCx0ITQ88ljCxCaBsYQuKdB2vEAAuMAA1eEbA_LD3f9g8IMvD0E')


@router_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo = FSInputFile('media/image.png')
    await message.answer_photo(photo=photo)


@router_commands.message(Command('time'))
async def time_handler(message: Message):
    now = datetime.now()
    await message.answer(f'Сейчас: {now.strftime("%d.%m.%Y %H:%M")}')


@router_commands.message(Command('random'))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(f'Твоё случайное число: {number}')


@router_commands.message(Command('joke'))
async def joke_handler(message: Message):
    jokes = [
        '12 танго',
        'ПЕРВЫЙ СКИЛЛ И ТРЕТИЙ',
        'Шаманчик связывай',
        'Так ты даже не знаешь что такое Суперхлоп',
    ]
    await message.answer(random.choice(jokes))