#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class ZheCe(Browser):
    用户名 = (By.NAME, 'username')
    密码 = (By.NAME, 'password')
    确认密码 = (By.NAME, 'userpassword2')
    手机 = (By.NAME, 'mobile_phone')
    email = (By.NAME, 'email')
    注册 = (By.CLASS_NAME, 'reg_btn')

    def zhuce(self,info):

        self.my_send_key(ZheCe.用户名,info[0])
        self.my_send_key(ZheCe.密码, info[1])
        self.my_send_key(ZheCe.确认密码, info[1])
        self.my_send_key(ZheCe.手机, info[2])
        self.my_send_key(ZheCe.email, info[3])
        self.my_click(ZheCe.注册)