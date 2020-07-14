#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     framework
   Description :
   Author :       feizzz
   date：          2020/7/9
-------------------------------------------------
   Change Activity:
                   2020/7/9:
-------------------------------------------------
"""
from threading import Thread, Lock
from queue import Queue
from enum import Enum, unique


class Subscriber(object):
    """
    订阅者
    """
    def __init__(self, topic, callback):
        self._topic = topic
        self._callback = callback

    @property
    def topic(self):
        return self._topic

    @property
    def callback(self):
        return self._callback


class Publisher(object):
    """
    发布者
    """
    def __init__(self, topic, content):
        self._topic = topic
        self._content = content

    @property
    def topic(self):
        return self._topic

    @property
    def content(self):
        return self._content

# 保留的topic, 该topic的事件不会响应
KEEP_TOPIC = 'keep'


class EventChannel(Thread):
    """
    消息循环
    """
    def __init__(self):
        super(EventChannel, self).__init__()

        self._working = True
        self._mutex = Lock()
        self._queue = Queue()
        self._resigster_container = {}

    def __del__(self):
        self._working = False

    def run(self) -> None:
        while self._working:
            puber = self._queue.get()
            with self._mutex:
                print('pop event {} : {}'.format(puber.topic, puber.content))
                group = self._resigster_container.get(puber.topic, [])
                for suber in group:
                    suber.callback(puber.content)

    # 事件发布：主题+内容
    def publish(self, topic: str, content):
        puber = Publisher(topic, content)
        self._queue.put(puber)

    # 事件订阅：主题+回调
    def subscribe(self, topic: str, callback):
        suber = Subscriber(topic, callback)
        with self._mutex:
            group = self._resigster_container.get(suber.topic, [])
            group.append(suber)
            self._resigster_container[suber.topic] = group


class BaseModel(object):
    """
    修改 Model 的成员变量时，触发事件发布
    在 signal_proxy 中添加更新model的函数
    """
    def __init__(self, topic: str):
        self._topic = topic

    @property
    def topic(self):
        return self._topic

    def signal_proxy(self):
        print('{} event proxy run'.format(type(self)))


class BaseView(object):
    """
    修改 View 的成员变量时，触发事件发布
    在 signal_proxy 中添加更新view的函数
    """
    def __init__(self, topic: str):
        self._topic = topic

    @property
    def topic(self):
        return self._topic

    def signal_proxy(self):
        print('{} event proxy run'.format(type(self)))


@unique
class BindingStyle(Enum):
    DOUBLE_BINDING = 0  # 双向绑定
    MODEL_TO_VIEW = 1   # model到view
    VIEW_TO_MODEL = 2   # view到model


class Framework(object):
    def __init__(self):
        self.channel = EventChannel()

    def work(self):
        self.channel.setDaemon(self)
        self.channel.start()

    def binding(self, model: BaseModel, view: BaseView, style=BindingStyle.DOUBLE_BINDING):
        if style == BindingStyle.DOUBLE_BINDING:
            self.channel.subscribe(model.topic, view.signal_proxy)
            self.channel.subscribe(view.topic, model.signal_proxy)
        elif style == BindingStyle.MODEL_TO_VIEW:
            # 模型改变引起视图改变
            self.channel.subscribe(model.topic, view.signal_proxy)
        elif style == BindingStyle.VIEW_TO_MODEL:
            # 视图改变引起模型改变
            self.channel.subscribe(view.topic, model.signal_proxy)
        else:
            raise RuntimeWarning('binding is wrong')

# 框架对象
fw_proxy = Framework()
