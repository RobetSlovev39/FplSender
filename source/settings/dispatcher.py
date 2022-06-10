from .telegram_bot import telegram_bot

from ..handlers import (
  my_id
)

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(my_id, commands=['my_id'])
