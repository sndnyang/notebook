Title: CentOS配置-Nginx安装
Slug: config-centOS-install-Nginx 
Date: 2017-08-28 10:41:29  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code  
tags: Linux, Nginx, web
Category: 数据库  
summary:  CentOS Nginx 安装 配置 和 运行 
  
[TOC]

# 下载安装

## 配置源

    vi /etc/yum.repos.d/nginx.repo
    [nginx]
    name=nginx repo
    baseurl=http://nginx.org/packages/OS/OSRELEASE/$basearch/
    gpgcheck=0
    enabled=1

    yum -y install nginx

# 配置

## 默认文件nginx.conf

    /etc/nginx/nginx.conf
    和
    /etc/nginx/conf.d/default.conf      // nginx.conf里有 include /etc/nginx/conf.d/*.conf 来导入

同理可以添加其他文件夹和文件，再在 nginx.conf 里 include, 其他一些发行版的 site-available, site-enabled 就是这个意思， 只要在新文件里写 server {} 部分即可

## 简单配置

[http80\https443简单配置](http://github.com/sndnyang/config/nginx/nginx.conf)

# 运行

    service nginx start
    reload              // 重新加载配置文件
    quit                // 正常关闭
    stop                // 强制关闭


