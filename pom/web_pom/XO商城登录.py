#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 
# @Author  : Mik


from selenium.webdriver.common.by import By
from libs.common.browser_init import BasePage


class Login(BasePage):
    loc_用户名 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input')
    loc_密码 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input')
    loc_提交 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input')
    loc_登录弹出信息 = (By.CLASS_NAME, 'prompt-msg')

    def login(self, user, pw):
        self.my_import_text(self.loc_用户名, user)
        self.my_import_text(self.loc_密码, pw)
        self.my_submit(self.loc_提交)

    def get_msg(self):
        return self.my_get_text(self.loc_登录弹出信息)