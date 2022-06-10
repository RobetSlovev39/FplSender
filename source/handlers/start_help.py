from aiogram.types import (
  Message,
  KeyboardButton,
  ReplyKeyboardMarkup
)

response_text = '''Start Help Message Text'''

keyboard = ReplyKeyboardMarkup(
  [[KeyboardButton('Just to see')]],
  resize_keyboard=True
)

async def start_help(message: Message) -> None:
  await message.answer(response_text, reply_markup=keyboard)
