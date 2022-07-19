from .state import ManualMailing
from ..keyboards import cancel_keyboard

from aiogram.types import Message


async def entry_point(message: Message) -> None:
  await message.answer('Введи dep_time. Например <code>1230</code>', reply_markup=cancel_keyboard, parse_mode='HTML')
  await ManualMailing.dep_time.set()
