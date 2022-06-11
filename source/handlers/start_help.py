from aiogram.types import Message
from .keyboards import get_start_help

response_text = '''Start Help Message Text'''

async def start_help(message: Message) -> None:
  await message.answer(response_text, reply_markup=get_start_help())
