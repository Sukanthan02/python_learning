import time
from celery.utils.log import get_task_logger
from app.core.celery_app import celery_app

logger = get_task_logger(__name__)

@celery_app.task(name="app.worker.tasks.send_welcome_email")
def send_welcome_email(email: str, name: str) -> bool:
    logger.info(f"Simulating sending welcome email to {email}")
    time.sleep(2)
    logger.info(f"Welcome email successfully sent to {email}")
    return True

@celery_app.task(name="app.worker.tasks.long_running_calculation")
def long_running_calculation(x: int, y: int) -> int:
    logger.info(f"Starting calculation for {x} and {y}")
    time.sleep(5)
    result = x * y
    logger.info(f"Calculation complete. Result: {result}")
    return result
