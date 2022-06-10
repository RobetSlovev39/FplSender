from pathlib import Path
from ..utilities import get_env_var, validate_time

BASE_DIR = Path(__file__).resolve().parent.parent

MAIL_AT = validate_time(get_env_var('MAIL_AT'))

TG_TOKEN = get_env_var('TG_TOKEN')
ADMIN_ID = int(get_env_var('ADMIN_ID'))
