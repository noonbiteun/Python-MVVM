#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     call_main_win
   Description :
   Author :       feizzz
   date：          2020/7/14
-------------------------------------------------
   Change Activity:
                   2020/7/14:
-------------------------------------------------
"""
from PyQt5.QtWidgets import QMainWindow
from design import main_win


class CallMainWin(QMainWindow, main_win.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CallMainWin, self).__init__(parent)
        self.setupUi(self)
        # 设置标题
        self.setWindowTitle("log演示demon")

