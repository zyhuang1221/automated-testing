#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser


class GouWu(Browser):
    输入框 = (By.NAME, 'keyword')
    搜索 = (By.CLASS_NAME, 'btn1')

    def search(self, value):
        self.my_send_key(GouWu.输入框, value)
        self.my_click(GouWu.搜索)
