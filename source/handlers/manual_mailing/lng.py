from source.service import perform
from source.settings.configuration import configuration

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def lng(message: Message, state: FSMContext) -> None:
  first_message = await message.answer('Отправка...')

  async with state.proxy() as data:
    data['lng'] = lng
    await perform(
      configuration['text'],
      data['dep_time'],
      data['alt'],
      data['radius'],
      data['lat'],
      data['lng']
    )

  await state.finish()
  await first_message.edit_text('Отправлено')
