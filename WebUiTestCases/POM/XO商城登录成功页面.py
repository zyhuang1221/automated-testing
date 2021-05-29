#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class DLCG(Browser):
    欢迎 = (By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/em[2]')
