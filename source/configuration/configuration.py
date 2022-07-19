from ..settings import BASE_DIR
from .exceptions import ValidationError

from ..utilities import validate_time, to_utc

from .type_abc import Type
from .mail_at import MailAt
from .lat import Lat
from .lng import Lng
from .radius import Radius
from .alt import Alt
from .dep_time import DepTime
from .text import Text

import orjson
from os import path
from functools import reduce

from typing import Dict, Union, Any, List

CONFIGURATION = BASE_DIR / 'configuration.json'

default_text = '''FPL-ZZZZ-VG
-ZZZZ/L-V/N
-ZZZZ{dep_time}
-K0130{alt}  /ZONA R{radius} 5439N02059E/
-ZZZZ{endur}
-DOF/{dof} DEP/5439N02059E DEST/5439N02059E TYP/PARAPLAN DO 125KG OPR/VLADIMIR SOLOMATIN RMK/UTP S PLOSHADKI RADIUS {radius}KM
-C/VLADIMIR SOLOMATIN +79097751000)'''


class Configuration:
  mail_at = MailAt('mail_at', to_utc(validate_time('12:00', raise_exception=True)))
  lat = Lat('lat', 54.652777)
  lng = Lng('lng', 20.993611)
  radius = Radius('radius', '005')
  alt = Alt('alt', 'A020')
  dep_time = DepTime('dep_time', '0700')
  text = Text('text', default_text)

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

  def all_verbose_names(self) -> List[str]:
    return sorted([value.verbose_name for value in self.items.values()])

  def get_item_by_verbose_name(self, verbose_name: str) -> Union[Type, None]:
    for value in self.items.values():
      if value.verbose_name == verbose_name:
        return value
