from ..keyboards import get_start_help
from source.configuration import ValidationError

from source.utilities import to_utc
from source.settings import telegram_bot
from source.background.hypervisor import hypervisor
from source.settings.configuration import configuration

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def change_value(message: Message, state: FSMContext) -> None:
  async with state.proxy() as data:
    item_verbose_name = data['item_verbose_name']
    sent_into_message_id = data['sent_into_message_id']

  item = configuration.get_item_by_verbose_name(item_verbose_name)

  try:
    configuration[item.name] = message.text
  except ValidationError:
    return await telegram_bot.send_message(
      message.from_user.id,
      item.error_text,
      reply_to_message_id=sent_into_message_id,
      allow_sending_without_reply=True
    )

  if item.name == 'mail_at':
    item.change(to_utc(item.value))
    hypervisor.reschedule_task('mailing', item.value_to_json())

  await message.answer('Изменено', reply_markup=get_start_help())
  await state.finish()
