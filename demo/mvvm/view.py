#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     view
   Description :
   Author :       feizzz
   date：          2020/7/14
-------------------------------------------------
   Change Activity:
                   2020/7/14:
-------------------------------------------------
"""
from PyQt5.QtWidgets import *

from mvvm.framework import *
from design import main_win


class LogView(BaseView):
    def __init__(self, topic: str, browser: QTextBrowser):
        super().__init__(topic)
        self.browser = browser

    def signal_proxy(self, log: str):
        super().signal_proxy()
        self.browser.append(log)
        # 文本框显示到底部
        self.browser.moveCursor(self.browser.textCursor().End)


class MainWinView(QMainWindow, main_win.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWinView, self).__init__(parent)
        self.setupUi(self)
        # 设置标题
        self.setWindowTitle("log演示demon")

        # 包装view
        self.view_log = LogView('view_to_log', self.LogBrowser)