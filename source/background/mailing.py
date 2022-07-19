from .hypervisor import hypervisor
from ..settings import configuration

from ..service import perform


@hypervisor.add('mailing', configuration['mail_at'])
async def mailing() -> None:

  await perform(
    configuration['text'],
    configuration.items['dep_time'].value,
    configuration['alt'],
    configuration['radius'],
    configuration['lat'],
    configuration['lng']
  )
