#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 
# @Author  : Mik
from selenium.webdriver import Remote
from selenium import webdriver
from libs.utils import rd_yaml
from libs.utils.log_module import logger


def browser_init():
    web_cfg_data = rd_yaml.read_yaml()['browser']
    if web_cfg_data['type'] == 'chrome':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Chrome()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "chrome",
                            })
        else:
            raise ValueError('env类型定义错误！')

    elif web_cfg_data['type'] == 'firefox':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Firefox()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "firefox",
                            })
        else:
            raise ValueError('env类型定义错误！')
    elif web_cfg_data['type'] == 'ie':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Ie()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "internet explorer",
                            })
        else:
            raise ValueError('env类型定义错误！')
    else:
        raise ValueError('driver驱动类型定义错误！')
    logger.info(f'在{web_cfg_data["env"]}使用{web_cfg_data["type"]}执行')
    driver.maximize_window()
    return driver
