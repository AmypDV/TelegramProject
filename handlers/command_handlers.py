from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
import logging


logger = logging.getLogger(__name__)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f'command start. Member {message.from_user.id}')
    await message.answer(text=LEXICON_RU.start)


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    logger.info(f'command help. Member {message.from_user.id}')
    await message.answer(text=LEXICON_RU.help)