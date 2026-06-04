import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Ensure the root folder is added to pythonpath so app can be imported
sys.path.insert(0, os.path.dirname(os.p
<truncated 1558 bytes>