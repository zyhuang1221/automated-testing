#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.base import BasePage


class MakeSure(BasePage):
    loc_使用新地址 = (By.XPATH, '//button[text()="使用新地址"]')
    loc_iframe = (By.XPATH, '//div[@id="popup-modal-address"]/div/iframe')

