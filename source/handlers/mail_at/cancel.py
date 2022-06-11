from ..keyboards import get_start_help

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def cancel(message: Message, state: FSMContext) -> None:

  if not (await state.get_state()):
    return await message.answer('Нечего отменять')

  await state.finish()
  await message.answer('Отменено', reply_markup=get_start_help())
