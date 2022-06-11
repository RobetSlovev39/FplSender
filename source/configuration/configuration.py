from ..settings import BASE_DIR
from .exceptions import ValidationError

from ..utilities import get_env_var, validate_time, to_utc

from .type_abc import Type
from .mail_at import MailAt

import orjson
from os import path
from functools import reduce

from typing import Dict, Union, Any

CONFIGURATION = BASE_DIR / 'configuration.json'


class Configuration:
  mail_at = MailAt('mail_at', to_utc(validate_time(get_env_var('MAIL_AT'), raise_exception=True)))

  def __init__(self) -> None:
    self.items = dict()

    for attribute in filter(lambda attr: not attr.startswith('__'), dir(self)):
      if isinstance(item := getattr(self, attribute), Type):
        self.items[item.name] = item

    if not path.exists(CONFIGURATION):
      return self.write()

    for key, value in self.read().items():
      if key in self.items:
        if value == self[key]:
          continue
        try:
          self.items[key].change(value)
        except ValidationError:
          pass

    self.write()

  def write(self) -> None:
    to_write = dict(reduce(lambda a, x: {**a, **x}, map(Type.to_json, self.items.values())))

    with open(CONFIGURATION, 'wb') as file:
      file.write(orjson.dumps(to_write, option=orjson.OPT_INDENT_2))

  def read(self) -> Dict:
    with open(CONFIGURATION, 'rb') as file:
      return orjson.loads(file.read())

  def __getitem__(self, item_name: str) -> Union[int, str]:
    return self.items[item_name].value_to_json()

  def __setitem__(self, item_name: str, new_value: Any) -> None:
    self.items[item_name].change(new_value)
    self.write()
