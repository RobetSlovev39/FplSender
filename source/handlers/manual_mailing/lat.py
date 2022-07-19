from .state import ManualMailing

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def lat(message: Message, state: FSMContext) -> None:

  async with state.proxy() as data:
    data['lat'] = lat

  await message.answer('Введи lng. Например: <code>20.993611</code>', parse_mode='HTML')
  await ManualMailing.next()
