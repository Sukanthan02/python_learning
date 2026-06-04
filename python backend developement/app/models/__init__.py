from app.core.database import Base
from app.models.user import User

# This ensures all models are loaded when importing app.models
__all__ = ["Base", "User"]
