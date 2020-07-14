#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     binder
   Description :
   Author :       feizzz
   date：          2020/7/14
-------------------------------------------------
   Change Activity:
                   2020/7/14:
-------------------------------------------------
"""
from mvvm.view_model import *
from mvvm.view import *


def binding_main_ui(ui: MainWinView, vm: MainWinVM):

    # 绑定事件
    ui.YesBtn.clicked.connect(vm.event_log_yes)
    ui.NoBtn.clicked.connect(vm.event_log_no)

    # 双向绑定
    fw_proxy.binding(vm.model_log, ui.view_log)
