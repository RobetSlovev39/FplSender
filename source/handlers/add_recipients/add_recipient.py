from ..keyboards import get_start_help
from source.settings.configuration import recipients

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def add_recipient(message: Message, state: FSMContext) -> None:
  recipients.add(message.text.strip())
  await message.answer('Получатель добавлен', reply_markup=get_start_help())
  await state.finish()


async def wrong_add_recipient(message: Message) -> None:
  await message.answer('Неверный формат почты')
