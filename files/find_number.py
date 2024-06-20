from aiogram import Bot, Dispatcher, F
from aiogram.types.message import Message
from aiogram.filters import CommandStart, Command

from dataclasses import dataclass
import os
import random


BOT_TOKEN = os.getenv("Amyp_First_Bot_key", "00000000")
MAX_NUMBER = 100
N_TRAIN = 8

bot = Bot(BOT_TOKEN)
dispetcher = Dispatcher()


def random_number():
    return random.randint(0, 100)


@dataclass(slots=True)
class StatsGames:
    in_game: bool = False
    number: int = None
    n_train: int = None
    n_game: int = 0
    n_win: int = 0


GAME: dict[int, StatsGames] = {}


@dispetcher.message(CommandStart())
async def get_start_command(message: Message):
    user_id = message.from_user.id
    GAME.setdefault(user_id, StatsGames())
    await message.answer('Привет. Я бот и умею играть в игру "Угадай число.\n'
                         'Для ознакомления с правилами введи команду /help.\n'
                         'Можно посмотреть статистику ваших игр по команде /stat\n'
                         'Начнём играть?')


@dispetcher.message(Command(commands='help'))
async def get_help_command(message: Message):
    await message.answer(f'Игра "Угадайте число"\nЯ загадываю число от 0 до {MAX_NUMBER}\n'
                         f'Ваща задача это число угадать\n'
                         f'У вас будет {N_TRAIN} попыток\n Команда досрочного завершения /end\n'
                         f'Начнем играть?')


@dispetcher.message(F.text.lower().in_(['да', 'играем']))
async def start_game(message: Message):
    user_id = message.from_user.id
    if not GAME.get(user_id):
        await message.answer('Я бот и для начала работы со мной нужна команда /start')
    elif GAME.get(user_id).in_game:
        await message.answer(f'Увы, но игра уже начата. Введите число от 0 до {MAX_NUMBER}')
    else:
        GAME.setdefault(user_id).number = random_number()
        GAME.setdefault(user_id).n_train = N_TRAIN
        GAME.setdefault(user_id).in_game = True
        GAME.setdefault(user_id).n_game += 1
        await message.answer(f'Введите число от 0 до {MAX_NUMBER}')


@dispetcher.message(F.text.lower().in_(['нет', 'не буду']))
async def start_game(message: Message):
    user_id = message.from_user.id
    if GAME.setdefault(user_id).in_game:
        await message.answer(f'Мы уже играем! Введите число от 0 до {MAX_NUMBER}')
    else:
        await message.answer('Но я больше ничего не умею... Давай сыграем...')


@dispetcher.message(lambda text: text.text and text.text.isdigit() and 0 <= int(text.text) <= 100)
async def get_number_from_man(message: Message):
    user_id = message.from_user.id
    if not GAME.get(user_id):
        await message.answer('Я бот и для начала работы со мной нужна команда /start')
    elif not GAME.get(user_id).in_game:
        await message.answer('Игра еще не началась!. Будем играть?')
    else:
        if int(message.text) == GAME.setdefault(user_id).number:
            GAME.setdefault(user_id).in_game = False
            GAME.setdefault(user_id).n_win += 1
            await message.reply(f'Поздравляю! Вы отгадали число {GAME.setdefault(user_id).number}!\nСыграем еще раз')
        elif int(message.text) < GAME.setdefault(user_id).number:
            GAME.setdefault(user_id).n_train -= 1
            await message.answer('Заданное число больше. Попробуйте еще раз')
        elif int(message.text) > GAME.setdefault(user_id).number:
            GAME.setdefault(user_id).n_train -= 1
            await message.answer('Заданное число меньше. Попробуйте еще раз')
        if GAME.setdefault(user_id).n_train == 0:
            GAME.setdefault(user_id).in_game = False
            await message.answer(f'Увы, но вы проиграли... Заданное число {GAME.setdefault(user_id).number}.\n'
                                 f' Еще раз сыграем?')


@dispetcher.message(Command(commands='stat'))
async def get_statistic(message: Message):
    user_id = message.from_user.id
    if not GAME.get(user_id):
        await message.answer('Я бот и для начала работы со мной нужна команда /start')
    else:
        await message.answer(f'Вы играли {GAME.setdefault(user_id).n_game} раз.\n'
                             f'Из них вы выиграли {GAME.setdefault(user_id).n_win} раз.\n'
                             'Сыграем?')



@dispetcher.message(Command(commands='end'))
async def end_game(message: Message):
    user_id = message.from_user.id
    if not GAME.get(user_id):
        await message.answer('Я бот и для начала работы со мной нужна команда /start')
    elif not GAME.get(user_id).in_game:
        await message.answer('Мы с Вами еще не играем... Начнем игру?')
    else:
        GAME.setdefault(user_id).in_game = False
        await message.answer(f'Жаль, что досрочно завершаем игру.... Может быть еще сыграем?')


@dispetcher.message()
async def get_any_message(message: Message):
    user_id = message.from_user.id
    print(GAME.get(user_id))
    if not GAME.get(user_id):
        await message.answer('Я бот и для начала работы со мной нужна команда /start')
    elif GAME.setdefault(user_id).in_game:
        await message.answer(f'Нужно ввести число от 0 до {MAX_NUMBER}')
    else:
        await message.answer('Я Вас не понимаю. Я умею только играть в игру "Угадай число". Сыграем?')


if __name__ == '__main__':
    dispetcher.run_polling(bot)
