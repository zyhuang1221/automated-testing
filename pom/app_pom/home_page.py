#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
from appium.webdriver.common.mobileby import MobileBy as By
from libs.common.appbase import BasePage


class Test(BasePage):
    loc_新建 = (By.ID, 'com.youdao.note:id/add_note')
    loc_新建笔记 = (By.ID, 'com.youdao.note:id/add_note_floater_add_note')
    loc_标题 = (By.ID, 'com.youdao.note:id/note_title')
    loc_正文 = (By.ACCESSIBILITY_ID, 'Android BulbEditor')

    def test(self):
        self.my_find_element(self.loc_新建).click()
        self.my_find_element(self.loc_新建笔记).click()
        self.my_find_element(self.loc_正文).send_keys('哈哈哈哈')
        self.my_find_element(self.loc_标题).send_keys('test1')




