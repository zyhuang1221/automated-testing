#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

from selenium.webdriver.common.by import By
from libs.common.browser_init import Browser
from selenium.webdriver.support.select import Select


class HeDui(Browser):
    添加新地址 = (By.CLASS_NAME, 'add-address')
    收货人 = (By.NAME, 'address[address_name]')
    手机号 = (By.NAME, 'address[mobile]')
    选择省 = (By.ID, 'add-new-area-select')
    选择市 = (By.CLASS_NAME, 'add-new-area-select')
    选择区 = (By.TAG_NAME, 'select')
    详细地址 = (By.NAME, 'address[address]')
    邮政编码 = (By.NAME, 'address[zipcode]')
    确定 = (By.CLASS_NAME, 'aui_state_highlight')

    def addnewdizhi(self, value):
        self.my_click(HeDui.添加新地址)
        self.my_send_key(HeDui.收货人, value[0])
        self.my_send_key(HeDui.手机号, value[1])
        ele = self.wait_element_visible(HeDui.选择省)
        Select(ele).select_by_visible_text(value[2])
        shi = self.find_elements(HeDui.选择市)[1]
        Select(shi).select_by_visible_text(value[3])
        qu = self.find_elements(HeDui.选择区)[2]
        Select(qu).select_by_visible_text(value[4])
        self.my_send_key(HeDui.详细地址, value[5])
        self.my_send_key(HeDui.邮政编码, value[6])
        self.my_click(HeDui.确定)
