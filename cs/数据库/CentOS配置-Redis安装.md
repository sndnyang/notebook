Title: CentOS配置-Redis安装
Slug: config-centOS-install-Redis安装 
Date: 2017-08-28 10:41:29  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code  
tags: Linux, Redis, web
Category: 数据库  
summary:  CentOS Redis 安装 配置 和 运行  
  
[TOC]

# 来源

实践内容主要来自 [如何在 CentOS 7 上安装 Redis 服务器](https://linux.cn/article-6719-1.html)

# 下载

    version="4.0.1"
    curl -O http://download.redis.io/releases/redis-$version.tar.gz
    tar zxvf redis-$version.tar.gz
    cd redis-$version

# 安装

    yum -y install gcc g++ make         // -y不要提示是否安装
    make MALLOC=libc                    // MALLOC 很重要
    make install                        // 似乎可要可不要
    cd src/                             // 可执行文件在 src/ 下
    cp redis-server redis-cli /usr/bin
    cp redis-sentinel redis-benchmark redis-check-aof redis-check-dump /usr/bin 2/dev/null                      // 以防某个文件redis-check-dump 不存在

# 配置

    port=6379                           // redis默认端口
    mkdir /etc/redis                    // redis 配置文件夹
    mkdir -p /var/lib/redis/$port       // 创建有效的保存数据的目录

    sysctl -w vm.overcommit_memory=1    // 避免数据被截断
    sysctl -w net.core.somaxconn=512    // 不知道什么用
    echo never > /sys/kernel/mm/transparent_hugepage/enabled    // 取消透明巨页内存（transparent huge pages），因为这会造成 redis 产生延时和内存访问问题

    cd ../              // 配置文件在原地
    cp redis.conf /etc/redis/6379.conf
    cp utils/redis_init_script /etc/init.d/redis_$port

## 配置文件redis.conf

    vi /etc/redis/6379.conf
    daemonize no                    //设置 daemonize 为 no，systemd 需要它运行在前台，否则 redis 会突然挂掉
    pidfile /var/run/redis_6379.pid
    port 6379                       // 默认不用改
    loglevel notice
    logfile /var/log/redis_6379.log
    dir /var/lib/redis/6379
    requirepass "bTFBx1NYYWRMTUEyNHhsCg"  // 密码

### Unix sockets

客户端程序和服务器端程序运行在同一个机器上，所以不需要监听网络上的 socket, 使用 unix socket 替代网络 socket

    port = 0
    unixsocket /tmp/redis.sock
    unixsocketperm 700

## 开机启动服务

    vi /etc/systemd/system/redis_$port.service     // 使用 systemd，所以在 /etc/systems/system 下创建一个单位文件, 不要 _$port 也挺好，免得搞错，但如果要多个的话， 可能还是用来区分的好

## 内容

    [Unit]
    Description=Redis on port $port
    [Service]
    Type=forking
    ExecStart=/etc/init.d/redis_$port start
    ExecStop=/etc/init.d/redis_$port stop
    [Install]
    WantedBy=multi-user.target

    vm.overcommit_memory = 1        // 这两句不知道是不是能直接添加
    net.core.somaxconn=512

    echo never > /sys/kernel/mm/transparent_hugepage/enabled  放到 /etc/rc.local 的结尾

# 启动运行

    service redis_$port start
    service redis_$port restart
    service redis_$port stop

# 配置文件

    /etc/redis/6379.conf                        // 常规配置
    /etc/systemd/system/redis_$port.service     // 启动配置