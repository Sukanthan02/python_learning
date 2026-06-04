from celery import Celery
from app.core.config import settings

# Initialize Celery app
celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

# Configure Celery settings
celery
<truncated 258 bytes>