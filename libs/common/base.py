#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC
from libs.utils.base_path import root_dir
from libs.utils.log import logger
from time import sleep
import allure
import time


class BasePage:
    """基于原生selenium第二次封装"""

    def __init__(self, driver, pagename=''):
        """
        :param driver: 浏览器对象
        :param pagename: 页面名，用于记录log和失败截图
        """
        self.driver = driver
        self.page = pagename

    def get(self, url):
        """
        发送url请求
        :param url: 请求url
        :return: None
        """
        try:
            logger.info(f'打开{url}')
            self.driver.get(url)
        except Exception:
            raise

    def find_element(self, loc, msg=''):
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
            except Exception:
                logger.error('元素定位失败!')
                self.save_img()
                raise
            else:
                logger.info('元素定位成功：耗时{}秒!'.format(round(end_time - start_time, 3)))
                return ele

    def find_elements(self, loc, msg=''):
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
                eles = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(loc))
                end_time = time.time()
            except Exception:
                logger.error('元素定位失败!')
                self.save_img()
                raise
            else:
                logger.info('元素定位成功：耗时{}秒!'.format(round(end_time - start_time, 3)))
                return eles

    def send_keys(self, loc, text='', msg=''):
        """
        输入操作
        :param loc:元素定位表达式
        :param text: 输入内容
        :param msg:元素描述
        :return:
        """
        ele = self.find_element(loc, msg=msg)
        try:
            logger.info('输入内容：{}'.format(text))
            ele.clear()
            ele.send_keys(text)
        except Exception:
            logger.error('输入失败')
            self.save_img()
            raise

    def click(self, loc, msg=''):
        """
        点击操作
        :param loc:元素定位表达式
        :param msg:元素描述
        :return: None
        """

        try:
            logger.info('点击元素：{}'.format(msg))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc)).click()
        except Exception:
            logger.error('点击失败,元素不可点击或者元素点位失败')
            self.save_img()
            raise

    def click_by_js(self, loc, msg=''):
        """
        点击操作
        :param loc:元素定位表达式
        :param msg:元素描述
        :return: None
        """

        try:
            logger.info('点击元素：{}'.format(msg))
            ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception:
            logger.error('点击失败,元素不可点击或者元素点位失败')
            self.save_img()
            raise

    def submit(self, loc):
        """
        提交form表单操作，元素定位在form表单中任意元素即可
        记住只能在form表单中使用，一般在submit难定位时使用
        :param loc:元素定位表达式
        :return:
        """
        ele = self.find_element(loc, msg='提交')
        try:
            logger.info('提交form表单')
            ele.submit()

        except Exception:
            logger.error('提交失败'.format())
            self.save_img()
            raise

    def get_handles(self):
        """
        获取当前所有句柄
        :return:所有句柄
        """
        logger.info('获取所有句柄')
        try:
            all_handles = self.driver.window_handles
        except Exception:
            logger.error('获取句柄失败')
            self.save_img()
            raise
        else:
            return all_handles

    def switch_window(self, handle='new', old_handles=None):
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
        except Exception:
            logger.error("切换失败")
            self.save_img()
            raise

    def get_text(self, loc, msg):
        """
        获取文本内容
        :param loc: 元素定位
        :param msg: 元素描述
        :return: 文本内容
        """
        ele = self.find_element(loc, msg=msg)
        try:
            text = ele.text
            logger.info('{}元素文本：{}'.format(msg, text))
        except Exception:
            logger.error("获取文本失败")
            self.save_img()
            raise
        else:
            return text

    def switch_alert(self, send_keys=None):
        """
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :send: 是否点击bool
        :return: alert内容
        """
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.alert_is_present())
            result = self.driver.switch_to.alert
            if result and send_keys is None:
                text = result.text
                logger.info("alert出现,内容：{}".format(text))
                result.accept()
                logger.info("alert已经关闭")
                return text
            elif result and send_keys is not None:
                text = result.text
                logger.info("alert出现,内容：{}".format(text))
                result.send_key(send_keys)
                result.accept()
                logger.info("alert已经关闭")
                return text
            else:
                logger.info("未弹出alert")
        except Exception:
            logger.error("alert切换失败！")
            self.save_img()
            raise

    def save_img(self):
        """
        失败截图，并加入allure
        :return: None
        """
        name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filepath = root_dir + r'\imgs\{}.png'.format(name)
        try:
            self.driver.save_screenshot(filepath)
            logger.info("截屏成功,图片路径为{}".format(filepath))
            sleep(1)
            allure.attach.file(filepath, name, allure.attachment_type.PNG)
        except Exception:
            logger.error("截屏失败")

    def switch_iframe(self, loc):
        """
        切换iframe
        :param loc: 元素定位
        :return:
        """
        logger.info("iframe切换：{}".format(loc))
        try:
            WebDriverWait(self.driver, timeout=10).until(
                EC.frame_to_be_available_and_switch_to_it(loc))
            logger.info("切换成功")
        except Exception:
            logger.error("iframe切换失败！")
            self.save_img()
            raise

    def window_close(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()
        logger.info('关闭窗口')

    def double_click(self, loc, msg=''):
        """
        鼠标双击
        :param loc: 元素定位
        :return:
        """
        ele = self.find_element(loc, msg=msg)
        try:
            AC(self.driver).double_click(ele).perform()
            logger.info("双击元素：{}".format(loc))
        except Exception:
            logger.error("鼠标双击操作失败。")
            self.save_img()
            raise

    def right_click(self, loc, msg=''):
        """
        右击
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(loc, msg=msg)
        try:
            AC(self.driver).context_click(ele).perform()
            logger.info("右击元素：{}".format(loc))
        except Exception:
            logger.error("右击操作失败。")
            self.save_img()
            raise

    def drag_and_drop(self, loc_rource, loc_tarteg, msg):
        """
        拖动元素
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(loc_rource, msg=msg)
        ele1 = self.find_element(loc_tarteg, msg=msg)
        try:
            AC(self.driver).drag_and_drop(ele, ele1).perform()
            logger.info("拖动元素：{}，{}".format(loc_rource, loc_tarteg))
        except Exception:
            logger.error("拖动操作失败。")
            self.save_img()
            raise

    def scroll_into_view(self, loc, msg=''):
        """
        滚动到元素可见位置
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(loc, msg=msg)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
            logger.info("滚动到元素：{}".format(loc))
        except Exception:
            logger.error("滚动操作失败。")
            self.save_img()
            raise

    def mouse_hover(self, loc, msg=''):
        """
        鼠标悬停到一个元素位置
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(loc, msg=msg)
        try:
            AC(self.driver).move_to_element(ele).perform()
            logger.info("鼠标悬停：{}".format(loc))
        except Exception:
            logger.error("鼠标操作失败。")
            self.save_img()
            raise

    def uncheck_checkbox(self, loc, msg=''):
        """
        取消选择复选框
        :param loc:
        :param msg:
        :return:
        """
        if self.checkbox(loc, msg=msg):
            self.click(loc, msg=msg)
        else:
            logger.info('复选框没有选择')

    def check_checkbox(self, loc, msg=''):
        """
        选择复选框
        :param loc:
        :param msg:
        :return:
        """
        if not self.checkbox(loc, msg=msg):
            self.click(loc, msg=msg)
        else:
            logger.info('复选框已是选择')

    def checkbox(self, loc, msg=''):
        """
        复选框状态
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(loc, msg=msg)
        try:
            status = ele.is_selected
            logger.info("复选框状态：{}".format(loc))
            return status
        except Exception:
            logger.error("获取复选框状态失败。")
            self.save_img()
            raise
