---
title: "开发了一个简单的静态博客系统"
date: 2014-12-11 07:53
categories:
slug: a-new-blog-system-python-markdown
---

本博客之前使用的crotal在新版本更新之后，出现了少许问题（并非bug）。
修改起来要花不少时间，于是我决定仿照它自己写一个静态的博客系统。


我自己的博客需求其实很简单：
1. 能写东西，支持markdown这样的标记语言，
2. 能发布，供自己和别人浏览。

这样就行了。

今天下午一共花了两个小时构建完毕。放在了github上，名字叫做[realsimpleblog](https://github.com/laszo/realsimpleblog)。因为真的是 real simple 了。喜欢极简风格、有兴趣维护自己独立博客的同学，可以下载使用一下。

我自己当然是这个系统的第一个用户。
我的博客[http://www.lvxiaoyu.com/](http://www.lvxiaoyu.com/)就是基于此系统构建，托管在githubpages上。
我还打算维护一个gist，收集[使用了realsimpleblog的站点](https://gist.github.com/laszo/6fbbb9cef91bde50fb02)。
如果你使用了realsimpleblog，欢迎通知我，我会把你的博客地址加在这个gist上面。

使用步骤：

1. 安装python环境，windows、linux、mac均可。并安装python库yaml、markdown。

2. 下载realsimpleblog
```
https://github.com/laszo/realsimpleblog.git
```
或点击如下连接：[下载zip包](https://github.com/laszo/realsimpleblog/archive/master.zip)，并解压。

3. 开始写博客。在content目录下，新建markdown类型的文件，使用你喜欢的编辑器写吧。如果你不熟悉markdown，可以参看[Markdown 语法说明 (简体中文版)](http://wowubuntu.com/markdown/)，或。[作业部落](https://www.zybuluo.com)提供了在线的markdown编辑器。我向你保证，markdown标记是最最简单易学的，花几分钟时间学会以后，物超所值，欲购从速！
如果你暂时不想写新文章，可以跳到第四步，因为content文件夹中已经附带了一篇“helloworld.markdown”。让你的新博客内容不会为空。

4. 打开命令行终端，进入realsimpleblog目录，输入
```
python main.py
```
我们看到，一个新的静态站点已经生成了。可以打开目录中的index.html 查看博客的首页。目前首页只提供文章列表。而没有文章摘要。

5. 启动本地http服务器，可以在本地预览站点。输入：
```
python -m Httpserver
```
然后打开：[http://127.0.0.1:8000/](http://127.0.0.1:8000/) 就可以看到你的站点。

6. 发布站点。你可以把站点发布到[GitHubPages](https://pages.github.com/)上面。只需要拷贝
index.html文件以及output、static两个文件夹即可。

通过这六个步骤，一套完整的个人独立博客解决方案就完成了。无需花费任何资金和其他工具。

本项目使用python开发，用到了如下几个库：

* [markdown]()，能够把markdown标记语言生成为响应的html标签。
* [jinjia]()，一个模板系统，很多著名的python项目在用。
* [bootstrap](http://getbootstrap.com/)，前端库。

为什么不用Jekyll？因为gem install在windows下运行有问题，难以安装Jekyll。