---
title: "编译Android系统源代码的步骤"
date: 2014-10-24 15:33
categories:
slug: compile-android-source-code-enviroment

---

本文简要介绍编译安卓系统源代码所需要的步骤、工具、下载地址等。主要参考了《Android系统源代码情景分析》。
源码分为两部分：安卓系统源代码(AOSP, Android Open Source Project)和安卓内核所使用的linux源代码。

1.	安卓源代码的编译环境推荐使用Ubuntu系统，可以从[sjtu](http://ftp.sjtu.edu.cn/ubuntu-cd/)下载。可以使用最新的64位版本。
1.	下载安装虚拟机[VirtualBox](https://www.virtualbox.org/wiki/Downloads)。
1.	使用vbox安装ubuntu，并安装如下包：
```
sudo apt-get install git-core gnupg flex bison gperf libsdl-dev libesd0-dev libwxgtk2.6-dev build-essential zip curl valgrind
```
1.	安装repo工具：
```
wget https://dl-ssl.google.com/dl/googlesource/git-repo/repo
chmod a+x repo
sudo mv repo /bin/
```
1.	下载源代码：
```
mkdir android;
cd android;
repo init -u https://android.googlesource.com/platform/manifest
repo sync
```
1.	编译源代码：
```
make
```
1. 使用安卓模拟器来运行编译出来的代码：
```
~/android/out/host/linux-x86/bin/emulator
```
如果运行模拟器报错：
```
SDL init failure, reason is: No available video device
```
可以参照[这篇帖子](http://blog.sina.com.cn/s/blog_66c16c980101g5qj.html)所说的方法安装依赖包。

接下来可以编译android所使用的linux内核源代码
---
```
mkdir kernel; cd kernel;
git clone http://android.googlesource.com/kernel/goldfish.git
git checkout remotes/origin/android-goldfish-2.6.29
export PATH=$PATH:~/android-2.3.1/prebuilt/linux-x86/toolchain/arm-eabi-4.4.3/bin
```

1.
```
make goldfish_defconfig
make
```