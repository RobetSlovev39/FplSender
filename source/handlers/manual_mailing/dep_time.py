from .state import ManualMailing

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from datetime import datetime


async def dep_time(message: Message, state: FSMContext) -> None:

  try:
    dep_time = datetime.strptime(message.text, '%H%M').time()
  except ValueError:
    return await message.answer('Неверный формат')

  async with state.proxy() as data:
    data['dep_time'] = dep_time

  await message.answer('Введи alt. Например: <code>A020</code>', parse_mode='HTML')
  await ManualMailing.next()
