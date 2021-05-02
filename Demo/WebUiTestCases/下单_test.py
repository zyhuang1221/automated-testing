#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik
import pytest
from selenium import webdriver

from WebUiTestCases.POM import 主页, 用户登录, 我的会员中心, 商城, 搜索商品结果, 加入购物车, \
    商品添加成功, 购物车信息, 核对订单信息

# driver = webdriver.Chrome()
# driver.get('http://127.0.0.1')

info = ('mik2', 'password',)
gereninfo = ('mik2', '15823234567', '湖北省', '武汉市', '江夏区', '湖北省武汉市', '123456')


class Testdl():
    def testcase1(self, browser):
        page = 主页.HomePage(browser)
        allhd = page.get_all_handles()
        page.denglu()
        page.switch_window(name='new', all_handles=allhd)
        page = 用户登录.Login(browser)
        page.denglu(info)
        page = 我的会员中心.GerenZhongxin(browser)
        page.my_click(我的会员中心.GerenZhongxin.进入商城购物)
        page = 商城.GouWu(browser)
        page.search('iphone')
        page = 搜索商品结果.ShangPing(browser)
        allhd = page.get_all_handles()
        page.my_click(搜索商品结果.ShangPing.商品)
        page.switch_window(name='new', all_handles=allhd)
        page = 加入购物车.Addshangping(browser)
        page.addsp()
        page = 商品添加成功.TJchenggong(browser)
        page.jiesuan()
        page = 购物车信息.GWCXX(browser)
        page.js()
        page = 核对订单信息.HeDui(browser)
        page.addnewdizhi(gereninfo)


if __name__ == '__main__':
    pytest.main(['./下单_test.py'])
