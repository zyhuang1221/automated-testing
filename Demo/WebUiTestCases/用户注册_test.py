#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 
# @Author  : Mik

import pytest
from selenium import webdriver
from WebUiTestCases.POM import 主页, 用户注册

info = ('mik2', 'password', '15732573434', '1237645688@qq.com')
# driver = webdriver.Chrome()
# driver.get('http://127.0.0.1')

class TestYuce():
    def testcase1(self, browser):
        page = 主页.HomePage(browser)
        allhd = page.get_all_handles()
        page.zhuce()
        page.switch_window(name='new', all_handles=allhd)
        page = 用户注册.ZheCe(browser)
        page.zhuce(info)


if __name__ == '__main__':
    pytest.main(['./用户注册_test.py'])
