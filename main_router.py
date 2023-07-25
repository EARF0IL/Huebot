from aiogram import Router
from aiogram import F
from aiogram.types import Message

from huenization_core import Huenizator
from filters import ValidateWordForHuenization

router = Router()


@router.message(F.content_type.in_({'text'}), ValidateWordForHuenization())
async def hueunction(message: Message):
    word = message.text.strip()
    huenizator = Huenizator(word)
    await message.answer(huenizator.get_huenizated_word().capitalize())


@router.message()
async def help_message(message: Message):
    await message.answer("""Отправьте боту одно слово и он вернёт его с корнем "хуй".""")
