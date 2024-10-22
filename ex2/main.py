import  functions_framework
import logging
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@functions_framework.http
def cron_function(request):
    now = datetime.datetime.now()
    logger.info(f'Current Time: {now}')
    return f'Current Time Logged Successfully: {now}'