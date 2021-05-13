#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 
# @Author  : Mik
import os

# base_path=os.path.abspath(os.path.dirname(__file__))
base_path_temp = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
base_path = base_path_temp.replace(r'\/'.replace(os.sep, ''), os.sep)
# print(base_path)
