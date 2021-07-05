#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
from time import sleep

import pytest
from pom.app_pom import 网易云主页, 搜索页


class TestLogin:

    def test01(self, driver):
        page_主页 = 网易云主页.HomePage(driver)
        page_主页.my_find_element(page_主页.loc_搜索按钮).click()
        page_搜索 = 搜索页.Search(driver)
        page_搜索.my_find_element(page_搜索.loc_输入框).send_keys('我们')
        page_搜索.driver.keyevent(66)
        page_搜索.my_find_element(page_搜索.loc_歌曲).click()


if __name__ == '__main__':
    pytest.main(["-s", "-vv", "test_02_searchMusic.py"])
