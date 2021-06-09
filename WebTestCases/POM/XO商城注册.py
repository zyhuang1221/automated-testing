#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser

class ZC(Browser):
    用户名 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input')
    设置登录密码 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input')
    注册按钮 = (By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/button')