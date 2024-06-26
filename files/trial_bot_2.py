from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Filter
from aiogram.types import Message, ContentType

import os
import sys
import requests

import logging


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = os.getenv("Amyp_First_Bot_key", "00000000")
URL = {'кот':'https://api.thecatapi.com/v1/images/search',
       'собака':'https://random.dog/woof.json',
       'лиса':'https://randomfox.ca/floof/'}

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

format = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'
formatter = logging.Formatter(format, style='{')
logger = logging.getLogger(__name__)
logger.setLevel(10)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


def parser_cat() -> str:
    url = URL['кот']
    foto = requests.get(url)
    if foto.status_code == 200:
        foto = foto.json()[0]["url"]
        logger.info('parcer cat')
        return foto

def parser_dog() -> str:
    url = URL['собака']
    foto = requests.get(url)
    if foto.status_code == 200:
        foto = foto.json()["url"]
        logger.info('parcer dog')
        return foto

def parser_fox() -> str:
    url = URL['лиса']
    foto = requests.get(url)
    if foto.status_code == 200:
        foto = foto.json()["image"]
        logger.info('parcer fox')
        return foto

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    logger.info(f'command start. Member {message.from_user.id}')
    await message.answer('Привет!\nМеня зовут Бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    logger.info(f'command help. Member {message.from_user.id}')
    await message.answer(
        ''' Напиши мне что-нибудь и в ответ
я пришлю тебе твое сообщение.
К томуже я генерирую фотографии кошек, собак и лис
в ответ на сообщения: кот, собака, лиса'''
    )

# Создаем класс-фильтр, со списком слов
# Для проверки на соответствие введенным словам в сообщении
class MyFilterWords(Filter):
    def __init__(self, *args:str) -> None:
        self.words = args

    async def __call__(self, message: Message) -> bool:
        return message.text in self.words

@dp.message(MyFilterWords('кот', 'собака', 'лиса'))
async def send_generate_foto(message:Message):
    match message.text:
        case 'кот': foto = parser_cat()
        case 'собака': foto = parser_dog()
        case 'лиса': foto = parser_fox()
    logger.info(f'answer photo. Member {message.from_user.id}')
    await message.answer_photo(photo=foto)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    if message.content_type == ContentType.TEXT:
        await message.reply(text=message.text)
    elif message.content_type == ContentType.STICKER:
        await message.answer_sticker(message.sticker.file_id)
    else:
        text = 'Я пока глуп и отвечаю только на текстовые сообщения и стикеры :))'
        await message.answer(text=text)

if __name__ == '__main__':
    dp.run_polling(bot)

