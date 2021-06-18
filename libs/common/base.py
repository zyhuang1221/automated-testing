#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC
from libs.utils.base_path import root_dir
from libs.utils.log_module import logger
from time import sleep
import allure
import time


class BasePage:
    """基于原生selenium第二次封装，主要添加显示等待和log以及失败截图"""

    def __init__(self, driver, page=''):
        """
        :param driver: 浏览器对象
        :param page: 页面功能名，用于记录log和失败截图
        """
        self.driver = driver
        self.page = page

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

    def wait_element_visible(self, loc, msg=''):
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
                start_time = time.time()
                ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
                end_time = time.time()
            except Exception as e:
                logger.error('元素定位失败!')
                self.my_save_webImgs()
                raise e
            else:
                logger.info('元素定位成功：耗时{}秒!'.format(round(end_time - start_time, 3)))
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
                start_time = time.time()
                eles = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
                end_time = time.time()
            except Exception as e:
                logger.error('元素定位失败!')
                self.my_save_webImgs()
                raise e
            else:
                logger.info('元素定位成功：耗时{}秒!'.format(round(end_time - start_time, 3)))
                return eles

    def my_sendkeys(self, loc, text='', msg=''):
        """
        输入操作
        :param loc:元素定位表达式
        :param text: 输入内容
        :param msg:元素描述
        :return:
        """
        ele = self.wait_element_visible(loc, msg=msg)
        try:
            logger.info('输入内容：{}'.format(text))
            ele.clear()
            ele.send_keys(text)
        except Exception as e:
            logger.error('输入失败')
            self.my_save_webImgs()
            raise e

    def my_click(self, loc, msg=''):
        """
        点击操作
        :param loc:元素定位表达式
        :param msg:元素描述
        :return: None
        """
        ele = self.wait_element_visible(loc, msg=msg)
        try:
            logger.info('点击元素：{}'.format(msg))
            ele.click()
        except Exception as e:
            logger.error('点击失败！')
            self.my_save_webImgs()
            raise e

    def my_submit(self, loc):
        """
        提交form表单操作，元素定位在form表单中任意元素即可
        记住只能在form表单中使用，一般在submit难定位时使用
        :param loc:元素定位表达式
        :return:
        """
        ele = self.wait_element_visible(loc, msg='提交')
        try:
            logger.info('点击提交')
            ele.submit()
        except Exception as e:
            logger.error('点击失败'.format())
            self.my_save_webImgs()
            raise e

    def my_get_current_handles(self):
        """
        获取当前所有句柄
        :return:所有句柄
        """
        logger.info('获取所有句柄')
        try:
            all_handles = self.driver.window_handles
        except Exception as e:
            logger.error('获取句柄失败')
            self.my_save_webImgs()
            raise e
        else:
            return all_handles

    def my_switch_window(self, handle='new', old_handles=None):
        """
        窗口切换==如果是切换到新窗口，new，如果是回到默认窗口，default。切换前，在新窗口打开前获取handles
        :param handle: (new, default,handle name )
        :param old_handles:切换新打开窗口时传入，传入的句柄为打开新窗口之前的所有句柄
        :return:
        """
        try:
            if handle == "new" and old_handles is not None:
                logger.info("切换到最新打开的窗口")
                WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(old_handles))
                window_handles = self.driver.window_handles  # 获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif handle == "default":
                logger.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
                # self.driver.switch_to_default_content()
            else:
                logger.info("切换到指定handles")
                self.driver.switch_to.window(handle)
        except Exception as e:
            logger.error("切换失败")
            self.my_save_webImgs()
            raise e

    def my_get_text(self, loc, msg):
        """
        获取文本内容
        :param loc: 元素定位
        :param msg: 元素描述
        :return: 文本内容
        """
        ele = self.wait_element_visible(loc, msg=msg)
        try:
            text = ele.text
            logger.info('{}元素文本：{}'.format(msg, text))
        except Exception as e:
            logger.error("获取文本失败")
            self.my_save_webImgs()
            raise e
        else:
            return text

    def my_switch_alert(self):
        """
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :return: alert内容
        """
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.alert_is_present())
            result = self.driver.switch_to.alert
            if result:
                text = result.text
                logger.info("alert出现,内容：{}".format(text))
                result.accept()
                logger.info("alert已经关闭")
                return text
            else:
                logger.info("未弹出alert")

        except:
            logger.error("alert切换失败！")
            self.my_save_webImgs()
            raise

    def my_save_webImgs(self):
        """
        失败截图，并加入allure
        :return: None
        """
        # filepath=制定的图片保存目录/(页面功能名称)_当前时间到秒.png
        name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filepath = root_dir + r'\imgs\{}.png'.format(name)
        try:
            self.driver.save_screenshot(filepath)
            logger.info("截屏成功,图片路径为{}".format(filepath))
            sleep(1)
            allure.attach.file(filepath, name, allure.attachment_type.PNG)
        except:
            logger.error("截屏失败")

    def my_switch_iframe(self, loc):
        """
        切换iframe
        :param loc: 元素定位
        :return:
        """
        logger.info("iframe切换：{}".format(loc))
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
        logger.info('关闭窗口')

    def my_double_click(self, loc, msg):
        """
        鼠标双击
        :param loc: 元素定位
        :return:
        """
        ele = self.wait_element_visible(loc, msg=msg)
        try:
            AC(self.driver).double_click(ele).perform()
            logger.info("{0}元素：鼠标双击成功".format(loc))
        except:
            logger.error("鼠标双击操作失败。")
            self.my_save_webImgs()
            raise
