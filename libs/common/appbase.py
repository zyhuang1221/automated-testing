#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 
# @Author  : Mik
from appium import webdriver
from time import sleep

caps = {
    'deviceName': '160fdb4c',
    'automationName': 'UiAutomator2',
    'platformName': 'android',
    'platformVersion': '7.0',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
driver.find_element_by_id('com.android.calculator2:id/op_add').click()
driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
driver.find_element_by_id('com.android.calculator2:id/eq').click()
sleep(5)
driver.quit()
