#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 
# @Author  : Mik


from selenium.webdriver.common.by import By
from libs.common.base import BasePage


class Login(BasePage):
    loc_用户名 = (By.XPATH, '//input[@placeholder="用户名/手机/邮箱"]')
    loc_密码 = (By.XPATH, '//input[@placeholder="登录密码"]')
    loc_提交 = (By.XPATH, '//input[@placeholder="登录密码"]')
    loc_登录弹出信息 = (By.XPATH, '//*[@id="common-prompt"]/p')

    def login(self, user, pw):
        self.my_sendkeys(self.loc_用户名, user, msg='用户名输入框')
        self.my_sendkeys(self.loc_密码, pw, msg='密码输入框')
        self.my_submit(self.loc_提交)

    def get_msg(self):
        return self.my_get_text(self.loc_登录弹出信息, '弹出框')
