from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class AddFilm(StatesGroup):
    name_film = State()
    janr = State()
    rating = State()

router_add_film = Router()

@router_add_film.message(Command('add_film'))
async def Add_Film(message: Message, state: FSMContext):
    await message.answer('Введите название фильма:')
    await state.set_state(AddFilm.name_film)

@router_add_film.message(AddFilm.name_film)
async def add_film_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите жанр фильма:')
    await state.set_state(AddFilm.janr)

@router_add_film.message(AddFilm.janr)
async def add_janr(message: Message, state: FSMContext):
    await state.update_data(janr=message.text)
    await message.answer('Введите рейтинг фильма:')
    await state.set_state(AddFilm.rating)

@router_add_film.message(AddFilm.rating)
async def add_rating(message: Message, state: FSMContext):
    await state.update_data(rating=message.text)

    data = await state.get_data()

    text = (
        f"Фильм добавлен:\n"
        f"Название: {data['name']}\n"
        f"Жанр: {data['janr']}\n"
        f"Рейтинг: {data['rating']}"
    )

    await message.answer(text)
    await state.clear()

# python3 main.py