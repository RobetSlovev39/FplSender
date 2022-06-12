from .state import AddRecipient
from source.settings.filters import IsAdmin

from .entry_point import entry_point
from .add_recipient import add_recipient, wrong_add_recipient

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text, Regexp


def register_add_recipient_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_message_handler(entry_point, IsAdmin(), Text(equals='Добавить получателя', ignore_case=True))
  dispatcher.register_message_handler(add_recipient, Regexp(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'), state=AddRecipient.recipient)
  dispatcher.register_message_handler(wrong_add_recipient, state=AddRecipient.recipient)
