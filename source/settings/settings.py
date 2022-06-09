from pathlib import Path
from ..utilities import get_env_var

BASE_DIR = Path(__file__).resolve().parent.parent

TG_TOKEN = get_env_var('TG_TOKEN')
ADMIN_ID = int(get_env_var('ADMIN_ID'))
