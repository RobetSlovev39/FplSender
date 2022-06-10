from .state import MailAtForm
from source.settings.filters import IsAdmin

from .entry_point import entry_point
from .new_mail_at import new_mail_at, wrong_new_mail_at
from .cancel import cancel

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text, Regexp


def register_mail_at_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_message_handler(entry_point, IsAdmin(), Text(equals='Время отправки', ignore_case=True))

  dispatcher.register_message_handler(
    new_mail_at,
    Regexp(r'^(\d{2})\:(\d{2})$'),
    state=MailAtForm.new_mail_at
  )

  dispatcher.register_message_handler(cancel, Text(equals='Отменить'), state='*')
  dispatcher.register_message_handler(wrong_new_mail_at, state=MailAtForm.new_mail_at)
