#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 
# @Author  : Mik
from selenium.webdriver.common.by import By
from libs.common.base import BasePage


class LoginSucceed(BasePage):
    loc_欢迎 = (By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/em[2]')
    loc_退出登录 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[1]/a[2]')
    loc_个人中心 = (By.XPATH, '/html/body/div[2]/div/ul[2]/div[1]/div/a/span')
    loc_搜索框 = (By.ID, "search-input")
    loc_搜索按钮 = (By.ID, "ai-topsearch")

    def exit(self):
        self.my_click(self.loc_退出登录, msg='退出登录')

    def goto_gerenzhongxin(self):
        self.my_click(self.loc_个人中心, msg='个人中心')
