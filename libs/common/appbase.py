#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 
# @Author  : Mik
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libs.utils.log_module import logger
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


class BasePage:
    def __init__(self, driver, pagename=''):
        self.driver = driver
        self.page = pagename

    def my_find_element(self, loc, msg=''):
        """自动显示等待10s,定位元素，并返回元素。没有定位到抛出异常
        :param loc:元素定位表达式，元组类型。
        :param msg:元素描述，用于记录到日志
        :return element
        """
        if not isinstance(loc, tuple):
            raise TypeError('loc参数类型错误，必须是元组；loc = ("id", "value1")')
        else:
            try:
                logger.info('定位{}页面元素：{}, 元素描述：{}'.format(self.page, loc, msg))
                ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            except Exception as e:
                logger.error('元素定位失败!')
                raise e
            else:
                logger.info('元素定位成功')
                return ele

    def my_find_elements(self, loc, msg=''):
        """
        定位元素组
        :param loc:元素定位表达式，元组类型。
        :param msg:元素描述，用于记录到日志
        :return: 元素组
        """
        if not isinstance(loc, tuple):
            raise TypeError('loc参数类型错误，必须是元组；loc = ("id", "value1")')
        else:
            try:
                logger.info('定位{}页面元素：{}, 元素描述：{}'.format(self.page, loc, msg))
                eles = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(loc))
            except Exception as e:
                logger.error('元素定位失败!')
                raise e
            else:
                logger.info('元素定位成功')
                return eles

    def swipe_to_up(self):
        """向上滑动屏幕"""
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        logger.info('向上滑动屏幕')
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        """向下滑动屏幕"""
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        logger.info('向下滑动屏幕')
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        """向左滑动屏幕"""
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        logger.info('向左滑动屏幕')
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        """向右滑动屏幕"""
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        logger.info('向右滑动屏幕')
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def pinch(self):
        """
        屏幕内容缩小
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        action1 = TouchAction(self.driver)  # 第一个手势
        action2 = TouchAction(self.driver)  # 第二个手势
        pinch_action = MultiAction(self.driver)  # 缩小手势
        action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
        action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()
        pinch_action.add(action1, action2)  # 加载
        logger.info('开始执行缩小')
        pinch_action.perform()  # 执行

    def zoom(self):
        """
        屏幕内容放大
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        action1 = TouchAction(self.driver)  # 第一个手势
        action2 = TouchAction(self.driver)  # 第二个手势
        zoom_action = MultiAction(self.driver)  # 放大手势
        action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
        action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()
        zoom_action.add(action1, action2)  # 加载
        logger.info('开始执行放大')
        zoom_action.perform()  # 执行










