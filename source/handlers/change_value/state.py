from aiogram.dispatcher.filters.state import StatesGroup, State


class ValueForm(StatesGroup):
  new_value = State()
