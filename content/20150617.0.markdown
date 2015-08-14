---
title: "8个Python Web框架基准测试（转）"
date: 2015-06-17 14:22
categories:
slug: 8-python-web-framework-benchmark
---

近来在Hacker News上面看到有人发了一篇帖子，对8个Python Web框架进行了测试。
原文见[Python's Web Framework Benchmarks](http://klen.github.io/py-frameworks-bench/)。

参与测试的框架有如下8个：

* Aiohttp 0.16.3 — http client/server for Asyncio.

* Bottle 0.12.8 — Fast, simple and lightweight WSGI micro web-framework

* Django 1.8.2 — The Web framework for perfectionists with deadlines

* Falcon 0.3.0 — A high-performance Python framework for building cloud APIs

* Flask 0.10.1 — A microframework based on Werkzeug, Jinja2 and good intentions

* Muffin 0.0.88 — A web-framework based on Asyncio stack

* Pyramid 1.5.7 — A small, fast, down-to-earth, open source Python web framework

* Tornado 4.2 — A Python web framework and asynchronous networking library

测试的方法很简单，有如下三项：

1. JSON测试。把一个对象序列化成JSON，并且返回 `application/json`响应。

2. 远程测试。从一个远程服务器获取数据并返回http响应。

3. 完全测试。使用ORM模型从数据库获取一些数据，插入一个新对象，排序并使用模板生成网页。

测试的结果请看原网页。

可以看到，除了第一项序列化JSON对象，后两项的测试中，tornado和aiohttp都取得了领先的成绩，
这显然跟它们使用的异步的事件机制有关。

在这条消息的评论里，有人说这个评测对性能原理考虑的不是很充分，有人说漏掉了某些框架，
还有人给出了另外一个benchmark:[https://www.techempower.com/benchmarks/](https://www.techempower.com/benchmarks/)。

Hacker News上面信息量真的是挺大。