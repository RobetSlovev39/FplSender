from .state import ValueForm
from ..keyboards import cancel_keyboard
from source.settings.configuration import configuration

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def entry_point(message: Message, state: FSMContext) -> None:
  item = configuration.get_item_by_verbose_name(message.text)
  sent_message = await message.answer(item.response_text, reply_markup=cancel_keyboard, parse_mode='HTML')
  await ValueForm.new_value.set()

  async with state.proxy() as data:
    data['item_verbose_name'] = message.text
    data['sent_into_message_id'] = sent_message.message_id
