from .news_schedule import SchedulerMiddleware
from loguru import logger

__all__ = [
    'SchedulerMiddleware'
]
logger.info('Middlewares are successfully configured')
