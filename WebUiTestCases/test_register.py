#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
import pytest
from WebUiTestCases.POM import XO商城主页, XO商城注册, XO商城登录成功页面
from libs.utils.log_module import log
from libs.utils import rw_xlsx
from selenium import webdriver
import pytest
from time import sleep

# driver = webdriver.Chrome()
# driver.maximize_window()
readInfo = rw_xlsx.ReadExcel()
userinfo = readInfo.get_rows(1, readInfo.row_max1)
base_url = 'http://123.56.183.84/'


class TestZc():

    def setup_class(self):
        log.info('开始执行TestZc测试')

    def teardown_class(self):
        log.info('TestZc测试完成')

    @pytest.mark.parametrize('user,password', userinfo)
    def testcase1(self, browser, user, password):
        主页_page = XO商城主页.HomePage(browser)
        主页_page.get_url(base_url)
        主页_page.my_click(主页_page.注册)
        注册_page = XO商城注册.ZC(browser)
        注册_page.my_import_text(注册_page.用户名, user)
        注册_page.my_import_text(注册_page.设置登录密码, password)
        注册_page.my_click(注册_page.注册按钮)
        登录成功_page = XO商城登录成功页面.DLCG(browser)
        text = 登录成功_page.my_get_text(登录成功_page.欢迎)
        try:
            assert '欢迎来到' in text
        except Exception as e:
            raise e
        sleep(3)


# zc=TestZc()
# zc.testcase1(driver,'http://123.56.183.84/')
