from .state import ManualMailing

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def alt(message: Message, state: FSMContext) -> None:

  async with state.proxy() as data:
    data['alt'] = message.text

  await message.answer('Введи radius. Например: <code>005</code>', parse_mode='HTML')
  await ManualMailing.next()
