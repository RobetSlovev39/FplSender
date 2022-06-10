from aiogram.dispatcher.filters.state import StatesGroup, State


class MailAtForm(StatesGroup):
  new_mail_at = State()
