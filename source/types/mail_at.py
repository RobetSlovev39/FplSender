from ..utilities import validate_time, to_utc

from datetime import datetime
from typing import Union, Tuple, Dict


class MailAt:

  def __init__(self, time: Union[str, datetime]) -> None:
    self.change(time)

  def change(self, time: Union[str, datetime]) -> None:
    self.mail_at = self.__process_time(time)

  def strftime(self, *args: Tuple, **kwargs: Dict) -> str:
    return self.mail_at.strftime(*args, **kwargs)

  def __process_time(self, time: Union[str, datetime]) -> datetime:
    return to_utc(validate_time(time)) if type(time) is not datetime else time
