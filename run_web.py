#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik

# from libs.utils.log_module import logger
from libs.utils.base_path import root_dir
from libs.utils import rw_properties
from libs.utils.clear_file import clearFile, clearLog
from shutil import copyfile
import globalvar as gl
import platform
import pytest
import os


def mainSetup():
    """测试前置"""
    # 设置全局变量
    gl._init()
    gl.set_val('name', 'web')
    # 清空一天前的log
    logdir = root_dir + r'\log'
    clearLog(logdir)
    # 获取系统信息并写入environment.properties
    file = root_dir + r'\report\environment.properties'
    sys_info = platform.uname().system
    rw = rw_properties.parse(file)
    rw.put('OS', sys_info)
    # 清空imgs和log目录
    imgdir = root_dir + r'\imgs'
    clearFile(imgdir)


def mainTearDown():
    """测试后置"""
    # 复制环境变量文件到xml
    source = root_dir + r'\report\environment.properties'
    target = root_dir + r'\report\xml\environment.properties'
    copyfile(source, target)
    # 生成allure报告
    os.system('allure generate --clean ./report/xml -o ./report/html')  # --clean 清空上次报告


if __name__ == '__main__':
    mainSetup()
    from libs.utils.log_module import logger
    logger.info('开始执行web自动化测试')
    pytest.main()
    logger.info('web自动化测试结束')
    mainTearDown()
