from ..settings import MAIL_AT
from .hypervisor import hypervisor


@hypervisor.add('mailing', MAIL_AT)
async def mailing() -> None:
  pass
