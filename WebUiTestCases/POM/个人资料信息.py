#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class GeRen(Browser):
    个人资料 = (By.LINK_TEXT, '个人资料')
    修改姓名 = (By.ID, 'true_name')
    修改性别 = (By.CSS_SELECTOR, '[value="1"]')
    修改生日 = (By.ID,'date')
    修改QQ = (By.ID, 'qq')
    确认 = (By.CSS_SELECTOR,'[value="确认"]')

