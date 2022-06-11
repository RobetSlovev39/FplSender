from .hypervisor import hypervisor
from ..settings import configuration


@hypervisor.add('mailing', configuration['mail_at'])
async def mailing() -> None:
  pass
