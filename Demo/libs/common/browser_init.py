#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from libs.utils import rd_yaml
from libs.utils import log_module
import time
# from datetime import datetime
from selenium.webdriver.common.by import By
from libs.utils.base_path import base_path

web_cfg_data = rd_yaml.read_yaml()['browser']


def browser_init():
    global driver
    if web_cfg_data['type'] == 'chrome':
        driver = webdriver.Chrome()
    elif web_cfg_data['type'] == 'firefox':
        driver = webdriver.Firefox()
    elif web_cfg_data['type'] == 'ie':
        driver = webdriver.Ie()
    else:
        raise NameError('driver驱动类型定义错误！')
    driver.get(web_cfg_data['url'])
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


class Browser():
    """封装浏览器操作，传入实例化driver"""

    def __init__(self, driver):
        self.driver = driver
        l = log_module.Logger()
        self.log = l.get_log('strean', file='web')

    def wait_element_visible(self, loc, t=10):
        """每次操作之前自动显示等待,找到元素，并返回元素对象"""
        try:
            self.log.info('开始等待页面元素<{}>是否可见！'.format(loc))
            start_time = time.time()
            ele = WebDriverWait(self.driver, t).until(EC.visibility_of_element_located(loc))
            return ele
        except Exception as e:
            self.log.error('等待页面元素<{}>失败！'.format(loc))
            # self.driver.save_screenshot(base_path+r'\img_1\test.png')
            # raise e
        else:
            end_time = time.time()
            self.log.info('页面元素<{}>等待可见，等待时间：{}秒'.format(loc, round(end_time - start_time, 1)))
            print(round(end_time - start_time, 1))



    def send_keys(self, loc, value):
        self.wait_element_visible(loc).send_keys(value)
        self.log.info('在{0}输入{0}'.format(loc[1], value))

    def click(self, loc):
        self.wait_element_visible(loc).click()
        self.log.info('点击{0}'.format(loc[1]))

driver= webdriver.Chrome()
driver.get('http://www.baidu.com')
web=Browser(driver)
web.send_keys((By.ID, 'kw'),'python')




