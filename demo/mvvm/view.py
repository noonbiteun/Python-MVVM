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
from mvvm.framework import *

from PyQt5.QtWidgets import *


class LogView(BaseView):
    def __init__(self, topic: str, browser: QTextBrowser):
        super().__init__(topic)
        self.browser = browser

    def signal_proxy(self, log: str):
        super().signal_proxy()
        self.browser.append(log)
        # 文本框显示到底部
        self.browser.moveCursor(self.browser.textCursor().End)