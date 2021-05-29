#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 
# @Author  : Mik
import pytest
from selenium import webdriver
from libs.utils.log_module import log
from WebUiTestCases.POM import 主页, 用户登录, 我的会员中心, 商城, 搜索商品结果, 加入购物车, \
    商品添加成功, 购物车信息, 核对订单信息
from time import sleep
# driver = webdriver.Chrome()
# driver.get('http://127.0.0.1')

info = ('mik2', 'password',)
userinfo = ('mik2', '15823234567', '湖北省', '武汉市', '江夏区', '湖北省武汉市', '123456')


class Testdl():
    def setup_class(self):
        log.info('开始执行Testdl测试')

    def teardown_class(self):
        log.info('Testdl测试完成')

    def testcase1(self, browser,base_url):

        主页_page = 主页.HomePage(browser)
        主页_page.get_url(base_url)
        allhd = 主页_page.get_all_handles()
        主页_page.denglu()
        主页_page.switch_window(name='new', all_handles=allhd)
        用户登录_page = 用户登录.Login(browser)
        用户登录_page.denglu(info)
        我的会员中心_page = 我的会员中心.GerenZhongxin(browser)
        我的会员中心_page.my_click(我的会员中心.GerenZhongxin.进入商城购物)
        商城_page = 商城.GouWu(browser)
        商城_page.search('iphone')
        搜索商品结果_page = 搜索商品结果.ShangPing(browser)
        allhd = 搜索商品结果_page.get_all_handles()
        搜索商品结果_page.my_click(搜索商品结果.ShangPing.商品)
        搜索商品结果_page.switch_window(name='new', all_handles=allhd)
        加入购物车_page = 加入购物车.Addshangping(browser)
        加入购物车_page.addsp()
        商品添加成功_page = 商品添加成功.TJchenggong(browser)
        商品添加成功_page.jiesuan()
        购物车信息_page = 购物车信息.GWCXX(browser)
        购物车信息_page.js()
        核对订单信息_page = 核对订单信息.HeDui(browser)
        核对订单信息_page.addnewdizhi(userinfo)


if __name__ == '__main__':
    pytest.main(['./.py'])
