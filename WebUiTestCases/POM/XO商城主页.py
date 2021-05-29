#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser

class HomePage(Browser):
    注册 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/a[2]')
    登录 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/a[1]')
