#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 
# @Author  : Mik


from libs.common.browser_init import browser_init
from libs.utils.base_path import root_dir
from libs.utils.log_module import logger
from libs.utils import rw_properties
import pytest

url = 'http://123.56.183.84/'


# scope='session', autouse=True
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    初始化浏览器，打开配置文件里面的url，运行环境
    :return: 浏览器对象
    """
    global driver
    logger.info('打开浏览器')
    driver = browser_init()  # 调用一个方法,浏览器初始化
    # 获取浏览器信息
    browserver = driver.capabilities['version']
    browserName = driver.capabilities['browserName']
    # 写入浏览器信息到allure报告环境
    file = root_dir + r'\report\environment.properties'
    rw = rw_properties.parse(file)
    rw.put('BrowserVer', browserver)
    rw.put('Browser', browserName)
    yield driver
    logger.info('关闭浏览器')
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def base_url():
    return url

#
# @pytest.fixture(scope='session', autouse=True)
# def brower_close():
#     print('完成')
#     # yield driver
#     driver.quit()
