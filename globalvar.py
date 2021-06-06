#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 
# @Author  : Mik

def _init():
    global _global_dict
    _global_dict = {}

def set_val(name,val):
    _global_dict[name] = val

def get_val(name):
    try:
        return _global_dict[name]
    except KeyError:
        return None

