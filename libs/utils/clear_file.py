#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 
# @Author  : Mik

import os


def clearFile(dir_path):
    """
    清除目录下的文件
    :param dir_path: 路径
    :return: None
    """
    ls = os.listdir(dir_path)
    for i in ls:
        c_path = os.path.join(dir_path, i)
        if os.path.isdir(c_path):
            dir_path(c_path)
        else:
            os.remove(c_path)
