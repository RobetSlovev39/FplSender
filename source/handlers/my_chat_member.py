from ..settings.settings import ADMIN_ID
from ..settings.configuration import channels
from ..settings.telegram_bot import telegram_bot

from aiogram.types import ChatMemberUpdated


async def my_chat_member(update: ChatMemberUpdated) -> None:
  channel_id = str(update.chat.id)
  channel_type = update.chat.type
  channel_title = update.chat.title
  channel_username = update.chat.username

  chat_member_status = update.new_chat_member.status
  channel_name = f'<a href="https://t.me/{channel_username}">{channel_title}</a>' if channel_username else f'<b>{channel_title}</b>'

  if channel_type == 'channel':

    if chat_member_status == 'administrator':

      if update.new_chat_member.can_post_messages:
        await telegram_bot.send_message(ADMIN_ID, f'Теперь бот будет отправлять посты в канал {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
        channels.add(channel_id, channel_type, channel_title, channel_username)
      else:
        await telegram_bot.send_message(ADMIN_ID, f'Ошибка! Бот не может отправлять посты в канал {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
        channels.delete(channel_id)
    
    elif chat_member_status == 'left':
      await telegram_bot.send_message(ADMIN_ID, f'Бота был выгнан из канала {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
      channels.delete(channel_id)

  elif channel_type == 'supergroup':

    if chat_member_status == 'administrator' or chat_member_status == 'member':
      await telegram_bot.send_message(ADMIN_ID, f'Теперь бот будет отправлять сообщения в чат {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
      channels.add(channel_id, channel_type, channel_title, channel_username)

    elif chat_member_status == 'restricted':

      if update.new_chat_member.can_send_messages is False:
        await telegram_bot.send_message(ADMIN_ID, f'У бота нет возможности отправлять сообщение в чат {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
        channels.delete(channel_id)
      else:
        await telegram_bot.send_message(ADMIN_ID, f'Теперь бот будет отправлять сообщения в чат {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
        channels.add(channel_id, channel_type, channel_title, channel_username)

    elif chat_member_status == 'kicked' or chat_member_status == 'left':
      await telegram_bot.send_message(ADMIN_ID, f'Бота был выгнан из чата {channel_name}', parse_mode='HTML', disable_web_page_preview=True)
      channels.delete(channel_id)
