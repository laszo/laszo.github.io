---
title: "mac 安装 nginx 过程中的提示信息"
date: 2014-08-11 11:44
categories:
slug: mac-install-nginx-info-out
---
mac 下安装nginx：
```
brew install nginx
```
安装中的提示信息：
```
localhost:test-pub laszo$ brew install nginx
==> Installing nginx dependency: pcre
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/pcre-8.35.mavericks.bottle.tar.
######################################################################## 100.0%
==> Pouring pcre-8.35.mavericks.bottle.tar.gz
🍺  /usr/local/Cellar/pcre/8.35: 146 files, 5.8M
==> Installing nginx
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/nginx-1.6.0_1.mavericks.bottle.
######################################################################## 100.0%
==> Pouring nginx-1.6.0_1.mavericks.bottle.tar.gz
==> Caveats
Docroot is: /usr/local/var/www

The default port has been set in /usr/local/etc/nginx/nginx.conf to 8080 so that
nginx can run without sudo.

To have launchd start nginx at login:
    ln -sfv /usr/local/opt/nginx/*.plist ~/Library/LaunchAgents
Then to load nginx now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist
Or, if you don't want/need launchctl, you can just run:
    nginx
==> Summary
🍺  /usr/local/Cellar/nginx/1.6.0_1: 7 files, 912K
```
