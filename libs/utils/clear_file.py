#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 
# @Author  : Mik

import os
import time
from libs.utils.base_path import root_dir


def clearFile(dir_path):
    """
    清除目录以及子目录下的文件
    :param dir_path: 路径
    :return: None
    """
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        # 获取目录下文件和文件夹列表
        ls = os.listdir(dir_path)
        # 删除目录下的所有文件及子目录下的所有文件
        for i in ls:
            c_path = os.path.join(dir_path, i)
            if os.path.isdir(c_path):
                clearFile(c_path)
            else:
                os.remove(c_path)

    else:
        raise NameError('路径不存在或者不是一个目录')


def clearLog(dir_path):
    now_time = time.time()
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        ls = os.listdir(dir_path)
        for i in ls:
            c_path = os.path.join(dir_path, i)
            print(c_path)
            if os.path.isdir(c_path):
                clearLog(c_path)
            else:
                cre_time = os.path.getmtime(c_path)
                if cre_time < (now_time - 86400):
                    os.remove(c_path)
    else:
        raise NameError('路径不存在或者不是一个目录')


# clearLog(root_dir+r'\log')