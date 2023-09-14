from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command

from huenization_core import Huenizator
from filters import ValidateWordForHuenization

router = Router()

# @router.message(CommandStart)
# async def start(message: Message):
#     await message.answer("""Отправьте боту одно слово и он вернёт его с корнем "хуй".
#                 Если вы думаете что слово хуенизировано неверно воспользуйтесь командой /start.
#                 Напишите /error <изначальное слово> <неверно хуенизированное слово> <правильная хуенизация словаЮ""")


@router.message(Command('help'))
async def help(message: Message):
    await message.answer("""Отправьте боту одно слово и он вернёт его с корнем "хуй".
Если вы думаете что слово хуенизировано неверно воспользуйтесь командой /error.
Напишите /error <изначальное слово> <неверно хуенизированное слово> <правильная хуенизация слова>.""")


@router.message(Command('error'))
async def send_error(message: Message):
    await message.answer("Ваше сообщение об ошибке отпралено на модерацию")
    # TODO: make error moderation


@router.message(Command('huy'), F.content_type.in_({'text'}), ValidateWordForHuenization())
async def commanded_hueunction(message: Message):
    word = message.text.lower().strip().split()[1]
    huenizator = Huenizator(word)
    await message.answer(huenizator.get_huenizated_word().capitalize())


@router.message(F.chat.type.in_({'private'}), F.content_type.in_({'text'}), ValidateWordForHuenization())
async def hueunction(message: Message):
    word = message.text.lower().strip()
    huenizator = Huenizator(word)
    await message.answer(huenizator.get_huenizated_word().capitalize())


@router.message(F.chat.type.in_({'private'}))
async def help_message(message: Message):
    await message.answer("""Отправьте боту одно слово и он вернёт его с корнем "хуй".""")

