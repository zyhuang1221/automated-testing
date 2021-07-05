#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
import pytest
from appium import webdriver
from libs.utils.read_ini import load_ini

_driver = None


@pytest.fixture(scope='session', autouse=True)
def driver():
    global _driver
    _driver = webdriver.Remote('http://192.168.1.5:4723/wd/hub', load_ini('desired'))
    return _driver
