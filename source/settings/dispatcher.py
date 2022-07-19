from .filters import IsAdmin
from .telegram_bot import telegram_bot

from ..handlers import (
  start_help,
  my_id,
  cancel,
  change_recipients, delete_recipient, do_not_delete, put_back,
  my_chat_member,
  all_channels,

  register_change_value_handlers,
  register_add_recipient_handlers,
  register_manual_mailing_handlers
)

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text, Regexp
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, IsAdmin(), commands=['start', 'help'])
dispatcher.register_message_handler(my_id, commands=['my_id'])
dispatcher.register_message_handler(cancel, IsAdmin(), commands=['cancel'], state='*')
dispatcher.register_message_handler(cancel, IsAdmin(), Text(equals='Отменить', ignore_case=True), state='*')
dispatcher.register_message_handler(change_recipients, IsAdmin(), Text(equals='Удалить получателя', ignore_case=True))
dispatcher.register_callback_query_handler(delete_recipient, IsAdmin(), Regexp(r'delete\_([0-9]+)'))
dispatcher.register_callback_query_handler(do_not_delete, IsAdmin(), Text(equals='do_not_delete'))
dispatcher.register_callback_query_handler(put_back, IsAdmin(), Text(equals='put_back'))
dispatcher.register_message_handler(all_channels, IsAdmin(), Text(equals='Добавленные каналы', ignore_case=True))

dispatcher.register_my_chat_member_handler(my_chat_member, IsAdmin())

register_change_value_handlers(dispatcher)
register_add_recipient_handlers(dispatcher)
register_manual_mailing_handlers(dispatcher)
