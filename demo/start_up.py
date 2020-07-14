#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     start_up
   Description :
   Author :       feizzz
   date：          2020/7/14
-------------------------------------------------
   Change Activity:
                   2020/7/14:
-------------------------------------------------
"""
import sys

from mvvm.binder import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # ui
    ui_main_win = MainWinView()
    # vm
    vm_main_win = MainWinVM()

    # 绑定
    binding_main_ui(ui_main_win, vm_main_win)

    # show
    ui_main_win.show()

    # 框架开始工作，事件循环启动
    fw_proxy.work()

    sys.exit(app.exec_())