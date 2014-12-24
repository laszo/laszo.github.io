---
title: "学习安卓Content Provider及联系人API"
date: 2014-12-17 11:24
categories:
slug: study-content-provicer-and-contacts-api
---

《pro》这本书上30.3.2小节及代码清单30-2中讲到，raw_contacts表中有两个字段：
account_name和account_type，在安卓4.4.2以及5.0中，已经被account_id取代。

在aosp中，联系人API主要定义在ContactsContract.java (core\java\android\provider)	。阅读它的源代码既可以对联系人API有更本质的理解，同时这也是一个学习编写自己的ContentProvider的优秀范本。

ContactsContract定义了一个三层的数据模型，分别是：
1.	ContactsContract.Data：这个表的每一行存储一条信息，比如电话号码或Email。
2.	ContactsContract.RawContacts：每一行存储一个人的信息，该信息属于某个账户。Data里的一行数据相当于RawContacts的一个字段。
3.	ContactsContract.Contacts：该表的每一行聚合了一个或多个RawContacts，如果是同一个人的话。

查看ContentProvider类的源代码，参看ContentProvider.java(core\java\android\content)。

感受：代码的复杂是因为架构设计的复杂。代码本身只是为了支撑和实现架构。如果不了解整体架构设置，看代码只会越看越乱。这是“数据结构决定算法”这一定律的升级版。软件架构决定代码形式。

至于架构为什么复杂呢？多半是由于需求的复杂，或现实世界的逻辑复杂。软件为了实现现实世界复杂的逻辑和需求，不得不把架构设计的复杂。