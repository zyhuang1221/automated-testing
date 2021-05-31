#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Remote
from libs.utils import rd_yaml
from libs.utils.log_module import log
import time
from libs.utils.base_path import base_path

web_cfg_data = rd_yaml.read_yaml()['browser']


def browser_init():
    if web_cfg_data['type'] == 'chrome':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Chrome()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "chrome",
                            })
        else:
            raise NameError('env类型定义错误！')

    elif web_cfg_data['type'] == 'firefox':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Firefox()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "firefox",
                            })
        else:
            raise NameError('env类型定义错误！')
    elif web_cfg_data['type'] == 'ie':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Ie()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "internet explorer",
                            })
        else:
            raise NameError('env类型定义错误！')
    else:
        raise NameError('driver驱动类型定义错误！')
    # driver.get(web_cfg_data['url'])
    # driver.implicitly_wait(10)
    log.info(f'在{web_cfg_data["env"]}使用{web_cfg_data["type"]}执行')
    driver.maximize_window()
    return driver


class Browser():
    """封装浏览器操作，传入实例化driver"""

    def __init__(self, driver):
        self.driver = driver


    def get_url(self,url):
        """
        发送url请求
        :param url: 传入url
        :return: None
        """
        self.driver.implicitly_wait(10)
        self.driver.get(url)


    def wait_element_visible(self, loc, t=10):
        """每次操作之前自动显示等待,找到元素，并返回元素对象
        :param loc:元素定位表达式，元组类型。（元素定位类型，元素定位方法）
        :param t:等待超时时间上限，数字类型
        :return element
        """

        log.info('开始等待页面元素<{}>是否可见！'.format(loc))
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, t).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log.error('等待页面元素<{}>{}秒失败！'.format(loc, t))
            # self.driver.save_screenshot(base_path+r'\img_1\test.png')
            # raise e
        else:
            end_time = time.time()
            log.info('页面元素<{}>可见，等待时间：{}秒!'.format(loc, round(end_time - start_time, 3)))
            return ele

    def my_import_text(self, loc, value):
        """
        输入操作，传入元素定位表达式，元组类型。和输入内容
        :param loc:
        :param value: 输入内容
        :return:
        """
        self.wait_element_visible(loc).send_keys(value)
        log.info('在<{}>输入<{}>'.format(loc, value))

    def my_click(self, loc):
        """
        点击操作，传入元素定位表达式，元组类型
        :param loc:
        :return: None
        """
        self.wait_element_visible(loc).click()
        log.info('点击<{0}>'.format(loc))

    def my_submit(self, loc):
        """
        提交操作，传入元素定位表达式，元组类型
        :param loc:
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            ele.submit()
        except Exception as e:
            log.error('未能提交<>'.format(loc))
        else:
            log.info("在<{}>点击提交".format(loc))

    def find_elements(self, loc):
        """
        获取元素出现的次数
        :param loc: 元素定位
        :return: 元素组
        """
        try:
            eles = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
        except Exception as e:
            raise e
        else:
            return eles

    def get_all_handles(self):
        """
        获取当前所有句柄
        :return:
        """
        all_handles = self.driver.window_handles
        return all_handles

    # 窗口切换==如果是切换到新窗口，new，如果是回到默认窗口，default。切换前，在新窗口打开前获取handles
    def switch_window(self, name, all_handles=None, timeout=10, model=None):
        '''
        :param name: new代表最新打开的一个窗口。default代表第一个窗口。其他的值表示为窗口的handles
        :param current_handles:传入的句柄为打开新窗口之前的句柄
        :param timeout:
        :param poll_frequency:
        :param model:
        :return:
        '''

        try:
            if name == "new" and all_handles is not None:
                log.info("切换到最新打开的窗口")
                WebDriverWait(self.driver, timeout, ).until(EC.new_window_is_opened(all_handles))
                window_handles = self.driver.window_handles  # 获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif name == "default":
                log.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
                # self.driver.switch_to_default_content()
            else:
                log.info("切换到指定handles")
                self.driver.switch_to.window(name)
        except:
            log.error("切换失败")
            raise

    def my_get_text(self,loc):
        """
        获取文本内容
        :param loc: 元素定位
        :return: 文本内容
        """
        text=self.wait_element_visible(loc).text
        log.info('元素<{}>的内容为<{}>'.format(loc,text))
        return text

