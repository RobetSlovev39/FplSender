from .state import ValueForm
from source.settings.filters import IsAdmin
from source.settings.configuration import configuration

from .entry_point import entry_point
from .change_value import change_value
from .cancel import cancel

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text


def register_change_value_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_message_handler(entry_point, IsAdmin(), lambda msg: msg.text in configuration.all_verbose_names())
  dispatcher.register_message_handler(cancel, Text(equals='Отменить'), state='*')

  dispatcher.register_message_handler(
    change_value,
    state=ValueForm.new_value
  )
