from .filters import IsAdmin
from .telegram_bot import telegram_bot

from ..handlers import (
  start_help,
  my_id,

  register_mail_at_handlers
)

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, IsAdmin(), commands=['start', 'help'])
dispatcher.register_message_handler(my_id, commands=['my_id'])

register_mail_at_handlers(dispatcher)
