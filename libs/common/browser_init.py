#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC
from libs.utils.base_path import root_dir
from libs.utils.log_module import logger
from selenium.webdriver import Remote
from selenium import webdriver
from libs.utils import rd_yaml
from time import sleep
import allure
import time


def browser_init():
    web_cfg_data = rd_yaml.read_yaml()['browser']
    if web_cfg_data['type'] == 'chrome':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Chrome()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "chrome",
                            })
        else:
            raise ValueError('env类型定义错误！')

    elif web_cfg_data['type'] == 'firefox':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Firefox()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "firefox",
                            })
        else:
            raise ValueError('env类型定义错误！')
    elif web_cfg_data['type'] == 'ie':
        if web_cfg_data['env'] == 'localhost':
            driver = webdriver.Ie()
        elif web_cfg_data['env'] == 'grid':
            driver = Remote(command_executor=web_cfg_data['gridUrl'],
                            desired_capabilities={
                                "browserName": "internet explorer",
                            })
        else:
            raise ValueError('env类型定义错误！')
    else:
        raise ValueError('driver驱动类型定义错误！')
    logger.info(f'在{web_cfg_data["env"]}使用{web_cfg_data["type"]}执行')
    driver.maximize_window()
    return driver


class BasePage:
    """封装浏览器操作"""

    def __init__(self, driver):
        """
        :param driver: 浏览器对象
        :param page: 页面功能名，用于失败截图命名
        """
        self.driver = driver

    def my_get_url(self, url):
        """
        发送url请求
        :param url: 传入url
        :return: None
        """
        try:
            self.driver.implicitly_wait(5)
            self.driver.get(url)
        except:
            raise

    def wait_element_visible(self, loc, t=10):
        """每次操作之前自动显示等待,找到元素，并返回元素对象
        :param loc:元素定位表达式，元组类型。（元素定位类型，元素定位方法）
        :param t:等待超时时间上限，数字类型
        :return element
        """
        logger.info('开始等待页面元素<{}>是否可见！'.format(loc))
        try:
            start_time = time.time()
            ele = WebDriverWait(self.driver, t).until(EC.visibility_of_element_located(loc))
            end_time = time.time()
        except Exception as e:
            logger.error('等待页面元素<{}>{}秒失败！'.format(loc, t))
            self.my_save_webImgs()
            raise e
        else:
            logger.info('页面元素<{}>可见，等待时间：{}秒!'.format(loc, round(end_time - start_time, 3)))
            return ele

    def my_import_text(self, loc, value):
        """
        输入操作，传入元素定位表达式，元组类型。和输入内容
        :param loc:
        :param value: 输入内容
        :return:
        """
        ele = self.wait_element_visible(loc)
        logger.info('在<{}>输入<{}>'.format(loc, value))
        try:
            ele.clear()
            ele.send_keys(value)
        except Exception as e:
            logger.error('输入操作失败')
            self.my_save_webImgs()
            raise e

    def my_click(self, loc):
        """
        点击操作，传入元素定位表达式，元组类型
        :param loc:
        :return: None
        """
        ele = self.wait_element_visible(loc)
        logger.info('点击<{0}>'.format(loc))
        try:
            ele.click()
        except Exception as e:
            logger.error(f'元素：<{loc}>点击失败')
            self.my_save_webImgs()
            raise e

    def my_submit(self, loc):
        """
        提交form表单操作，传入元素定位表达式，元组类型。元素定位在form表单中任意元素即可
        记住只能在form表单中使用，一般在submit难定位时使用
        :param loc:
        :return:
        """
        ele = self.wait_element_visible(loc)
        logger.info('点击<{0}>提交'.format(loc))
        try:
            ele.submit()
        except Exception as e:
            logger.error('点击提交<loc>失败'.format(loc))
            self.my_save_webImgs()
            raise e

    def my_find_elements(self, loc):
        """
        获取元素组
        :param loc: 元素定位
        :return: 元素组
        """
        logger.info('开始寻找页面元素<{}>'.format(loc))
        try:
            eles = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
        except Exception as e:
            logger.error('寻找页面元素失败<{}>'.format(loc))
            self.my_save_webImgs()
            raise e
        else:
            return eles

    def my_get_current_handles(self):
        """
        获取当前所有句柄
        :return:
        """
        logger.info('获取当前句柄')
        try:
            all_handles = self.driver.window_handles
        except Exception as e:
            logger.error('获取当前失败')
            self.my_save_webImgs()
            raise e
        else:
            return all_handles

    def my_switch_window(self, name, old_handles, timeout=10):
        """
        窗口切换==如果是切换到新窗口，new，如果是回到默认窗口，default。切换前，在新窗口打开前获取handles
        :param name: new代表最新打开的一个窗口。default代表第一个窗口。其他的值表示为窗口的handles name
        :param old_handles:传入的句柄为打开新窗口之前的所有句柄
        :param timeout:
        :return:
        """

        try:
            if name == "new" and old_handles is not None:
                logger.info("切换到最新打开的窗口")
                WebDriverWait(self.driver, timeout, ).until(EC.new_window_is_opened(old_handles))
                window_handles = self.driver.window_handles  # 获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif name == "default":
                logger.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
                # self.driver.switch_to_default_content()
            else:
                logger.info("切换到指定handles")
                self.driver.switch_to.window(name)
        except Exception as e:
            logger.error("切换失败")
            self.my_save_webImgs()
            raise e

    def my_get_text(self, loc):
        """
        获取文本内容
        :param loc: 元素定位
        :return: 文本内容
        """
        ele = self.wait_element_visible(loc)
        logger.info('获取元素<{}>的内容'.format(loc))
        try:
            text = ele.text
            logger.info('元素<{}>的内容为<{}>'.format(loc, text))
        except Exception as e:
            logger.error("获取内容失败")
            self.my_save_webImgs()
            raise e
        else:
            return text

    def my_switch_alert(self):
        """
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :return: None
        """
        try:
            # result = EC.alert_is_present()(self.driver)
            WebDriverWait(self.driver, timeout=10).until(EC.alert_is_present())
            result = self.driver.switch_to.alert
            if result:
                msg = result.text
                logger.info("alert出现，内容为：{0}".format(msg))
                result.accept()
                logger.info("alert已经关闭")
                return msg
            else:
                logger.info("未弹出alert")

        except:
            logger.error("alert切换失败！")
            self.my_save_webImgs()
            raise

    def my_save_webImgs(self):
        """
        失败截图
        :return: None
        """
        # filepath=制定的图片保存目录/(页面功能名称)_当前时间到秒.png
        name1 = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filepath = root_dir + r'\imgs\{}.png'.format(name1)
        try:
            self.driver.save_screenshot(filepath)
            logger.info("截屏成功,图片路径为{}".format(filepath))
            sleep(1)
            allure.attach.file(filepath, name1, allure.attachment_type.PNG)
        except:
            logger.error("截屏失败")

    def my_switch_iframe(self, loc):
        """
        等待iframe存在
        :param loc: 元素定位
        :return:
        """
        logger.info("iframe切换操作：")
        try:
            WebDriverWait(self.driver, timeout=10).until(
                EC.frame_to_be_available_and_switch_to_it(loc))
            time.sleep(0.5)
            logger.info("切换成功")
        except:
            logger.error("iframe切换失败！")
            self.my_save_webImgs()
            raise

    def my_window_cloce(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()

    def my_double_click(self, loc):
        """
        鼠标双击
        :param loc: 元素定位，元组类型
        :return:
        """
        ele = self.wait_element_visible(loc)
        try:
            AC(self.driver).double_click(ele).perform()
            logger.info("{0}:元素：鼠标双击成功".format(loc))
        except:
            logger.error("鼠标双击操作失败。")
            self.my_save_webImgs()
            raise
