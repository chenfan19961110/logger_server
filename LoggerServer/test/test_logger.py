from logging.handlers import HTTPHandler

import requests
import logging


#1. 获取或创建，某一个记录器
logger=logging.getLogger('request')

#1.1 设置记录器的等级(FATUL（严重错误）50，ERROR 40，WARN 30,INFO 20，DEBUG 10，NOSET 0)
#等级高的，不会获取等级低的信息
logger.setLevel(logging.INFO)

#2. 设置日志的格式
fmt_str='[%(asctime)s %(levelname)s] %(message)s'
format=logging.Formatter(fmt=fmt_str,datefmt='%Y-%m-%d %H:%M:%S')

#3. 设置日志的处理器 Handler
# - StreamHandler 控制台输出流


handler=logging.StreamHandler()
file_handler=logging.FileHandler('test.log')
file_handler.setLevel(logging.WARN)  #设置处理的日志等级

http_handler=HTTPHandler(host='10.35.166.17:5000',
                         url='/upload_log/',
                         method="POST")
http_handler.setLevel(logging.ERROR)

logger.addHandler(handler)
logger.addHandler(file_handler)
logger.addHandler(http_handler)

logger.info('第一个普通消息的测试')
logger.debug('日志等级低的消息不会被处理')
logger.warning('警告日志会被写入文件中，同时控制台显示')
logger.critical('严重的日志信息，被上传到日志服务器，同时控制台显示')

