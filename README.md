# Python-MVVM
mvvm framework, coding by Python, simpler to build up gui

一个基于发布-订阅模式实现双向绑定的MVVM框架，纯python语言编写，不依赖于具体的gui组件库，可方便快捷地接入到gui开发中

# 什么是MVVM模式

它采用双向绑定（data-binding）：View的变动，自动反映在 ViewModel，反之亦然

学习资料：[MVC，MVP 和MVVM 的图示- 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2015/02/mvcmvp_mvvm.html)

# 框架解析

双向绑定的实现基于发布-订阅模式实现，所有事件会被发布到一个队列中，对应事件的订阅者会被激活然后执行函数。

view与model不进行直接交互；

view的改变会反馈在view model中，反之亦然；

view中仅定义对应的视图更新函数，view model中处理各种逻辑；

通过binder绑定 view 与 view model。

## diy拓展功能

为了使用多种特殊情况：如demo中的log控件，仅需要从model到view；

framework中定义了三种绑定模式：双向绑定，视图到模型（单向：view->model）， 模型到视图（单向：model -> view）。

# 如何使用该框架

复制`framework.py`到你的项目中，即可立即开始使用，不需要额外导入其他包；

仓库中提供了一个本框架配合PyQt5进行GUI开发的demo，该demo中演示了仅需要在逻辑代码中更新model的值即可自动在界面上显示；

参考[demo](https://github.com/noonbiteun/Python-MVVM/tree/master/demo)的代码即可快速搭建一个基于 MVVM 模式的GUI。

# demo效果
![image](https://github.com/noonbiteun/Python-MVVM/blob/master/demo.gif)
