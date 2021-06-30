#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 
# @Author  : Mik
from appium import webdriver
from time import sleep

caps = {
    'deviceName': '127.0.0.1:62001',
    'platformName': 'android',
    'platformVersion': '5.1.1',
    'appPackage': 'com.wuba',
    'appActivity': '.activity.city.CityHotActivity t3'
}

driver = webdriver.Remote('http://192.168.1.5:4723/wd/hub', caps)


sleep(5)