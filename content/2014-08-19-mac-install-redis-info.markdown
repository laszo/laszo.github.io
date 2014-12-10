---
title: "mac 安装 redis 过程信息"
date: 2014-08-19 17:08
categories:
slug: mac-install-redis-info
---
```
$ brew install redis

==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/redis-2.8.13.mavericks.bottle.t
######################################################################## 100.0%
==> Pouring redis-2.8.13.mavericks.bottle.tar.gz
==> Caveats
To have launchd start redis at login:
    ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
Then to load redis now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
Or, if you don't want/need launchctl, you can just run:
    redis-server /usr/local/etc/redis.conf
==> Summary
🍺  /usr/local/Cellar/redis/2.8.13: 10 files, 1.3M
```
