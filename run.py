#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik
import os
import pytest
from libs.utils.log_module import logger
from libs.utils.base_path import root_dir
from shutil import copyfile
from libs.utils.clear_file import clearFile

if __name__ == '__main__':
    imgdir = root_dir+r'\imgs'
    # logdir = root_dir+r'\log'
    clearFile(imgdir)
    # clearFile(logdir)
    logger.info('开始执行web自动化测试')
    pytest.main()
    logger.info('web自动化测试结束')
    source = root_dir + r'\report\environment.properties'
    target = root_dir + r'\report\xml\environment.properties'
    copyfile(source, target)
    os.system('allure generate --clean ./report/xml -o ./report/html')  # --clean 清空上次报告
