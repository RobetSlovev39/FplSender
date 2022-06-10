from .mailing import mailing
from .hypervisor import hypervisor

import asyncio
import aioschedule


async def background() -> None:
  while True:
    await aioschedule.run_pending()
    await asyncio.sleep(1)


__ALL__ = ('hypervisor', 'background')
