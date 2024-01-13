from libraries.generate_logs import logging


logging.debug('This message is skipped as a level is set as INFO')
logging.info('So should this')
logging.warning('And this, too')
logging.warning('And this, too')
logging.error('Testing non-ASCII character, Ø and ö')