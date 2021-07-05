#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
from appium.webdriver.common.mobileby import MobileBy as By
from libs.common.appbase import BasePage


class HomePage(BasePage):
    loc_搜索按钮 = (By.ACCESSIBILITY_ID, '搜索')


