#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 
# @Author  : Mik
from pom.web_pom import XO商城登录成功, XO商城登录, XO商城主页
from libs.utils.log_module import logger
from libs.utils import rw_xlsx
from libs.utils.rd_yaml import load
import pytest
import allure


@allure.epic('WebUI测试')
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('用户登录模块')
class TestLogin:
    udata = load('web_data.yaml')

    def setup_class(self):
        logger.info(f'开始执行{TestLogin.__name__}模块测试')

    def teardown_class(self):
        logger.info(f'{TestLogin.__name__}模块测试完成')

    # @pytest.mark.xfail
    @allure.story('用户登录')
    @allure.title('测试数据：用户名：{user},密码：{password}')
    @pytest.mark.parametrize('user,password', udata)
    def testcase_01(self, browser, user, password):
        with allure.step('打开主页，点击登录'):
            page_主页 = XO商城主页.HomePage(browser)
            page_主页.open_home()
            page_登录 = page_主页.goto_login()
        with allure.step('输入用户名密码，点击确认'):
            page_登录.login(user,password)
            msg = page_登录.get_msg()
        with allure.step('断言'):
            try:
                assert msg == '登录成功'
            except:
                raise
            else:
                登录成功_page = XO商城登录成功.LoginSucceed(browser)
                登录成功_page.exit()
