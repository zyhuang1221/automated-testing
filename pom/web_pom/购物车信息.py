#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class GWCXX(Browser):
    结算 = (By.CLASS_NAME, 'shopCar_btn_03')

    def js(self):
        self.my_click(GWCXX.结算)
