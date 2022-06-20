from .type_abc import Type
from .exceptions import ValidationError

response_text = '''Задай новую широту (lat)
Например: <code>54.652777</code>

Сейчас установлено: <code>{current_lat}</code>'''

error_text = 'Не float'


class Lat(Type):
  verbose_name = 'Широта'
  error_text = error_text

  def validate(self, value: float) -> float:

    try:
      return float(value)
    except ValueError:
      raise ValidationError('Not float')

  def value_to_json(self) -> float:
    return self.value

  @property
  def response_text(self) -> str:
    return response_text.format(current_lat=self.value_to_json())
