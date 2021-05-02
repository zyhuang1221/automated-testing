#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 
# @Author  : Mik

import pytest
from libs.common.browser_init import browser_init, Browser
from selenium import webdriver


@pytest.fixture()  # 返回值
def browser():
    """初始化浏览器"""
    # excute_sql('select limit 5 from user ')
    # print('浏览器基础设置，打开配置文件里面的url，运行环境')
    dirver = browser_init()  # 调用一个方法,浏览器初始化
    # d = Browser(dirver)  # web自动化操作
    yield dirver
    # print('后置')
