#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 
# @Author  : Mik


import pytest
from WebUiTestCases.POM import baidu


def testcase1(browser):
    browser.send_keys(baidu.搜索输入框, 'python')
    browser.click(baidu.点击百度)


if __name__ == '__main__':
    pytest.main()
