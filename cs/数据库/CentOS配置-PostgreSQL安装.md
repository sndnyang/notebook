Title: CentOS配置-PostgreSQL安装
Slug: config-centOS-install-postgresql 
Date: 2017-08-28 10:41:29  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code  
tags: Linux, postgresql, web
Category: 数据库  
summary:  CentOS postgresql 安装 配置 和 运行
  
[TOC]

# 下载安装

    curl -O https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm //视版本而定
    rpm -ivh pgdg-centos96-9.6-3.noarch.rpm
    yum -y install postgresql96-server postgresql96-contrib

# 初始化

    /usr/pgsql-9.6/bin/postgresql96-setup initdb
    或
    service postgresql-9.6 initdb  //好像成功率不高，推荐上面那条

修改

    /etc/sysconfig/pgsql/postgresql-9.6 端口和数据路径，

例：

    PGPORT=5432
    PGDATA=/pgdata96

# 启动

    service postgresql-9.6 start
    chkconfig postgresql-9.6 on
    service postgresql-9.6 restart // 我之前就忘了加版本

# 配置

    vi /var/lib/pgsql/9.6/datapostgresql.conf
    listen_addresses = '*' // 如果要远程连接的话，需要重启
    #port = 5432 // 默认不用动

# 防火墙

    firewall-cmd --add-service=postgresql --permanent
    firewall-cmd --reload

# 用户

## 连接数据库

    su - postgres
    psql

或

    psql -U postgres -h localhost

## 用户密码

    CREATE USER sndnyang WITH PASSWORD 'yourpassword';
    ALTER USER sndnyang PASSWORD 'yournewpassword'; 

# 注意

1. 关键字推荐用大写（小写可能出错？）
2. 记住要用 ; 结束一句命令，psql提示符对换行很不明显：  
        postgres=# ALTER USER sndnyang PASSWORD '没有分号结尾'
        postgres-# 左边变化确实不明显，^C

# 用户权限文件

    vi /var/lib/pgsql/9.6/data/pg_hba.conf

## 示例

    local   all             postgres                                ident(peer也行)  // 建议保留一行这个
    local   all             all                                     md5
    host    all             all             127.0.0.1/32            md5
    # IPv6 local connections:
    host    all             all             ::1/128                 md5

修改后，重启服务

    service postgresql-9.6 restart

## 简短说明

MD5 表示密码用 md5 登陆(推荐这个而不是 password)，   
sqlalchemy 自动使用md5, psycopg2 不会自动，所以会出现各种认证问题， 

    sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL:  password authentication failed for user "postgres" // 密码错误
    ident authentication failed for user "postgres" // 忘了
    fe_sendauth: no password supplied  // 没给密码

# 创建数据库

     CREATE DATABASE dbname WITH OWNER=sndnyang ENCODING='UTF8';

# 配置文件

    /var/lib/pgsql/9.6/datapostgresql.conf // 远程连接侦听
    /var/lib/pgsql/9.6/data/pg_hba.conf    // 用户权限
    /etc/sysconfig/pgsql/postgresql-9.6    // 初始配置

# 本地端口转发

port forward利用SSH

    ssh -L <local port>:<remote host>:<remote port> <SSH hostname>

例：

    ssh -L 5433(想在本地侦听的端口):your_host_ip(远程IP或域名):5432(远程端口，这里指服务器上PostgreSQL的端口)  user@your_host_ip(远程IP或域名)

