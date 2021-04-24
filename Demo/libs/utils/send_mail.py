#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 
# @Author  : Mik

import zmail
from libs.utils.rd_yaml import read_yaml


class SendEmail():
    def __init__(self, subject, content_text, *attachments):
        """构造方法，初始化邮件内容
        :param subject:主题内容
        :param content_text:文本内容
        :param attachments:附件，传入数据是字符串，多个值用逗号隔开
        """
        self.subject = subject
        self.content_text = content_text
        self.attachments = list(attachments)

    def send_email(self):
        """
        发送邮件,自动读取邮件配置发送人信息
        """
        self.msg = {
            'subject': self.subject,
            'content_text': self.content_text,
            'attachments': self.attachments
        }
        yaml_info = read_yaml()
        sender = yaml_info['mail']['sender']
        # sender = tuple(yaml_info['mail']['sender'])
        receiver = yaml_info['mail']['receiver']
        z_server = zmail.server(*sender)
        z_server.send_mail(receiver, self.msg)


if __name__ == '__main__':
    s = SendEmail('主题：offer', '内容：恭喜你收到华测的offer',
                  )
    s.send_email()
