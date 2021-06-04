#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 
# @Author  : Mik


from WebUiTestCases.POM import 用户登录, 我的会员中心, 个人资料信息
from selenium import webdriver
import pytest

info = ('mik2', 'password')
url = "http://127.0.0.1/index.php?m=user&c=public&a=login"


class TestCI():
    def testCase1(self, browser):
        print('开始测试')
        用户登录_page = 用户登录.Login(browser, '用户登录')
        用户登录_page.my_get_url(url)
        用户登录_page.denglu(info)
        我的会员中心_page = 我的会员中心.GerenZhongxin(browser, '我的会员中心')
        我的会员中心_page.my_click(我的会员中心_page.账号设置)
        个人资料信息_page = 个人资料信息.GeRen(browser, '个人资料信息')
        个人资料信息_page.my_click(个人资料信息_page.个人资料)
        个人资料信息_page.my_import_text(个人资料信息_page.修改姓名,'张三')
        个人资料信息_page.my_click(个人资料信息_page.修改性别)
        script = "document.getElementById('date').removeAttribute('readonly')"
        个人资料信息_page.driver.execute_script(script)
        个人资料信息_page.my_import_text(个人资料信息_page.修改生日,'1980-02-01')
        个人资料信息_page.my_import_text(个人资料信息_page.修改QQ,'23247896')
        个人资料信息_page.my_click(个人资料信息_page.确认)
        i=个人资料信息_page.my_switch_alert()
        print(i)


if __name__ == '__main__':
    pytest.main(['./change_info_test.py'])

