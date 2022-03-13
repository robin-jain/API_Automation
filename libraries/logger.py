import logging as log

handler=log.StreamHandler()
logg=log.getLogger('Report_logger')
FORMAT="%(asctime)s - %(levelname)s -%(name)s - %(message)s"
#FORMAT="%(asctime)s [%(levelname)s] %(message)s",
format=log.Formatter(FORMAT)
handler.setFormatter(format)
logg.addHandler(handler)
logg.setLevel(log.INFO)