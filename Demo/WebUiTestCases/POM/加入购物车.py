#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class Addshangping(Browser):
    添加购物车 = (By.ID, 'joinCarButton')


    def addsp(self):
        self.my_click(Addshangping.添加购物车)