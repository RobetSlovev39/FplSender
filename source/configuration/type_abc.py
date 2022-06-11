import abc
from typing import Union, Any, Dict


class Type(abc.ABC):

  def __init__(self, name: str, value: Union[Any, None]) -> None:
    self.name = name
    self.value = self.validate(value)

  @abc.abstractmethod
  def validate(self, value: Any) -> Any:
    pass

  def to_json(self) -> Dict:
    return {self.name: self.value_to_json()}

  @abc.abstractmethod
  def value_to_json(self) -> Union[int, str]:
    pass

  def change(self, new_value: Any) -> None:
    self.value = self.validate(new_value)
