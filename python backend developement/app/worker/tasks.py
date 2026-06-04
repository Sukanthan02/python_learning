import time
from celery.utils.log import get_task_logger
from app.core.celery_app import celery_app

logger = get_task_logger(__name__)

@celery_app.task(name="app.worker.tasks.send_welcome_email")
def send_welcome_email(email: str, name: str) ->
<truncated 930 bytes>