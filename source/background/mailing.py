from .hypervisor import hypervisor
from ..settings import configuration, recipients, channels, telegram_bot

import logging
from ..service import get_text, send_mails


@hypervisor.add('mailing', configuration['mail_at'])
async def mailing() -> None:

  text = await get_text(
    configuration['text'],
    configuration.items['dep_time'].value,
    configuration['alt'],
    configuration['radius'],
    configuration['lat'],
    configuration['lng']
  )

  await send_mails(recipients.recipients, text)

  for channel in channels.channels:
    try:
      await telegram_bot.send_message(channel, text)
    except Exception as error:
      logging.error(str(error))

  logging.info(f'Sent\n{text}')
