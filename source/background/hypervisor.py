from ..utilities import validate_time

import aioschedule
from datetime import datetime

from typing import (
  Union,
  Callable,
  Coroutine,
  Tuple,
  Dict
)


class Hypervisor:

  def __init__(self) -> None:
    self.tasks = dict()

  def __time_to_run(self, run_at: Union[datetime, str]) -> str:
    if type(run_at) is str:
      run_at = validate_time(run_at, raise_exception=True)

    return run_at.strftime('%H:%M')

  def add(self, name: str, run_at: Union[datetime, str], *args: Tuple, **kwargs: Dict) -> Callable:
    run_at = self.__time_to_run(run_at)

    def decorator(function: Coroutine) -> Coroutine:
      task = aioschedule.every().day.at(run_at).do(function, *args, **kwargs)

      if name in self.tasks:
        aioschedule.cancel_job(task)
        raise KeyError('Task with this name already exists')

      self.tasks[name] = (task, function)

      async def wrapper(*args: Tuple, **kwargs: Dict) -> None:
        return await function(*args, **kwargs)

      return wrapper

    return decorator

  def reschedule_task(self, name: str, run_at: Union[datetime, str], *args: Tuple, **kwargs: Dict) -> None:
    if name not in self.tasks:
      raise KeyError('Task with this name does not exist')

    task, function = self.tasks.pop(name)
    aioschedule.cancel_job(task)

    run_at = self.__time_to_run(run_at)
    task = aioschedule.every().day.at(run_at).do(function, *args, **kwargs)

    self.tasks[name] = (task, function)


hypervisor = Hypervisor()
