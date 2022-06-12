from ..settings.configuration import channels

from typing import Dict
from aiogram.types import Message


def channel_to_string(channel: Dict) -> str:
  channel_type = {'channel': 'Канал', 'supergroup': 'Чат'}[channel['type']]
  channel_name = f'<a href=https://t.me/{channel["username"]}>{channel["title"]}</a>' if channel['username'] else f'<code>{channel["title"]}</code>'
  return f'<b>{channel_type}:</b> {channel_name}'


async def all_channels(message: Message) -> None:
  response_text = 'Все каналы:\n\n'
  response_text += '\n'.join(map(channel_to_string, list(channels.channels.values())))
  response_text += '\n\n<i>Чтобы прекратить рассылку, удали бота из канала или лиши прав</i>'
  await message.answer(response_text, parse_mode='HTML')
