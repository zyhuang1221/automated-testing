#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from WebUiTestCases.POM import XO商城主页, XO商城注册, XO商城登录成功页面
from libs.utils.log_module import logger
from libs.utils import rw_xlsx
import pytest
from time import sleep
import allure

# driver = webdriver.Chrome()
# driver.maximize_window()
readInfo = rw_xlsx.ReadExcel()
userinfo = readInfo.get_rows(1, readInfo.row_max1)


@allure.epic('WebUI测试')
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('用户注册模块')
class TestZc():

    def setup_class(self):
        logger.info(f'开始执行{TestZc.__name__}测试')

    def teardown_class(self):
        logger.info(f'{TestZc.__name__}测试完成')

    # @pytest.mark.xfail
    @allure.title('用户注册')
    @pytest.mark.parametrize('user,password', userinfo)
    def testcase1(self, browser, base_url, user, password):
        with allure.step('打开主页，点击注册'):
            主页_page = XO商城主页.HomePage(browser)
            主页_page.my_get_url(base_url)
            主页_page.my_click(主页_page.注册)
        with allure.step('输入用户名，点击注册'):
            注册_page = XO商城注册.ZC(browser)
            注册_page.my_import_text(注册_page.用户名, user)
            注册_page.my_import_text(注册_page.设置登录密码, password)
            # 注册_page.my_click(注册_page.注册按钮)
            注册_page.my_submit(注册_page.设置登录密码)
        # with allure.step('断言'):
        #     msg1 = 注册_page.my_switch_alert()
            # print(msg1)
            # logger.info(msg1)

        with allure.step('注册断言'):
            登录成功_page = XO商城登录成功页面.DLCG(browser)


            try:
                text = 登录成功_page.my_get_text(登录成功_page.欢迎)

            # text='12121'
            # assert '欢迎来到' in text
                if '欢迎来到' in text:
                    logger.info('注册成功')
                    登录成功_page.my_click(登录成功_page.退出登录)

                else:
                    raise AssertionError('注册失败')
            except Exception as e:
                raise e
        sleep(3)

# zc=TestZc()
# zc.testcase1(driver,'http://123.56.183.84/')
