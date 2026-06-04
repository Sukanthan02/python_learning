from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# Create SQLAlchemy engine
# pool_pre_ping=True enables automatic connection health-che
<truncated 524 bytes>