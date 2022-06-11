from .type_abc import Type
from ..utilities import validate_time
from .exceptions import ValidationError

from typing import Union
from datetime import datetime


class MailAt(Type):
  verbose_name = 'Время отправки'

  def validate(self, value: Union[datetime, str]) -> datetime:
    try:
      if type(value) is datetime:
        return value

      return validate_time(value)
    except ValueError:
      raise ValidationError("Can't parse time")

  def value_to_json(self) -> str:
    return self.value.strftime('%H:%M')
