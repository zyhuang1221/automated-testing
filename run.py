#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik
import os
import pytest
from libs.utils.log_module import log

if __name__ == '__main__':
    log.info('开始执行web自动化测试')
    pytest.main()
    log.info('web自动化测试结束')
#    os.system('allure generate --clean ./report/xml -o ./report/html')  #--clean

