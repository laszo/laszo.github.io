---
title: "openfire客户端获取聊天记录"
date: 2014-11-13 10:19
categories:
slug: openfire-ke-hu-duan-huo-qu-liao-tian-ji-lu
---

openfire是当前较为流行的xmpp服务端。使用它作为服务端，借助github上面的一些开源项目，很容易打造出一套跨平台的即时通讯解决方案，包含如下的五个主流平台：PC端的windows、mac os、linux，以及移动端的ios和android平台。

当然，这只能包含最基本的通讯功能。如果想达到QQ、MSN、微信、whatsapp这样主流软件丰富的用户体验，还有许多工作要做。

比如，如何在服务端保存聊天记录，并需要的时候客户端能够获取并展现出来，就需要专门研究一下。

这篇[Openfire Chat Logs](https://community.igniterealtime.org/thread/29686)居然是google搜出来的第一篇。

```
On the server-side it is configured from the "Message Audit Policy" link/page.
```
问题：

1. Message Audit Policy 是否需要装插件？答案：不需要，就在server-server settings页面里。
2. 这样记录应该不是聊天记录吧？仅仅是记录了所有的通讯数据包。不方便根据用户或房间查询聊天记录。答案：不方便。需要一个viewer，有人建议看这篇帖子([audit log viewer?](https://community.igniterealtime.org/thread/29159))。
3. 即便是能看了，也并未提供一个接口，使客户端用以获取与某项的聊天记录。

从这篇的问答里我追踪到了[Non-Jive Openfire Plugins](https://community.igniterealtime.org/docs/DOC-1041)。然后[i-Ball Chat Auditor](http://sourceforge.net/projects/iball-auditor/) 装了一下居然不起作用。如何让它起作用以及如何使用它，留待以后研究了。

[Logging Conversations](https://community.igniterealtime.org/thread/14773)这篇帖子很老（2006年），也很长。另有：[XEP-0136: Message Archiving](http://www.xmpp.org/extensions/xep-0136.html)乃是最权威的资料。

从stackoverflow的一个问题[Smack API - Read Chat Histroy from Openfire Server](http://stackoverflow.com/questions/6635034/smack-api-read-chat-histroy-from-openfire-server)中，
[Alpay](http://stackoverflow.com/users/1206536/alpay)提供了一个回答，这个回答并没有帮助到我，而回答下面的评论（comments）里面，被折叠的一条评论倒是帮助到了我：
>I haven' t tested but you should see [this](http://www.igniterealtime.org/projects/openfire/plugins/monitoring/readme.html), and [this](https://blogs.reucon.com/srt/tag/open_archive/). I hope they help –  Alpay Feb 7 '13 at 12:40

从这里发现，原来[Monitoring Service](http://www.igniterealtime.org/projects/openfire/plugins/monitoring/readme.html)插件就是用于记录聊天记录（chat logs）的。但是有两个问题：

1.	如何从客户端获取这些聊天记录呢？
2.	中文的信息是乱码该如何解决？

根据这篇[spark + openfire的聊天监控问题](http://www.myexception.cn/java-other/1001465.html)，检查了mysql数据库，发现的确有一张ofMessageArchive表。

```
mysql> select * from ofMessageArchive limit 10;

```

可以看到聊天数据的确存在，那么现在有两项工作要做：

1.	解决中文乱码问题。顺便解决用户昵称中文乱码。
2.	写一个小型服务端，提供rest接口，根据fromJID、toJID、sentDate、分页等信息，供客户端查询聊天记录。

按照这篇[解决openfire在使用MySQL数据库后的中文乱码问题](http://blog.sina.com.cn/s/blog_4bf75d0a0100l92b.html)，在serverURL这一节添加如下字符：
```
&amp;useUnicode=true&amp;characterEncoding=utf8
```
之后重启openfire。使用spark发送了几天中英文及数字消息，发现现在不记录中文消息。以前是记录，但显示为问号，现在是不记录。

似乎可以考虑重新安装mysql和openfire了。先在vmware虚拟机上试验一下搞了utf8以后能否支持中文昵称和中文聊天记录。官方文档：[Database Installation Guide](http://www.igniterealtime.org/builds/openfire/docs/latest/documentation/database.html)。最关键的两个配置：
```
create database openfire default character set utf8 default collate utf8_general_ci

<serverURL>jdbc:mysql://localhost:3306/openfire1?rewriteBatchedStatements=true&amp;useUnicode=true&amp;characterEncoding=UTF-8&amp;characterSetResults=UTF-8</serverURL>
```
经过一番折腾，终于可以在ofMessageArchive这个表里看到中文聊天记录了。剩下的工作就是写一个rest服务端，提供客户端对于聊天记录的查询。只是包装一些简单的sql查询、或者使用ORM库，在这里就不赘述了。

那么刚才提到的Message Audit Policy就可以禁用掉了。Message Audit Policy与Monitoring Service 的关系、特点、异同、适用性，留待以后去探究了。或者，如果读者你对着这方面有要说的，欢迎分享给大家。
