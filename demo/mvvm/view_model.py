#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     vm
   Description :
   Author :       feizzz
   date：          2020/7/14
-------------------------------------------------
   Change Activity:
                   2020/7/14:
-------------------------------------------------
"""
from mvvm.model import *


class MainWinVM(object):
    def __init__(self):

        # 创建日志内容model
        self.model_log = StringModel('log_to_view', '启动日志')

    def event_log_yes(self):
        self.model_log.value = 'log: yes!!!'

    def event_log_no(self):
        self.model_log.value = 'log: no~~~'
