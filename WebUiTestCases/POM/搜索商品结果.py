#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser

class ShangPing(Browser):
    商品 = (By.XPATH,'/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img')

