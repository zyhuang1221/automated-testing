#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik
import os
import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate --clean ./report/xml -o ./report/html')

