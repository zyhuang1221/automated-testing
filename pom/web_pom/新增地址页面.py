#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.base import BasePage
from time import sleep

class NewAddress(BasePage):
    loc_别名 = (By.XPATH, '//input[@placeholder="别名"]')
    loc_姓名 = (By.XPATH, '//input[@placeholder="姓名"]')
    loc_电话 = (By.XPATH, '//input[@placeholder="电话"]')
    loc_省下拉框 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[1]/a/div')
    loc_市下拉框 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[2]/a')
    loc_区下拉框 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[3]/a')
    loc_详细地址 = (By.XPATH, '//input[@placeholder="详细地址"]')
    loc_保存按钮 = (By.XPATH, '//button[text()="保存"]')

    def add_addres(self, userinfo):
        self.my_sendkeys(self.loc_别名, userinfo[0], '别名')
        self.my_sendkeys(self.loc_姓名, userinfo[1], '姓名')
        self.my_sendkeys(self.loc_电话, userinfo[2], '电话')
        self.my_click(self.loc_省下拉框, '省下拉框')
        loc_选择省 = (By.XPATH, f'/html/body/div[1]/form/div[4]/div[1]/div/ul/li[text()="{userinfo[3]}"]')
        self.my_click(loc_选择省, '选择省')
        self.my_click(self.loc_市下拉框, '市下拉框')
        loc_选择市 = (By.XPATH, f'/html/body/div[1]/form/div[4]/div[2]/div/ul/li[text()="{userinfo[4]}"]')
        self.my_click(loc_选择市, '选择市')
        self.my_click(self.loc_区下拉框, '区下拉框')
        loc_选择区 = (By.XPATH, f'/html/body/div[1]/form/div[4]/div[3]/div/ul/li[text()="{userinfo[5]}"]')
        self.my_click(loc_选择区, '选择区')
        self.my_sendkeys(self.loc_详细地址, userinfo[6], '详细地址')
        self.my_click(self.loc_保存按钮, '保存按钮')
