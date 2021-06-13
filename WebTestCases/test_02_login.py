#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 
# @Author  : Mik
from WebTestCases.POM import XO商城主页, XO商城登录, XO商城登录成功页面
from libs.utils.log_module import logger
from libs.utils import rw_xlsx
import pytest
from time import sleep
import allure

readInfo = rw_xlsx.ReadExcel()
userinfo = readInfo.get_rows(1, readInfo.row_max1)


@allure.epic('WebUI测试')
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('用户登录模块')
class TestLogin:

    def setup_class(self):
        logger.info(f'开始执行{TestLogin.__name__}模块测试')

    def teardown_class(self):
        logger.info(f'{TestLogin.__name__}模块测试完成')

    # @pytest.mark.xfail
    @allure.story('用户登录')
    @allure.title('测试数据：{user},{password}')
    @pytest.mark.parametrize('user,password', userinfo)
    def testcase_01(self, browser, base_url, user, password):
        with allure.step('打开主页，点击注册'):
            主页_page = XO商城主页.HomePage(browser)
            主页_page.my_get_url(base_url)
            主页_page.my_click(主页_page.登录)
        with allure.step('输入用户名，点击注册'):
            登录_page = XO商城登录.Login(browser)
            登录_page.login((user, password))
        with allure.step('断言'):
            msg = 登录_page.my_get_text(登录_page.登录弹出信息)
            try:
                assert msg == '登录成功'
            except:
                raise
            else:
                登录成功_page = XO商城登录成功页面.DLCG(browser)
                登录成功_page.my_click(登录成功_page.退出登录)
