#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 
# @Author  : Mik

import pytest
from WebUiTestCases.POM import 主页, 用户注册
from libs.utils.log_module import log
from libs.utils import rw_xlsx

read_xlsx = rw_xlsx.ReadExcel()
info = read_xlsx.get_rowdata(3)
# info = ('mik2', 'password', '15732573434', '1237645688@qq.com')
class TestZc():
    def setup_class(self):
        log.info('开始执行TestZc测试')

    def teardown_class(self):
        log.info('TestZc测试完成')

    def testcase1(self, browser,base_url):
        主页_page = 主页.HomePage(browser)
        主页_page.get_url(base_url)
        allhd = 主页_page.get_all_handles()
        主页_page.zhuce()
        主页_page.switch_window(name='new', all_handles=allhd)
        用户注册_page = 用户注册.ZheCe(browser)
        用户注册_page.zhuce(info)


if __name__ == '__main__':
    pytest.main(['./register_test.py'])
