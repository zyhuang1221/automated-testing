#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 
# @Author  : Mik

import pytest
from libs.common.browser_init import browser_init
from libs.utils.log_module import log

url = 'http://127.0.0.1/'


# scope='session', autouse=True
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    初始化浏览器，打开配置文件里面的url，运行环境
    :return: 浏览器对象
    """
    global driver
    log.info('开始执行web自动化测试')
    dirver = browser_init()  # 调用一个方法,浏览器初始化
    yield dirver
    log.info('web自动化测试结束')


@pytest.fixture()
def base_url():
    return url

#
# @pytest.fixture(scope='session', autouse=True)
# def brower_close():
#     print('完成')
#     # yield driver
#     driver.quit()
