from .type_abc import Type
from ..utilities import validate_time
from .exceptions import ValidationError

from typing import Union
from datetime import datetime

response_text = '''Напиши новое время отправки
Формат <b>%H:%M</b>, 12 часовой. <code>12:30</code>

Сейчас установлено время: <b>{set_now}</b>
(со сдвигом в UTC до Server Time <b>{server_time}</b>)'''

error_text = '''Неправильный формат времени'''


class MailAt(Type):
  verbose_name = 'Время отправки'
  error_text = error_text

  def validate(self, value: Union[datetime, str]) -> datetime:
    try:
      if type(value) is datetime:
        return value

      return validate_time(value, raise_exception=True)
    except ValueError:
      raise ValidationError("Can't parse time")

  def value_to_json(self) -> str:
    return self.value.strftime('%H:%M')

  @property
  def response_text(self) -> str:
    return response_text.format(set_now=self.value_to_json(), server_time=datetime.now().strftime('%H:%M'))
