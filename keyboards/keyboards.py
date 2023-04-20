# import statements
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU

# ------------- make keyboard by ReplyKeyboardBuilder
# create buttons with answers accept and decline
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# initialization keyboard builder with buttons "accept", "decline"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# adding buttons to keyboard builder with param width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# create keyboard with buttons "accept", "decline"
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# ------------- make keyboard without using builder
