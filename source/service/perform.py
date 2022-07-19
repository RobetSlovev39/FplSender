from ..settings.telegram_bot import telegram_bot
from ..settings.configuration import recipients, channels

import logging
from datetime import time

from .get_text import get_text
from .send_mails import send_mails


async def perform(text: str, dep_time: time, alt: str, radius: int, lat: float, lng: float) -> None:

  text = await get_text(
    text,
    dep_time,
    alt,
    radius,
    lat,
    lng
  )

  await send_mails(recipients.recipients, text)

  for channel in channels.channels:
    try:
      await telegram_bot.send_message(channel, text)
    except Exception as error:
      logging.error(str(error))

  logging.info(f'Sent\n{text}')
