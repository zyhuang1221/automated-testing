#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import BasePage
from pom.web_pom.XO商城登录 import Login
from pom.web_pom.XO商城注册 import Register


class HomePage(BasePage):
    # 元素定位
    __loc_注册 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/a[2]')
    __loc_登录 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/a[1]')
    url = 'http://123.56.183.84/'

    def open_home(self):
        self.my_get_url(self.url)

    def goto_login(self):
        self.my_click(self.__loc_登录)
        return Login(self.driver)

    def goto_register(self):
        self.my_click(self.__loc_注册)
        return Register(self.driver)
