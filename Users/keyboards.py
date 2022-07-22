from aiogram import types
import json


with open("Users/json/keyboards.json", 'r', encoding="utf-8") as file:
    keyboards = json.load(file)
back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(keyboards['back'])
start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*keyboards['greetings'].values())
stages = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*keyboards['scenes'].values()).add(keyboards['back'])
sad = types.ReplyKeyboardRemove()