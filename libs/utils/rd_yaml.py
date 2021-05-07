#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 
# @Author  : Mik

import yaml
import os
from libs.utils.base_path import base_path

def read_yaml():
    """读取yaml文件并return文件"""
    file_dir = base_path+'/config/cfg.yaml'.replace(r'\/'.replace(os.sep, ''), os.sep)
    # file_dir = os.path.dirname(__file__).replace(r'\/'.replace(os.sep, ''), os.sep) #获取当前文件路径并转换成当前目录格式
#    path_file = file_dir.replace(r'libs\utils', r'config\cfg.yaml')
    path_file = file_dir.replace('libs', 'config').replace('utils','cfg.yaml')
    with open(path_file, mode='r', encoding='utf-8') as file:
        msg = yaml.load(file, Loader=yaml.FullLoader)
        # sender = tuple(msg['mail']['sender'])
        # receiver = msg['mail']['receiver']
    return msg
