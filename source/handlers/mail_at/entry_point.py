from .state import MailAtForm
from ..keyboards import cancel_keyboard

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

response_text = '''Напиши новое время отправки
Формат <b>%H:%M</b>, 12 часовой. <code>12:30</code>'''


async def entry_point(message: Message, state: FSMContext) -> None:
  sent_message = await message.answer(response_text, reply_markup=cancel_keyboard, parse_mode='HTML')
  await MailAtForm.new_mail_at.set()

  async with state.proxy() as data:
    data['sent_into_message_id'] = sent_message.message_id
