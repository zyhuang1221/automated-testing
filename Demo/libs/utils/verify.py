#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 
# @Author  : Mik


import zmail
import yaml
import os
import time

# def open_yaml():
#     file_dir = os.path.dirname(__file__)
#     path_file = file_dir.replace('libs/utils', 'config/cfg.yaml')
#     print(path_file)
#     with open(path_file, mode='r', encoding='utf-8') as file:
#         msg = yaml.load(file, Loader=yaml.FullLoader)
#         sender = tuple(msg['mail']['sender'])
#         receiver = msg['mail']['receiver']
#         print(receiver,type(receiver))
#
#     return sender,receiver
#         #print(tuple(msg1), type(msg1))  # ['sender'],type(msg['mail']['user']))
#         # print(msg['mail']['password'])
#
#
# data=open_yaml()
# print(data[0],data[1],type(data[0]),type(data[1]))


# import zmail
# # 发件人：发件人账号，密码(授权码) dzpqnpfrbgnndjeg
# sender=('1457139077@qq.com','jmhzkervwxedbafb')
# # 收件人
# receiver=['751212216@qq.com','e751212216@163.com']  #元组只有一个值,一定要加上逗号
# # 邮件内容：主题/正文
# msg={
#     'subject':'邮件主题：测试zmail发送邮件是否成功',
#     'content_text':'邮件正文：zmail发送邮件比smtp发送邮件简单'
# }
# # 发送邮件
# # 1：创建zmail发送邮件的服务
# # email_server=zmail.server(sender[0],sender[1])  #username: str, password: str
# email_server=zmail.server(*sender) # * 解包
# # 2:发送邮件
# email_server.send_mail(receiver,msg)
# import datetime
# import time
#
# now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
# print(now_time)

# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')

# print(type(time.time()),time.time())
#
# try:
#     print(1221)
#
# except Exception as e:
#     raise e
# else:
#     print(2323)
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from libs.utils import log_module
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

l = log_module.Logger()
log = l.get_log(file='web')
try:
    log.info('开始等待页面元素<{}>是否可见！'.format("loc"))
    start_time = time.time()
    ele = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'kw')))

except Exception as e:
    end_time = time.time()
    raise e

else:
    end_time = time.time()

    print(round(end_time - start_time, 1))