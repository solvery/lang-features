#encoding=utf-8

import logging

logging.basicConfig(
        filename="config.log",
        filemode="w",
        format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
        level=logging.INFO);

#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
