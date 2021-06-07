#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 
# @Author  : Mik

import yaml
import os
from libs.utils.base_path import root_dir

def read_yaml():
    """读取yaml文件并return文件"""
    file_dir = root_dir+'/config/cfg.yaml'.replace(r'\/'.replace(os.sep, ''), os.sep)
#    path_file = file_dir.replace('libs', 'config').replace('utils','cfg.yaml')
    with open(file_dir, mode='r', encoding='utf-8') as file:
        msg = yaml.load(file, Loader=yaml.FullLoader)
    return msg
