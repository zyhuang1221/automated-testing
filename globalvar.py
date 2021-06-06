#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 
# @Author  : Mik

def _init():
    """全局变量初始化"""
    global _global_dict
    _global_dict = {}


def set_val(name, val):
    """设置全局变量"""
    _global_dict[name] = val


def get_val(name):
    """获取全局变量"""
    try:
        return _global_dict[name]
    except KeyError:
        return None
