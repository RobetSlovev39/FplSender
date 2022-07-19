from ..settings import MAIL_HOSTNAME, MAIL_SENDER, MAIL_PASSWORD, MAIL_PORT, MAIL_USE_TLS

import logging
import asyncio
import aiosmtplib
from typing import List


def get_message(subject: str, text: str) -> str:
  return f'Subject: {subject}\n\n{text}'


async def send_mails(recipients: List[str], message: str) -> None:
  client = aiosmtplib.SMTP(hostname=MAIL_HOSTNAME, port=MAIL_PORT, use_tls=MAIL_USE_TLS)

  await client.connect()
  await client.starttls()
  await client.login(username=MAIL_SENDER, password=MAIL_PASSWORD)

  message = get_message('Mailing', message)

  for recipient in recipients:
    try:
      await client.sendmail(MAIL_SENDER, recipient, message)
    except Exception as error:
      logging.error(str(error))
    await asyncio.sleep(1)
