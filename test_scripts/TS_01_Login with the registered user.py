from libraries.generate_logs import logging


logging.debug('This message is skipped as a level is set as INFO')
logging.info('So should this')
logging.info(' this is change from user')
logging.info(' this is change from user git hub')
logging.info(' this is change from user git hub')
logging.info('This commit from git hub')
logging.info(' this is change from user git hub')
logging.info(' this is change from user git hub')

logging.warning('And this, too')
logging.error('Testing non-ASCII character, Ø and ö')

logging.info(' this is change from user B')
logging.info('So should Final')
logging.info('So should Final')
logging.info('This commit from git hub')
logging.info('This commit from git hub')
logging.info('This commit from git hub')


logging.warning('And this, too')

