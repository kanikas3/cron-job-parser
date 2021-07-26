import logging

def setup_logger():
    logging.basicConfig(filename="output.log", encoding="utf-8", level=logging.DEBUG)
    logger = logging.getLogger('cron-job-parser')
    logger.setLevel(logging.DEBUG)