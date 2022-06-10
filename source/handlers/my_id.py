from aiogram.types import Message


async def my_id(message: Message) -> None:
  await message.answer(f'<code>{message.from_user.id}</code>', parse_mode='HTML')
