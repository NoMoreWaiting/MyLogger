from logger import timeLog as log
import sys
import os

# log.debug('for debug ====%d', 'dddddd')
# log.info('for info %d', 555)
# log.error('for error', ',,,,', 5986, 8880.222)


# print(os.getcwd())
# filePath = os.path.join(os.getcwd(), "log")
# print(filePath)

def getTrackInfo():
	try:
		raise Exception
	except:
		for x in sys.exc_info():
			print(x)
		# sys.exc_info() return (type, value/message, traceback)
		f2 = sys.exc_info()[2].tb_frame.f_back.f_back  # 简单封装下  后面在处理

	finally:
		# print(f2.f_code.co_filename, f2.f_code.co_name, f2.f_lineno)
		return (f2.f_code.co_filename, f2.f_code.co_name, f2.f_lineno)


def f1():
	filename, name, lineno = getTrackInfo()
	print(filename, name, lineno)


def f2():
	print("ddddd")
	log.debug('for debug ====%d', 'dddddd')
	log.info('for info %d', 555)
	log.error('for error', ',,,,', 5986, 8880.222)
	# f1()

def f3():
	f2()


if __name__ == '__main__':
	f3()
