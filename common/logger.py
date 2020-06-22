#-*- coding: UTF-8 -*-
import logging
import time
import os
class Logger(object):
    def __init__(self, logger):

        # 创建一个log
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        # 获取本地实际，转换为设置的格式
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 设置所有日志和错误日志的存放路径
        path = os.path.dirname(os.path.abspath('.'))
        all_logs_path = path + '/logs/All_logs/'
        error_logs_path = path + '/logs/Error_logs/'

        # 设置日志名
        all_log_name = all_logs_path + rq + '.log'
        error_log_name = error_logs_path + rq + '.log'

        # 创建handler
        # 创建handler用于写入日志
        fh = logging.FileHandler(all_log_name)
        fh.setLevel(logging.INFO)

        # 创建handler用于写错误日志
        eh = logging.FileHandler(error_log_name)
        eh.setLevel(logging.ERROR)

        # 创建一个handler用于输出控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 定义格式
        # 以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        # 以时间-日志器名称-日志级别-文件名-函数函数-错误内容的形式展示
        error_log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)
        sh.setFormatter(all_log_formatter)

        # 将logger添加给handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        self.logger.addHandler(eh)



    def getlog(self):
        return self.logger










