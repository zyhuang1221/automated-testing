#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.base import BasePage
from pom.web_pom.订单确认页面 import MakeSure
from time import sleep


class GoodsDetails(BasePage):
    loc_套餐1 = (By.XPATH, '//li[@data-value="套餐一"]')
    loc_金色 = (By.XPATH, '//li[@data-value="金色"]')
    loc_32G = (By.XPATH, '//li[@data-value="32G"]')
    loc_立即购买 = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/div[3]/div[2]/button[1]')
    loc_加入购物车 = (By.XPATH, '//button[@title="加入购物车"]')
    loc_加入购物车弹出框 = (By.XPATH, '//p[@class="prompt-msg"]')

    def select_goods(self):
        self.my_click(self.loc_套餐1, '套餐1')
        sleep(0.5)
        self.my_click(self.loc_金色, '金色')
        sleep(0.5)
        self.my_click(self.loc_32G, '32G')
        sleep(0.5)
        self.my_click(self.loc_立即购买, '立即购买')
        return MakeSure(self.driver,'订单确认')
