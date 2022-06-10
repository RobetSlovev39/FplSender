from pathlib import Path

from ..types import MailAt
from ..utilities import get_env_var

BASE_DIR = Path(__file__).resolve().parent.parent

MAIL_AT = MailAt(get_env_var('MAIL_AT'))

TG_TOKEN = get_env_var('TG_TOKEN')
ADMIN_ID = int(get_env_var('ADMIN_ID'))
