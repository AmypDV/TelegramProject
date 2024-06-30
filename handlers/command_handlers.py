from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router

from keyboards.keyboard_utils import keyboard_animal

from lexicon.lexicon import LEXICON_RU
import logging


logger = logging.getLogger(__name__)

router_command = Router()

# Этот хэндлер будет срабатывать на команду "/start"
@router_command.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f'command start. Member {message.from_user.id}')
    await message.answer(text=LEXICON_RU().start,
                         reply_markup=keyboard_animal)




# Этот хэндлер будет срабатывать на команду "/help"
@router_command.message(Command(commands='help'))
async def process_help_command(message: Message):
    logger.info(f'command help. Member {message.from_user.id}')
    await message.answer(text=LEXICON_RU().help)