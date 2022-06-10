from .settings import ADMIN_ID

from aiogram.types import Message
from aiogram.dispatcher.filters import Filter


class IsAdmin(Filter):
  key = 'is_admin'

  async def check(self, message: Message) -> bool:
    return message.from_user.id == ADMIN_ID
