---
title: "监视linux服务器运行状态与性能"
date: 2014-11-07 15:15
categories:
slug: monitor-linux-performance
---

我们在使用服务器的时候，当然希望能随时监控服务器的运行状态、系统负载等信息，便于找出系统瓶颈，并且在硬件配置快要不够用的时候及时进行扩展。

下面这篇文章给出了20种有可能会帮助我们的工具。

[20 Command Line Tools to Monitor Linux Performance](http://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)

下面这篇文章给出了25个，当然它们有很多是重复的。
[Top 25 Best Linux Performance Monitoring and Debugging Tools](http://www.thegeekstuff.com/2011/12/linux-performance-monitoring-tools/)

还有下面这篇文章有助于我们理解CPU负载的相关问题，[Understanding Linux CPU Load - when should you be worried?](http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages)，还有[Understanding Disk I/O - when should you be worried?](http://blog.scoutapp.com/articles/2011/02/10/understanding-disk-i-o-when-should-you-be-worried)是关于Disk I/O的，[Determining free memory on Linux](http://blog.scoutapp.com/articles/2010/10/06/determining-free-memory-on-linux)是关于内存的。都值得一看。

类似 uptime、 htop 这些命令，只能够在服务器本机上运行。我们想要随时监控还得远程登录到服务器上，不方便。为了方便，我们可以写一段脚本，随时统计这样的信息，记录在数据库或文件系统，再搭配一个日志系统，这样使用浏览器就可以随时看到服务器的状态，还可以设置短信报警、邮件报警等。

ELK(Elasticsearch + Logstash + Kibana)就是这样的一套方案。参见[Improving Linux log-analysis capabilities with logstash + elasticsearch + kibana](http://blog.carlos-spitzer.com/2014/09/28/improving-linux-log-analysis-capabilities-with-logstash-elasticsearch-kibana/)。