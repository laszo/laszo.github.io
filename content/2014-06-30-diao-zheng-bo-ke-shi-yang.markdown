---
title: "调整博客"
date: 2014-06-30 18:06
categories:
slug: diao-zheng-bo-ke-shi-yang
---

这个博客的式样需要调整，目前遇到的问题有：

* 文章栏目过于靠左，而不是居中
* 在dev-1上面添加post，如果标题是中文会报错。而在ec2-1上面则没有这个问题。

2014-7-2 14:38 记：
今天已经解决了这个问题。办法是修改如下文件：
```shell
sudo vi /usr/local/lib/python2.7/dist-packages/crotal/create_post.py
```
第14行：
```python
post.title = string
```
修改为：
```python
post.title = unicode(string, errors='ignore')
```
* 这是一个纯静态站点，每次编辑文章都要ssh到服务器上操作，实在太不方便了。
目标是像[这个网站](https://www.zybuluo.com)一样能够在线的写作和发布。当然
这样的话就不是静态站点而是动态的了。也可以现在zybuluo上面写好草稿，
最后一次性的发布。能够不方便，也好。太方便反而不会去慎重对待了。

* 首页的prev按钮不起作用
