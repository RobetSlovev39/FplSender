from .type_abc import Type

response_text = '''Задай новый тект сообщения

Сейчас установлено:
{current_text}'''

error_text = 'Ошибка валидации'


class Text(Type):
  verbose_name = 'Текст сообщения'
  error_text = error_text

  def validate(self, value: str) -> str:
    return value

  def value_to_json(self) -> float:
    return str(self.value)

  @property
  def response_text(self) -> str:
    return response_text.format(current_text=self.value_to_json())
