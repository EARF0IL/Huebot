from aiogram.filters import BaseFilter
from aiogram.types import Message


class ValidateWordForHuenization(BaseFilter):
    def __init__(self):
        super().__init__()

    async def __call__(self, message: Message) -> bool:
        text = message.text.lower().strip().split()
        if len(text) > 1:
            if text[0][:4] != '/huy' or len(text) > 2:
                return False
        word = text[-1]
        return all(i in 'йцукенгшщзхъфывапролджэячсмитьбю' for i in word)
