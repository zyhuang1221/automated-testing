#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
from appium.webdriver.common.mobileby import MobileBy as By
from libs.common.appbase import BasePage


class Login(BasePage):
    loc_用户名 = (By.ID, 'com.wuba:id/login_username')
    loc_密码 = (By.ID, 'com.wuba:id/login_password')
    loc_同意协议并登录 = (By.ID, 'com.wuba:id/login_login_button')

    def login(self, usname, pw):
        self.my_find_element(self.loc_用户名).send_keys(usname)
        self.my_find_element(self.loc_密码).send_keys(pw)
        self.my_find_element(self.loc_同意协议并登录).click()
