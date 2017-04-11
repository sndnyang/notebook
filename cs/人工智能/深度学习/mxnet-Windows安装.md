Title: mxnet-Windows安装   
Date: 2017-04-11 10:15
slug: mxnet-Windows-installation
category: 机器学习   
tags: CS, 机器学习, 深度学习, 软件安装  

[TOC]

# Mxnet安装流程

[mxnet官方安装说明](http://mxnet.io/get_started/windows_setup.html)

1. 先装 cuda , 我装了 8.0，但注意它里面自带驱动程序， 可能会造成  mxnet 找不到显卡， 或者叫显卡不支持 CUDA， 下载GPU-Z可查，如果已经支持，不要安装自带的驱动程序。 我是碰到安装驱动后，刚开始能用， 重启后失败，反复重装驱动，黑屏了重启，结果文件坏了，只能重装系统。 现在版本 GeForce 940M  378.92版驱动。
2. 安装 Cuda toolkit , 我装的 5.3 
3. https://github.com/dmlc/mxnet/releases, [mxnet windows下载地址](https://github.com/yajiedesign/mxnet/releases)
4. 按照说明， 初次使用，先下载 base package 即基本包， 我下载的是 vc12， 对应 cudnnv5.1
5. 解压， 将 cudnnv5.1 bin下的cudnnXX_X.dll， 放到 3rdparty\cudnn\bin 下。 和base包里 README.txt描述不同， 里面写的是放到 3rdparty\cudnn 下， 但 setupenv.cmd里是 bin文件夹
6. 运行 setupenv.cmd
7. 下载最新的 mxnet
8. 检查 dll依赖关系， 使用 Dependency Walker 打开 build目录下的 libmxnet.dll， 除了一个 ie 开头的不用管，其他要搜一下，比如是 cudnnv 还是 vc没装好
9. Python版，安装， 照包里的 README.txt 运行、测试即可

# 主要的坑

1. WindowsError: [Error 126]， 上面第8步，检查 dll依赖关系
2. no cuda-capable device，软件GPU-Z可查， 显卡是否支持 CUDA (最下一行的 CUDA前选项框有选中表示支持)， 需要装别的版本驱动程序
3.  driver version is insufficient for CUDA runtime version 驱动版本太低。
4. 驱动版本问题， 刚安装完， 可用， 但重启两次后， 又不能用了， 没有找到解决方案。
5. 我的 GeForce 940M ， 版本 378.92 亲测可用。