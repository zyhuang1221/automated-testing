#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.base import BasePage


class Register(BasePage):
    # 元素定位
    loc_用户名 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input')
    loc_设置登录密码 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input')
    loc_注册按钮 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/button')
    loc_弹出信息 = (By.XPATH, '//*[@id="common-prompt"]/p')
    loc_阅读并同意 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label')

    def register(self, user, pw):
        self.my_sendkeys(self.loc_用户名, user, msg='用户名输入框')
        self.my_sendkeys(self.loc_设置登录密码, pw, msg='密码输入框')
        self.my_click(self.loc_阅读并同意, msg='阅读并同意')
        self.my_submit(self.loc_设置登录密码)
        return self

    def get_msg(self):
        return self.my_get_text(self.loc_弹出信息, '弹出框')
