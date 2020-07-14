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

from design.call.call_win import *
from mvvm.vm import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 界面
    ui_main_win = CallMainWin()

    # vm中进行逻辑绑定
    vm_main_window = MainWindowVM(ui_main_win)

    # show
    ui_main_win.show()

    # 框架开始工作，事件循环启动
    fw_proxy.work()

    sys.exit(app.exec_())