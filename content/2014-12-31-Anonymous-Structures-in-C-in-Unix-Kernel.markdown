---
title: "unix v6 源代码中的匿名结构体"
date: 2014-12-31 10:14
categories:
slug: Anonymous-Structures-in-C-in-Unix-Kernel
---

我们知道，C语言中的结构体定义是：

```
struct tag { member-list } variable-list ; 
```

其中，tag、member-list、variable-list这3部分至少要出现2个，比如：

```
struct 
{
    int a;
    char b;
    double c;
} s1;

struct SIMPLE
{
    int a;
    char b;
    double c;
};
```
都是可以的。

最近在阅读unix v6的源码，却经常发现这样的代码：

```
struct
{
        char    lobyte;
        char    hibyte;
};
struct
{
        int     integ;
};
```

即没有定义结构体的名字，也没有定义这个类型的变量。那么这样的结构体定义有什么意义呢？又是怎么使用的呢？

我从stackoverflow上的一个问答：[Anonymous Structures in C found in Unix Kernel](http://stackoverflow.com/questions/3881064/anonymous-structures-in-c-found-in-unix-kernel)找到了答案：

>
IRC, ancient C compilers kept all field names (such as integ) in a single namespace instead of creating a namespace per struct type. They also did not distinguish between struct pointers and int pointers, so that every pointer has an integ field corresponding to its first sizeof(int) bytes. Since integ is the first value in a struct and has type int, SW->integ corresponds to *((int *)SW).

直接把答案粘过来，就不翻译了。