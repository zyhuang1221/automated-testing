#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import BasePage


class HomePage(BasePage):
    注册 = (By.LINK_TEXT, '注册')
    登录 = (By.LINK_TEXT, '登录')

    def zhuce(self):
        self.my_click(HomePage.注册)

    def denglu(self):
        self.my_click(HomePage.登录)



