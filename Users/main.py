from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

import json
from datetime import datetime

from Users import keyboards as kb


with open("Users/json/messages.json", 'r', encoding='utf-8') as file:
    messages = json.load(file)

with open("Users/json/keyboards.json", 'r', encoding='utf-8') as file:
    keyboards = json.load(file)

class Main(StatesGroup):
    start = State()
    scene = State()
    alt_scene = State()
    settings = State()

async def start(message: types.Message, state: FSMContext):
    await Main.start.set()

    if datetime.now().day !=23 and datetime.now().day !=24 and datetime.now().year == 2022:
        await message.answer(messages['sad'], reply_markup=kb.sad)
        return

    await message.answer(messages['greetings'], reply_markup=kb.start_kb)
    
# Импортируем здесь чтобы избежать ошибки цикличного импорта
from Users.scenes import Stages

def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(start, Text(equals=keyboards['back'], ignore_case=True), state=Stages.start)