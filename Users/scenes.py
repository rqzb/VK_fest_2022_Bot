from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import json

from Users import keyboards as kb
from Users.main import Main 
from Users.json import print_from_json as pfj


with open("Users/json/messages.json", 'r', encoding='utf-8') as file:
    messages = json.load(file)

with open("Users/json/keyboards.json", 'r', encoding='utf-8') as file:
    keyboards = json.load(file)

class Stages(StatesGroup):
    start = State()
    stage = State()


async def choose_stage(message: types.Message, state: FSMContext):
    await message.answer(messages['choose_stage'], reply_markup=kb.stages)
    await Main.scene.set()
    await Stages.start.set()

async def stage(message: types.Message, state: FSMContext):
    await message.answer(pfj.print_formatted(message['text'].upper()), reply_markup=kb.back)
    await Stages.next()


# async def genre_chosen(message: types.Message, state: FSMContext):
#     if message.text.capitalize() not in genre.keys():
#         await message.answer(messages['genre_chosen_fail'])
#         return

#     await state.update_data(genre=message.text.lower())
#     await Artist.next()
#     await message.answer(messages['artist'], reply_markup=kb.artists_kb(message.text.capitalize()))


# async def artist_shosen(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     if message.text not in genre[user_data['genre'].capitalize()]:
#         await message.answer(messages['artist_chosen_fail'])
#         return

#     await state.update_data(artist=message.text.lower())
#     user = message.from_user.id
#     artist = await state.get_data()

#     if add_user_json(str(user), artist['artist']):
#         await message.answer(messages['ok'][0] + message.text + messages['ok'][1], reply_markup=kb.delete_kb(message.text))
#     else:
#         await message.answer(messages['error'])


# async def back(message: types.Message, state: FSMContext):
#     await state.finish()
#     await Main.start.set()
    
    # await message.answer(messages['genre'], reply_markup=kb.genre_kb)


def register_scenes(dp: Dispatcher):
    dp.register_message_handler(choose_stage, Text(equals=keyboards['greetings']['scenes'], ignore_case=True), state=Main.start)
    dp.register_message_handler(choose_stage, Text(equals=keyboards['back'], ignore_case=True), state=Stages.stage)
    dp.register_message_handler(stage, Text(startswith=keyboards['scenes'].values(), ignore_case=True), state=Stages.start)
    # dp.register_message_handler(back, Text(equals=keyboards['back'], ignore_case=True), state=Stages.start)

    # dp.register_message_handler(back, Text(equals=messages['keyboards']['back'], ignore_case=True), state=Artist.artist)
    # dp.register_message_handler(genre_chosen, state=Artist.genre)
    # dp.register_message_handler(artist_shosen, state=Artist.artist)
