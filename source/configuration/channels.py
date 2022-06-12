from ..settings import BASE_DIR

import orjson
from os import path
from typing import Dict

CHANNELS = BASE_DIR / 'channels.json'


class Channels:

  def __init__(self) -> None:
    self.channels: Dict = dict()

    if not path.exists(CHANNELS):
      return self.write()

    self.channels = self.read()

  def write(self) -> None:
    with open(CHANNELS, 'wb') as file:
      file.write(orjson.dumps(self.channels, option=orjson.OPT_INDENT_2))

  def read(self) -> Dict:
    with open(CHANNELS, 'rb') as file:
      return orjson.loads(file.read())

  def add(self, c_id: int, c_type: str, title: str, username: str) -> None:
    self.channels[c_id] = {
      'type': c_type,
      'title': title,
      'username': username
    }
    self.write()

  def delete(self, c_id: int) -> Dict:
    deleted = self.channels.pop(c_id)
    self.write()
    return deleted
