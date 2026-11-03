from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class DrinkForm(StatesGroup):
    name = State()
    is_alcohol = State()
    location = State()
    price = State()


router_drink = Router()


@router_drink.message(Command('add_drink'))
async def cmd_start_drink(message: Message, state: FSMContext):
    await state.set_state(DrinkForm.name)
    await message.answer("Введите название напитка:")


@router_drink.message(DrinkForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(DrinkForm.is_alcohol)
    await message.answer("Напиток алкогольный или нет? (Да/Нет):")


@router_drink.message(DrinkForm.is_alcohol)
async def process_alcohol(message: Message, state: FSMContext):
    await state.update_data(is_alcohol=message.text)
    await state.set_state(DrinkForm.location)
    await message.answer("На складе или в пути?:")


@router_drink.message(DrinkForm.location)
async def process_location(message: Message, state: FsmContext if 'FsmContext' in globals() else FSMContext): # type: ignore
    await state.update_data(location=message.text)
    await state.set_state(DrinkForm.price)
    await message.answer("Введите стоимость напитка:")


@router_drink.message(DrinkForm.price)
async def process_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    
    response_text = (
        f"Напиток добавлен:\n"
        f"Название: {data['name']}\n"
        f"Алкогольный: {data['is_alcohol']}\n"
        f"Статус: {data['location']}\n"
        f"Стоимость: {data['price']}"
    )
    
    await message.answer(response_text)
    await state.clear()