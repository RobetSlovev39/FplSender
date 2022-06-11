from ..keyboards import start_help_keyboard
from source.background.hypervisor import hypervisor
from source.settings.configuration import configuration

from source.settings import telegram_bot
from source.utilities import validate_time, to_utc

from re import Match
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def new_mail_at(message: Message, state: FSMContext, regexp: Match) -> None:
  mail_at = f'{regexp.group(1)}:{regexp.group(2)}'
  mail_at = to_utc(validate_time(mail_at))

  configuration['mail_at'] = mail_at
  hypervisor.reschedule_task('mailing', mail_at)

  await message.answer('Время изменено (до перезапуска)', reply_markup=start_help_keyboard)
  await state.finish()


async def wrong_new_mail_at(message: Message, state: FSMContext) -> None:
  async with state.proxy() as data:

    await telegram_bot.send_message(
      message.from_user.id,
      'Неправильный формат времени',
      reply_to_message_id=data['sent_into_message_id'],
      allow_sending_without_reply=True
    )
