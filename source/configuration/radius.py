from .type_abc import Type
from .exceptions import ValidationError

response_text = '''Задай новый радиус
Например: <code>005</code>

Сейчас установлено: <code>{current_radius}</code>'''

error_text = 'Ошибка валидации'


class Radius(Type):
  verbose_name = 'Радиус'
  error_text = error_text

  def validate(self, value: str) -> str:

    if value.isdigit():
      return value

    raise ValidationError('Not digit')

  def value_to_json(self) -> float:
    return str(self.value)

  @property
  def response_text(self) -> str:
    return response_text.format(current_radius=self.value_to_json())
