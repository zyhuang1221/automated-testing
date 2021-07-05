#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
from time import sleep

import pytest
from pom.app_pom.登录页 import Login


class TestLogin:

    def test01(self, driver):
        pass
        # page_登录 = Login(driver)
        # page_登录.login('17364016259', 'A123b567')
        # sleep(10)


if __name__ == '__main__':
    pytest.main(["-s", "-vv", "test_01_login.py"])
