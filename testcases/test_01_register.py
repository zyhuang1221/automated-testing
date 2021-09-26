#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from pom.web_pom import XO商城登录成功, XO商城主页
from libs.utils.log_module import logger
from libs.utils.rd_yaml import load
import pytest
import allure


@allure.epic('WebUI测试')
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('用户注册模块')
class TestRegister:
    udata = load('web_data.yaml')

    def setup_class(self):

        logger.info(f'开始执行{TestRegister.__name__}模块测试')

    def teardown_class(self):
        logger.info(f'{TestRegister.__name__}模块测试完成')

    # @pytest.mark.xfail
    @allure.story('用户注册')
    @allure.title('测试数据：用户名：{user},密码：{password}')
    @pytest.mark.parametrize('user,password', udata)
    def testcase_01(self, browser, user, password):
        with allure.step('打开主页，点击注册'):
            page_主页 = XO商城主页.HomePage(browser, '商城主页')
            page_主页.open_home()
            page_注册 = page_主页.goto_register()
        with allure.step('输入用户名，点击注册'):
            page_注册.register(user, password)
            msg = page_注册.get_msg()
        with allure.step('断言'):
            try:
                assert msg == '注册成功'
            except:
                raise
            else:
                登录成功_page = XO商城登录成功.LoginSucceed(browser, '登录主页')
                登录成功_page.exit()
