#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 
# @Author  : Mik
from pom.web_pom import XO商城登录成功, XO商城主页, 商品显示页面, 商品详情页面, 新增地址页面
from libs.utils.log import logger
from libs.utils.rd_yaml import load
import pytest
import allure
from time import sleep

uinfo = ['ak67', 'mik123', '18923234567', '湖北省', '武汉市', '江夏区', '湖北省']


@allure.epic('WebUI测试')
@allure.severity('blocker')
@allure.feature('购物模块')
class TestShop:
    @allure.story('用户购物')
    def test_case01(self, browser):
        with allure.step('打开主页，点击登录'):
            page_主页 = XO商城主页.HomePage(browser, '商城主页')
            page_主页.open_home()
            page_登录 = page_主页.goto_login()
        with allure.step('输入用户名登录'):
            page_登录.login('mik_2', '123456')
        with allure.step('搜索手机'):
            page_登录成功 = XO商城登录成功.LoginSucceed(browser, '登录成功主页')
            page_登录成功.my_sendkeys(page_登录成功.loc_搜索框, '手机', '搜索框')
            page_登录成功.my_click(page_登录成功.loc_搜索按钮, '搜索按钮')
            page_商品显示 = 商品显示页面.AfterSearch(browser, '显示商品页面')
            all_hd = page_商品显示.my_get_handles()
            page_商品显示.my_click(page_商品显示.loc_商品, '第一个商品')
        with allure.step('选择手机类型'):
            page_商品显示.my_switch_window(old_handles=all_hd)
            page_商品详情 = 商品详情页面.GoodsDetails(browser, '商城主页')
            page_确认订单 = page_商品详情.select_goods()
        with allure.step('确认订单'):
            page_确认订单.my_click(page_确认订单.loc_使用新地址, '使用新地址')
            sleep(1)
            page_确认订单.my_switch_iframe(page_确认订单.loc_iframe)
            page_新增地址 = 新增地址页面.NewAddress(browser, '新增地址')
            page_新增地址.add_addres(uinfo)

            text = page_新增地址.my_get_text(page_新增地址.loc_新增地址弹窗结果, '新增地址弹窗结果')
            try:
                assert text == '新增成功'
            except:
                raise
