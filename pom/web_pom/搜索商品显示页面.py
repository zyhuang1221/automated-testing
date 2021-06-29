#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.base import BasePage


class AfterSearch(BasePage):
    loc_商品 = (By.XPATH, "/html/body/div[4]/div/ul/li[1]/div")


