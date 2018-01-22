import logging
import os
import sys
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


def getTrackInfo():
	try:
		raise Exception
	except:
		# sys.exc_info() return (type, value/message, traceback)
		f = sys.exc_info()[2].tb_frame.f_back.f_back  # 简单封装下  后面在处理
	finally:
		return (f.f_code.co_filename, f.f_code.co_name, f.f_lineno)


filePath = os.path.join(os.getcwd(), "../log")
if not os.path.exists(filePath):
	print(filePath)
	os.makedirs(filePath)


# format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
# datefmt = '%a, %d %b %Y %H:%M:%S'
# filename = 'myapp.log'
# filemode = 'w'

# basic 配置, 如果未指定文件, 那么就从stderr输出
# logging.basicConfig(level=logging.DEBUG, format=format, datefmt=datefmt)


# 日志过滤器
class LoggerFilter(logging.Filter):
	def __init__(self, name='', level=logging.DEBUG):
		super(LoggerFilter, self).__init__(name)
		self.level = level

	def filter(self, record):
		return record.levelno == self.level


# 根据大小分割文件
class SizeLogger(object):
	logger = logging.getLogger("SizeLog")

	def __init__(self, level=logging.DEBUG, maxBytes=10 * 1024 * 1024):
		# 创建日志对象, 添加级别
		SizeLogger.logger.setLevel(level)
		# 设置日志文件名和管理器
		debug_filename = time.strftime("%Y-%m-%d") + '_debug' + '.log'
		debug_filename = os.path.join(filePath, debug_filename)
		debug_file = RotatingFileHandler(debug_filename, mode='a', maxBytes=maxBytes, backupCount=10, encoding='utf-8')
		info_filename = time.strftime("%Y-%m-%d") + '_info' + '.log'
		info_filename = os.path.join(filePath , info_filename)
		info_file = RotatingFileHandler(info_filename, mode='a', maxBytes=maxBytes, backupCount=10, encoding='utf-8')
		info_file.setLevel(level=logging.INFO)
		error_filename = time.strftime("%Y-%m-%d") + '_error' + '.log'
		error_filename = os.path.join(filePath,  error_filename)
		error_file = RotatingFileHandler(error_filename, mode='a', maxBytes=maxBytes, backupCount=10, encoding='utf-8')

		# 每行日志的前缀设置
		# '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s thread-%(thread)d: %(message)s'
		formatter = logging.Formatter(
			'%(asctime)s %(levelname)s thread-%(thread)d %(message)s')
		debug_file.setFormatter(formatter)
		info_file.setFormatter(formatter)
		error_file.setFormatter(formatter)

		# 为每个文件增加日志过滤, 仅显示本级别的日志
		debug_filter = LoggerFilter(level=logging.DEBUG)
		info_filter = LoggerFilter(level=logging.INFO)
		error_filter = LoggerFilter(level=logging.ERROR)
		debug_file.addFilter(debug_filter)
		info_file.addFilter(info_filter)
		error_file.addFilter(error_filter)

		# logger对象增加文件管理器
		SizeLogger.logger.addHandler(debug_file)
		SizeLogger.logger.addHandler(info_file)
		SizeLogger.logger.addHandler(error_file)

	def debug(self, *args, **kwargs):
		SizeLogger.logger.debug("where:%s, msg:%s", getTrackInfo(), args, **kwargs)

	def info(self, *args, **kwargs):
		SizeLogger.logger.info("where:%s, msg:%s", getTrackInfo(), args, **kwargs)

	def error(self, *args, **kwargs):
		SizeLogger.logger.error("where:%s, msg:%s", getTrackInfo(), args, **kwargs)


# 根据时间分割文件
class TimeLogger(object):
	# 注意 getLogger 的名字不能一样, 否则找到的是同一个logging对象, 日志输出多次
	logger = logging.getLogger("TimeLog")  # 给logging对象命名

	def __init__(self, level=logging.DEBUG, maxBytes=10 * 1024 * 1024):
		# 创建日志对象, 添加级别
		TimeLogger.logger.setLevel(level)
		# 设置日志文件名和管理器
		debug_filename = time.strftime("%Y-%m-%d") + '_debug' + '.log'
		debug_filename = os.path.join(filePath, debug_filename)
		debug_file = TimedRotatingFileHandler(debug_filename, when='MIDNIGHT', backupCount=10, encoding='utf-8')
		info_filename = time.strftime("%Y-%m-%d") + '_info' + '.log'
		info_filename = os.path.join(filePath ,  info_filename)
		info_file = TimedRotatingFileHandler(info_filename, when='MIDNIGHT', backupCount=10, encoding='utf-8')
		info_file.setLevel(level=logging.INFO)
		error_filename = time.strftime("%Y-%m-%d") + '_error' + '.log'
		error_filename = os.path.join(filePath , error_filename)
		error_file = TimedRotatingFileHandler(error_filename, when='MIDNIGHT', backupCount=10, encoding='utf-8')

		# 每行日志的前缀设置
		# '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s thread-%(thread)d: %(message)s'
		formatter = logging.Formatter(
			'%(asctime)s %(levelname)s thread-%(thread)d %(message)s')
		debug_file.setFormatter(formatter)
		info_file.setFormatter(formatter)
		error_file.setFormatter(formatter)

		# 为每个文件增加日志过滤, 仅显示本级别的日志
		debug_filter = LoggerFilter(level=logging.DEBUG)
		info_filter = LoggerFilter(level=logging.INFO)
		error_filter = LoggerFilter(level=logging.ERROR)
		debug_file.addFilter(debug_filter)
		info_file.addFilter(info_filter)
		error_file.addFilter(error_filter)

		# logger对象增加文件管理器
		TimeLogger.logger.addHandler(debug_file)
		TimeLogger.logger.addHandler(info_file)
		TimeLogger.logger.addHandler(error_file)

	def debug(self, *args, **kwargs):
		TimeLogger.logger.debug("where:%s, msg:%s", getTrackInfo(), args, **kwargs)

	def info(self, *args, **kwargs):
		TimeLogger.logger.info("where:%s, msg:%s", getTrackInfo(), args, **kwargs)

	def error(self, *args, **kwargs):
		TimeLogger.logger.error("where:%s, msg:%s", getTrackInfo(), args, **kwargs)


sizeLog = SizeLogger()
timeLog = TimeLogger()

# 日志输出
# logger.debug('for debug')
# logger.info('for info')
# logger.error('for error')
