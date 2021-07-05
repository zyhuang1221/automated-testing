#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
from appium.webdriver.common.mobileby import MobileBy as By
from libs.common.appbase import BasePage


class Search(BasePage):
    loc_输入框 = (By.ID, 'com.netease.cloudmusic:id/search_src_text')
    loc_歌曲 = (By.ID, 'com.netease.cloudmusic:id/zp')
