from libraries.generate_logs import logging


logging.debug('This message is skipped as a level is set as INFO')
logging.info('So should this')
logging.info(' this is change from user')
logging.info(' this is change from user Final')
logging.info(' this is change from user Final')


logging.warning('And this, too')

