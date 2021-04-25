#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from libs.utils import rd_yaml

web_cfg_data = rd_yaml.read_yaml()['browser']
print(web_cfg_data['url'])

def browser_init():
    if web_cfg_data['type'] == 'chrome':
        driver = webdriver.Chrome()
    elif web_cfg_data['type'] == 'firefox':
        driver = webdriver.Firefox()
    elif web_cfg_data['type'] == 'ie':
        driver = webdriver.Ie()
    elif web_cfg_data['type'] == 'grid':
        driver = webdriver.Remote(command_executor='', desired_capabilities={})
    else:
        raise NameError('driver驱动类型定义错误！')
    driver.get(web_cfg_data['url'])
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


browser_init()