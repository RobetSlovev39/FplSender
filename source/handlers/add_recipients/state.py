from aiogram.dispatcher.filters.state import StatesGroup, State


class AddRecipient(StatesGroup):
  recipient = State()
