#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     model
   Description :
   Author :       feizzz
   date：          2020/7/14
-------------------------------------------------
   Change Activity:
                   2020/7/14:
-------------------------------------------------
"""
from mvvm.framework import fw_proxy, BaseModel


class StringModel(BaseModel):
    def __init__(self, topic: str, value: str):
        super().__init__(topic)
        self._string = value

    @property
    def value(self):
        return self._string

    @value.setter
    def value(self, value: str):
        self._string = value
        fw_proxy.channel.publish(self._topic, value)

    def signal_proxy(self, value: str):
        super().signal_proxy()
        self._string = value