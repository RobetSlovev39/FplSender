from .state import ManualMailing

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def radius(message: Message, state: FSMContext) -> None:

  async with state.proxy() as data:
    data['radius'] = radius

  await message.answer('Введи lat. Например: <code>54.652777</code>', parse_mode='HTML')
  await ManualMailing.next()
