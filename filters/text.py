from aiogram.filters import Filter
from aiogram.types import Message


# Создаем класс-фильтр, со списком слов
# Для проверки на соответствие введенным словам в сообщении
class MyFilterWords(Filter):
    def __init__(self, *args:str) -> None:
        self.words = args

    async def __call__(self, message: Message) -> bool:
        return message.text.lower() in self.words