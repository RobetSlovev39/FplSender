from pathlib import Path
from ..utilities import get_env_var

BASE_DIR = Path(__file__).resolve().parent.parent

TG_TOKEN = get_env_var('TG_TOKEN')
ADMIN_ID = int(get_env_var('ADMIN_ID'))

MAIL_HOSTNAME = get_env_var('MAIL_HOSTNAME')
MAIL_SENDER = get_env_var('MAIL_SENDER')
MAIL_PASSWORD = get_env_var('MAIL_PASSWORD')
MAIL_PORT = get_env_var('MAIL_PORT', 587)
MAIL_USE_TLS = bool(get_env_var('MAIL_USE_TLS', 0))
