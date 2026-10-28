from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot

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