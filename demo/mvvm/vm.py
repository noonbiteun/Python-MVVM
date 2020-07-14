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
from design.call import call_win
from mvvm.model import *
from mvvm.view import *


class MainWindowVM(object):
    def __init__(self, ui: call_win.CallMainWin):
        self.ui = ui

        # 创建日志内容model
        self.model_log = StringModel('log_to_view', '启动日志')
        # 创建日志窗口view
        self.view_log = LogView(KEEP_TOPIC, self.ui.LogBrowser)  # 由于该窗口不可编辑，故使用保留topic
        # 绑定model 与 view; 使用单向绑定，当model变换时引起view改变；
        # 若需要view或model其中的任意一方改变时，引起另一方改变则可以使用双向绑定 BindingStyle.DOUBLE_BINDING
        fw_proxy.binding(self.model_log, self.view_log, BindingStyle.MODEL_TO_VIEW)

        # 按钮事件
        self.ui.YesBtn.clicked.connect(self.event_log_yes)
        self.ui.NoBtn.clicked.connect(self.event_log_no)

    def event_log_yes(self):
        self.model_log.value = 'log: yes!!!'

    def event_log_no(self):
        self.model_log.value = 'log: no~~~'
