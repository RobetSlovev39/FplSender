from .state import AddRecipient
from ..keyboards import cancel_keyboard

from aiogram.types import Message


async def entry_point(message: Message) -> None:
  await message.answer('Введи почту получателя', reply_markup=cancel_keyboard)
  await AddRecipient.recipient.set()
