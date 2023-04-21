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
yes_no_kb = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, 
    resize_keyboard=True)

# ------------- make keyboard without using builder
# create game keyboard buttons
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# create game keyboard with buttons 'rock', 'scissors'
# and 'paper' as matrix (list of lists)
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_rock],[button_scissors], [button_paper]],
    resize_keyboard=True)
