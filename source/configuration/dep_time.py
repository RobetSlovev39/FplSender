from .type_abc import Type
from .exceptions import ValidationError

from datetime import datetime, time

response_text = '''Задай новое время отправления
Например: <code>0700</code>

Сейчас установлено: <code>{current_dep_time}</code>'''

error_text = 'Неверный формат'


class DepTime(Type):
  verbose_name = 'Время отправки'
  error_text = error_text

  def validate(self, value: str) -> time:

    try:
      return datetime.strptime(value, '%H%M').time()
    except ValueError:
      raise ValidationError('Wrong format')

  def value_to_json(self) -> str:
    return self.value.strftime('%H%M')

  @property
  def response_text(self) -> str:
    return response_text.format(current_dep_time=self.value_to_json())
