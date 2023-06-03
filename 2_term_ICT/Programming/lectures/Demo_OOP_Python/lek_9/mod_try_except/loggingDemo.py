# Применение модуля logging  для записи сообщений в log-file
# that stores all 5 message levels.
# Record log entries to test it then view the file content

import logging, os, platform, datetime

timestring = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")

logfile = 'python_' + timestring + '.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG,format='%(asctime)s_%(levelname)s: %(message)s')
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an eror message.')
logging.critical('This is a critical message.')

if platform.system() == 'Windows':
    os.system('type ' + logfile)
else:
    os.system('cat ' + logfile)
