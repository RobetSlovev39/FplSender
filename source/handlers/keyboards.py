from ..settings.configuration import configuration

from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def get_start_help() -> ReplyKeyboardMarkup:
  buttons = [
    [KeyboardButton(value.verbose_name)]
  for value in configuration.items.values()]
  buttons.insert(0, [KeyboardButton('Отправить вручную')])
  buttons.append([KeyboardButton('Удалить получателя'), KeyboardButton('Добавить получателя')])
  buttons.append([KeyboardButton('Добавленные каналы')])
  return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


cancel_keyboard = ReplyKeyboardMarkup(
  [[KeyboardButton('Отменить')]],
  resize_keyboard=True
)
