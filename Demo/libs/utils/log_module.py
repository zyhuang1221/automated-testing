#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 
# @Author  : Mik


import logging
import os
import datetime


class Logger():
    def __init__(self):
        """创建日志器"""
        self.log = logging.getLogger()
        self.log.setLevel(level=logging.DEBUG)

    def add_Formatter(self):
        """设置格式器"""
        self.f1 = logging.Formatter(fmt='[%(asctime)s]：[%(levelname)s] -->>%(message)s')
        self.f2 = logging.Formatter(fmt='[%(filename)s]: [%(levelname)s]  [%(asctime)s]：%(lineno)d-->>%(message)s',
                                    datefmt='%Y-%m-%d %H:%M:%S')
        return self.f1, self.f2

    def add_StreanHandle(self, level=logging.INFO):
        """添加控制台处理器"""
        self.s_hand = logging.StreamHandler()
        self.s_hand.setLevel(level)
        self.s_hand.setFormatter(self.add_Formatter()[0])  # 添加控制台格式器f1
        return self.s_hand

    def add_FileHandle(self, file, level=logging.DEBUG):
        """添加文件处理器"""
        self.f_hand = logging.FileHandler(filename=file, encoding='utf-8')
        self.f_hand.setLevel(level)
        self.f_hand.setFormatter(self.add_Formatter()[1])  # 添加文件格式器f2
        return self.f_hand

    def get_log(self, handler='all', file='api'):
        """
        返回日志
        :param handler: 默认输出控制台和文件，strean参数输出控制台,file参数输出到文件
        :param file: 默认log文件名API
        :return: log
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        file_dir = os.path.dirname(__file__).replace(r'\/'.replace(os.sep, ''), os.sep)
        # path_file = file_dir.replace(r'libs\utils', r'log\{}_{}.log'.format(file, now_time))
        path_file = file_dir.replace('libs', 'log').replace('utils', '{}_{}.log'.format(file, now_time))
        if handler == "all":
            # 日志器添加控制台处理器
            self.log.addHandler(self.add_StreanHandle())
            # 日志器添加文件处理器
            self.log.addHandler(self.add_FileHandle(path_file))
            return self.log
        elif handler == 'strean':
            self.log.addHandler(self.add_StreanHandle())
            return self.log
        elif handler == 'file':
            self.log.addHandler(self.add_FileHandle(path_file))
            return self.log
        else:
            raise ValueError("参数错误")


if __name__ == '__main__':
    l = Logger()
    # 调用get_log
    log = l.get_log(handler='file')
    log.critical('critical严重错误')
    log.error('error错误')
    log.warning('warning警告')
    log.info('info信息')
    log.debug('debug调试日志')
