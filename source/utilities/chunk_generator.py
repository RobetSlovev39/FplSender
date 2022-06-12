from typing import Sequence, Any


def chunk_generator(data: Sequence[Any], chunk_size: int) -> Sequence[Any]:
  for counter in range(0, len(data), chunk_size):
    yield data[counter:counter + chunk_size]
