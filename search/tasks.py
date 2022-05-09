from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask
from celery.utils.log import get_task_logger
from celery import Celery
from search.utils import saveListing

logger = get_task_logger(__name__)

def task_save_latest_ebay():
    """
    Saves latest image from ebay
    """
    saveListing()
    logger.info("Saved listing from ebay")