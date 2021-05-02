#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class Login(Browser):
    用户名 = (By.ID, 'username')
    密码 = (By.ID, 'password')
    提交 = (By.CLASS_NAME,'login_btn')

    def denglu(self, value):
        self.my_send_key(Login.用户名, value[0])
        self.my_send_key(Login.密码, value[1])
        self.my_submit(Login.提交)
