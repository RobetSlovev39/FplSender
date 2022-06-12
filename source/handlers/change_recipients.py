from ..utilities import chunk_generator
from ..settings.configuration import recipients

import asyncio
from re import Match
from typing import List, Tuple

from aiogram.utils.exceptions import MessageToDeleteNotFound

from aiogram.types import (
  Message,
  InlineKeyboardButton,
  InlineKeyboardMarkup,

  CallbackQuery
)


def get_response_data(all_recipients: List, delete: bool = True) -> Tuple[str, InlineKeyboardMarkup]:
  all_recipients = list(enumerate(recipients.recipients, 1))

  response_text = '<b>Получатели:</b>\n\n'
  response_text += '\n'.join(map(lambda el: f'{el[0]} – <code>{el[1]}</code>', all_recipients))

  if delete:
    response_text += '\n\n<i>Кого удалить:</i>'

  buttons = [[InlineKeyboardButton(index, callback_data=f'delete_{index - 1}') for index, recipient in chunk] for chunk in chunk_generator(all_recipients, 5)]
  buttons.append([InlineKeyboardButton('Не удалять', callback_data='do_not_delete')])
  keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

  return response_text, keyboard


async def change_recipients(message: Message) -> None:
  if not recipients.recipients:
    return await message.answer('Получателей нет')

  response_text, keyboard = get_response_data(recipients.recipients)
  await message.answer(response_text, reply_markup=keyboard, parse_mode='HTML')


async def delete_recipient(callback_query: CallbackQuery, regexp: Match) -> None:
  deleted = recipients.delete(int(regexp.group(1)))
  response_text, keyboard = get_response_data(recipients.recipients)

  action1 = callback_query.message.edit_text(response_text, reply_markup=keyboard, parse_mode='HTML')
  action2 = callback_query.answer('✅')

  response_text = f'Был удалён: <code>{deleted}</code>\n\n<i>На случай, если удалил случайно\nУдалится через 5 секунд</i>'
  keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton('Вернуть', callback_data='put_back')
  ]])

  action3 = callback_query.message.answer(response_text, reply_markup=keyboard, parse_mode='HTML')

  await asyncio.gather(action1, action2)
  sent_message = await action3

  await asyncio.sleep(5)

  try:
    await sent_message.delete()
  except MessageToDeleteNotFound:
    pass


async def do_not_delete(callback_query: CallbackQuery) -> None:
  response_text, _ = get_response_data(recipients.recipients, delete=False)
  action1 = callback_query.message.edit_text(response_text, reply_markup=None, parse_mode='HTML')
  action2 = callback_query.answer('✅')

  await asyncio.gather(action1, action2)


async def put_back(callback_query: CallbackQuery) -> None:
  to_put_back = callback_query.message.text.split('\n')[0].lstrip('Был удалён: ')
  recipients.add(to_put_back)

  action1 = callback_query.answer('✅')
  action2 = callback_query.message.delete()

  await asyncio.gather(action1, action2)
