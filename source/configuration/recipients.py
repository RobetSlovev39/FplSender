from ..settings import BASE_DIR

import orjson
from os import path
from typing import Dict

RECIPIENTS = BASE_DIR / 'recipients.json'


class Recipients:

  def __init__(self) -> None:
    self.recipients = list()

    if not path.exists(RECIPIENTS):
      return self.write()

    self.recipients = self.read()

  def write(self) -> None:
    with open(RECIPIENTS, 'wb') as file:
      file.write(orjson.dumps(self.recipients, option=orjson.OPT_INDENT_2))

  def read(self) -> Dict:
    with open(RECIPIENTS, 'rb') as file:
      return orjson.loads(file.read())

  def delete(self, to_delete: int) -> str:
    deleted = self.recipients.pop(to_delete)
    self.write()
    return deleted

  def add(self, to_add: str) -> None:
    self.recipients.append(to_add)
    self.write()
