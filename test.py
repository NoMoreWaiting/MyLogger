import logging
import sys
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


class LogLevelFilter(logging.Filter):

	def __init__(self, name='', level=logging.DEBUG):
		super(LogLevelFilter, self).__init__(name)
		self.level = level

	def filter(self, record):
		return record.levelno == self.level



# 日志分级别文件输出
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh_info = logging.FileHandler('logging_info.log')
fh_info.setLevel(logging.INFO)
fh_debug = logging.FileHandler('logging_debug.log')
fh_debug.setLevel(logging.DEBUG)
filter_info = LogLevelFilter(level=logging.INFO)
filter_debug = LogLevelFilter(level=logging.DEBUG)
fh_info.addFilter(filter_info)
fh_debug.addFilter(filter_debug)
logger.addHandler(fh_info)
logger.addHandler(fh_debug)
logger.debug('for debug')
logger.info('for info')
logger.error('for error')

fromat = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
datefmt = '%a, %d %b %Y %H:%M:%S'
filename = 'myapp.log'
filemode = 'w'

logging.basicConfig(level=logging.DEBUG, format=fromat, datefmt=datefmt, filename=filename, filemode=filemode)



# 日志同时输出到控制台
# 默认stderr.
# console = logging.StreamHandler(sys.stderr) # sys.stdout
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# 为空指向标准输出
logging.getLogger().addHandler(console)

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error("This is error message")
logging.critical("This is critical message")



# 日志文件分割
# # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler(filename, maxBytes=10 * 1024 * 1024, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
# getLogger("logname") 是从配置文件中读取的. 这里用不到
logging.getLogger().addHandler(Rthandler)



# 每日凌晨分割日志
trHandler = TimedRotatingFileHandler('timeRotating.log', when='MIDNIGHT', backupCount=10)
