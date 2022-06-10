from typing import Union
from datetime import datetime


def validate_time(time_string: str, raise_exception: bool = False) -> Union[datetime, None]:

  try:
    return datetime.strptime(time_string, '%H:%M')
  except ValueError as error:

    if raise_exception:
      raise error
