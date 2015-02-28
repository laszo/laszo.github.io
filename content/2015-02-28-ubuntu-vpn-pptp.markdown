---
title: "Ubuntu下使用VPN（基于PPTP协议）"
date: 2015-02-28 12:12
categories:
slug: ubuntu-vpn-pptp
---

1.	首先要安装pptp-linux
	
		sudo apt-get install pptp-linux

2.	初始化一个VPN的连接通道
	
		sudo pptpsetup --create myvpn --server xxx.xxx.xxx.xxx --username xx1 --password xx2 --encrypt --start

	通过刚才的创建步骤，在/etc/ppp/peers目录下面，会生成一个叫myvpn的文件。在/etc/ppp目录下面，用户名和密码会写在chap-secrets文件中。这时候，虽然已经添加了VPN、并且启动了连接，但是默认的路由仍然是原来的，我们需要修改路由配置。

3.	修改默认路由
	
		sudo ip route del default
		sudo ip route add default dev ppp0

	这时候已经可以通过VPN连接互联网了。

4.	开启与关闭VPN时需要做的动作。在关闭VPN连接时，需要恢复原来的默认路由
	
		sudo poff myvpn
		sudo ip route add default via xx.xx.xx.xx

	开启VPN时，需要添加新的VPN为默认路由

		sudo pon myvpn
		sudo ip route del default
		sudo ip route add default dev ppp0

5.	如果嫌每次输入命令麻烦，可以将这两段命令写在脚本文件中自动执行。

	Ubuntu在开启VPN连接时，会自动执行/etc/ppp/ip-up.d/下的可执行文件，在关闭VPN连接时，会自动执行/etc/ppp/ip-down.d/目录下的可执行文件。

	所以，可以把如下内容

		#!/bin/bash
		/sbin/ip route del default
		/sbin/ip route add default dev ppp0

	写入 /etc/ppp/ip-up.d/route-traffic 文件。把如下内容

		#!/bin/bash
		/sbin/ip route add default via 192.168.1.1

	写入 /etc/ppp/ip-down.d/disableroute 文件。最后修改文件的执行权限

		sudo chmod a+x /etc/ppp/ip-up.d/route-traffic
		sudo chmod a+x /etc/ppp/ip-down.d/disableroute 

	以后，要开启和关闭VPN，只需执行如下命令即可。

		sudo pon myvpn	
		sudo poff myvpn

