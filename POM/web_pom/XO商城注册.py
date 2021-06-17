#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import BasePage


class Register(BasePage):
    # 元素定位
    loc_用户名 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input')
    loc_设置登录密码 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input')
    loc_注册按钮 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/button')
    loc_弹出信息 = (By.CLASS_NAME, 'prompt-msg')

    def register(self, user, pw):
        self.my_import_text(self.loc_用户名, user)
        self.my_import_text(self.loc_设置登录密码, pw)
        self.my_submit(self.loc_注册按钮)
        return self

    def get_msg(self):
        return self.my_get_text(self.loc_弹出信息)
