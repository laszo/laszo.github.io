---
title: "mac安装CocoaPods"
date: 2015-02-27 15:12
categories:
slug: mac-install-cocoapods
---

首先要安装gem和ruby


先安装 [Xcode](http://developer.apple.com/xcode/) 开发工具，它将帮你安装好 Unix 环境需要的开发包 

然后安装 [Homebrew](http://brew.sh) 
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
curl -L https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm install 2.0.0
rvm 2.0.0 --default
```

切换gem源
```
gem source -r https://rubygems.org/
gem source -a https://ruby.taobao.org
```

然后
```
sudo gem install cocoapods
```

参考：
https://ruby-china.org/wiki/install_ruby_guide
http://code4app.com/article/cocoapods-install-usage
