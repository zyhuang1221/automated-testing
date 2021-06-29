#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 
# @Author  : Mik
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()  # 打开浏览器
driver.get('http://www.baidu.com')  # 打开百度
driver.find_element(By.ID, 'kw').send_keys('python')  # 输入python
driver.find_element(By.ID, 'su').click()  # 点击搜索
sleep(1)  # 等待打开页面
driver.find_element(By.XPATH, '//div[@id=2]/h3/a').click()  # 找到百科点击
# handles = driver.window_handles  # 获取全部句柄
# driver.switch_to.window(handles[-1])  # 切换到新打开
# driver.find_elements(By.LINK_TEXT, '面向对象')[0].click()  # 点击面向对象
