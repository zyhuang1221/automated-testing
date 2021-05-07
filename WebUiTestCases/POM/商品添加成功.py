#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class TJchenggong(Browser):
    购物车结算 = (By.CLASS_NAME, 'shopCar_T_span3')

    def jiesuan(self):
        self.my_click(TJchenggong.购物车结算)
