#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import BasePage


class LoginSucceed(BasePage):
    loc_欢迎 = (By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/em[2]')
    loc_退出登录 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[1]/a[2]')

    def exit(self):
        self.my_click(self.loc_退出登录)
