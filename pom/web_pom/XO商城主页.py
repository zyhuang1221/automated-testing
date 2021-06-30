#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.base import BasePage
from pom.web_pom.XO商城登录 import Login
from pom.web_pom.XO商城注册 import Register


class HomePage(BasePage):
    # 元素定位
    __loc_注册 = (By.XPATH, '//a[text()="注册"]')
    __loc_登录 = (By.XPATH, '//a[text()="登录"]')
    url = 'http://39.98.138.157/shopxo/'

    def open_home(self):
        self.my_get_url(self.url)

    def goto_login(self):
        self.my_click(self.__loc_登录, '登录')
        return Login(self.driver, '登录')

    def goto_register(self):
        self.my_click(self.__loc_注册, '注册')
        return Register(self.driver, '注册')
