from libraries.generate_logs import logging


logging.debug('This message is skipped as a level is set as INFO')
logging.info('So should this')
logging.info(' this is change from user')
logging.info(' this is change from user AAAA')
logging.info(' this is change from user AAAA')
logging.info(' this is change from user AAAA')
logging.info(' this is change from user AAAA')

logging.warning('And this, too')
logging.error('Testing non-ASCII character, Ø and ö')

logging.info(' this is change from user B')
logging.info('So should thisAAAA')
logging.info('So should thisAAAA')


logging.warning('And this, too')

#done
