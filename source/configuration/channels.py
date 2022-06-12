from ..settings import BASE_DIR

import orjson
from os import path
from typing import List, Dict

CHANNELS = BASE_DIR / 'channels.json'


class Channel:

  def __init__(self, channel_id: int, name: str, channel_type: str) -> None:
    self.channel_id = channel_id
    self.name = name
    self.channel_type = channel_type

  def to_json(self) -> Dict:
    return {'sex': self.sex}


class Channels:

  def __init__(self) -> None:
    self.channels: List[Channel] = list()

    if not path.exists(CHANNELS):
      return self.write()

    self.channels = self.read()

  def write(self) -> None:
    with open(CHANNELS, 'wb') as file:
      file.write(orjson.dumps(list(map(Channel.to_json, self.channels)), option=orjson.OPT_INDENT_2))

  def read(self) -> List[Channel]:
    with open(CHANNELS, 'rb') as file:
      return [Channel(**channel) for channel in orjson.loads(file.read())]
