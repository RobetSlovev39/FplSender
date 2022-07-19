from aiogram.dispatcher.filters.state import StatesGroup, State


class ManualMailing(StatesGroup):
  dep_time = State()
  alt = State()
  radius = State()
  lat = State()
  lng = State()
