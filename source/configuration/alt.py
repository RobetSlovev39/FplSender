from .type_abc import Type

response_text = '''Задай новую высоту
Например: <code>A020</code>

Сейчас установлено: <code>{current_alt}</code>'''

error_text = 'Ошибка валидации'


class Alt(Type):
  verbose_name = 'Высота'
  error_text = error_text

  def validate(self, value: str) -> str:
    return value

  def value_to_json(self) -> float:
    return str(self.value)

  @property
  def response_text(self) -> str:
    return response_text.format(current_alt=self.value_to_json())
