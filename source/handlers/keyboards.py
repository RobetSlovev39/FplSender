from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)

start_help_keyboard = ReplyKeyboardMarkup(
  [[KeyboardButton('Время отправки')]],
  resize_keyboard=True
)

cancel_keyboard = ReplyKeyboardMarkup(
  [[KeyboardButton('Отменить')]],
  resize_keyboard=True
)
