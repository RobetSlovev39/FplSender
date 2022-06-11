from .state import MailAtForm
from ..keyboards import cancel_keyboard
from source.settings.configuration import configuration

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

response_text = '''Напиши новое время отправки
Формат <b>%H:%M</b>, 12 часовой. <code>12:30</code>

Сейчас установлено время: <b>{set_now}</b>
(со сдвигом в UTC до Server Time <b>{server_time}</b>)'''


async def entry_point(message: Message, state: FSMContext) -> None:
  sent_message = await message.answer(response_text.format(set_now=configuration['mail_at'], server_time=datetime.now().strftime('%H:%M')), reply_markup=cancel_keyboard, parse_mode='HTML')
  await MailAtForm.new_mail_at.set()

  async with state.proxy() as data:
    data['sent_into_message_id'] = sent_message.message_id
