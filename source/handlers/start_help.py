from aiogram.types import Message
from .keyboards import start_help_keyboard

response_text = '''Start Help Message Text'''

async def start_help(message: Message) -> None:
  await message.answer(response_text, reply_markup=start_help_keyboard)
