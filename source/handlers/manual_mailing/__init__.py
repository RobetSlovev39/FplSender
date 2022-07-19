from .state import ManualMailing
from source.settings.filters import IsAdmin

from .entry_point import entry_point
from .dep_time import dep_time
from .alt import alt
from .radius import radius
from .lat import lat
from .lng import lng

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text, Regexp


def register_manual_mailing_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_message_handler(entry_point, IsAdmin(), Text(equals='Отправить вручную', ignore_case=True))
  dispatcher.register_message_handler(dep_time, state=ManualMailing.dep_time)
  dispatcher.register_message_handler(alt, state=ManualMailing.alt)
  dispatcher.register_message_handler(radius, state=ManualMailing.radius)
  dispatcher.register_message_handler(lat, state=ManualMailing.lat)
  dispatcher.register_message_handler(lng, state=ManualMailing.lng)
