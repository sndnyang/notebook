Title: CentOS配置-git安装
Date: 2017-08-27 20:44:20
slug: config-centOS-install-git
tags: Linux, CentOS, git
summary: centos yum的GIT版本太老，从源代码安装最新的
Type: code

# 卸载旧版本

    git –version // 最新版本2.X.X， 而服务器上只有1.8

    yum remove git

# 下载获取解压源码

    wget https://github.com/git/git/archive/v2.12.2.tar.gz
    tar -zxvf v2.12.2.tar.gz

# 安装依赖的包

    yum update
    yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-ExtUtils-MakeMaker package // 缺什么补什么

# 编译安装
    
    make configure
    ./configure --prefix=/usr // prefix=/usr 或  prefix=/usr/local
    make  // 没有上两行，直接  make prefix=/usr 好像不行
    make install

# 完成

    git --version

# 后续使用

[使用git在服务器上传部署代码](use-git-upload-deploy-project)
