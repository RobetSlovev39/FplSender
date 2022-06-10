from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)

start_help_keyboard = ReplyKeyboardMarkup(
  [[KeyboardButton('Время отправки')]],
  resize_keyboard=True
)
