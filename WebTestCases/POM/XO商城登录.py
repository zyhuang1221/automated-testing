#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 
# @Author  : Mik


from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class Login(Browser):
    用户名 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input')
    密码 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input')
    提交 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input')
    登录弹出信息 = (By.CLASS_NAME, 'prompt-msg')

    def login(self, value):
        self.my_import_text(Login.用户名, value[0])
        self.my_import_text(Login.密码, value[1])
        self.my_submit(Login.提交)
