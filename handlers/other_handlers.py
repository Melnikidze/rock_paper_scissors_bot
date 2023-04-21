# import statements
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

# router initialization
router: Router = Router()

# create handler for messages didn't included in another handlers
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
