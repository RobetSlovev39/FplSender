from .type_abc import Type
from .exceptions import ValidationError

response_text = '''Задай новую долготу (lng)
Например: <code>20.993611</code>

Сейчас установлено: <code>{current_lng}</code>'''

error_text = 'Не float'


class Lng(Type):
  verbose_name = 'Долгота'
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
    return response_text.format(current_lnt=self.value_to_json())
