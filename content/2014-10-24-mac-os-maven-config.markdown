---
title: "Mac os 下面Java和Maven配置"
date: 2014-10-24 10:56
categories:
slug: mac-os-maven-config
---

首先，mac os系统的终端是bash，配置文件放在 “~/.bash_profile” 而不是 “~/.profile”，如果你在后者里面更改环境变量，是不起作用的。

1. 下载jdk并安装，地址：[Oracle Java SE Download](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

2. 下载maven，地址：[Apache Maven](http://maven.apache.org/download.cgi)

3. 修改配置文件，添加如下内容：
```
export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK/Home
export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
export PATH=$JAVA_HOME/bin:$PATH
export M2_HOME=/usr/local/apache-maven-3.2.3
export M2=$M2_HOME/bin
export MAVEN_OPTS="-Xms256m -Xmx512m"
export PATH=$M2:$PATH
```

参考：

http://maven.apache.org/download.cgi

http://www.oracle.com/technetwork/cn/community/java/apache-maven-getting-started-1-406235-zhs.html

