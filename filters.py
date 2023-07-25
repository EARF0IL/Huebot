from aiogram.filters import BaseFilter
from aiogram.types import Message


class ValidateWordForHuenization(BaseFilter):
    def __init__(self):
        super().__init__()

    async def __call__(self, message: Message) -> bool:
        text = message.text.strip().split()
        if len(text) > 1:
            return False
        word = text[0]
        return all(i in 'йцукенгшщзхъфывапролджэячсмитьбю' for i in word)

