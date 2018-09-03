Title: python web 部署：gunicorn + supervisor + gevent
Slug: gunicorn-supervisor-deploy  
Date: 2017-08-28 10:41:29  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code  
tags: python, web
Category: web  
summary:  python, web, gunicorn, supervisor, gevent 部署

[TOC]

# 原文

[简书文章](http://www.jianshu.com/p/be9dd421fb8d)

# 个人汇总

[Vultr配置flask运行环境](http://blog.zhimind.com/Vultr-config-flask-production-environment.html)

# gunicorn

## 安装

[安装](http://blog.zhimind.com/Vultr-config-flask-production-environment.html#virtualenvflasksqlalchemy)

## 配置文件

[gun.py](https://github.com/sndnyang/zhimind/blob/master/wsgi/gun.py)

## 运行

    gunicorn -c /path/to/gun.py module_name:app

1. app 是 app = Flask(__name__)的这个 app
2. module_name 可以是文件名(不带.py)， 里面有app，也可以是文件夹名，但里面的__init__.py文件里需要有 app(不管是Flask创建的还是import的)

# supervisor

## 安装

    pip install supervisor                    # pip install -r requirements就行
    echo_supervisord_conf > supervisor.conf   # 生成 supervisor 默认配置文件， 不要奇怪， 这个命令名字就叫这个， 我还以为是写错了~~~

## 配置

在supervisor.conf 配置文件底部添加

    [program:应用名字，不知道中文怎么样]
    command=/path/to/virtualenv/gunicorn -c /path/to/gun.py module:app    ; supervisor启动命令, 整成一个 shell 脚本也成
    directory=/path/to/myproject                         ; 项目(module)文件夹路径
    startsecs=0                                          ; 启动时间
    stopwaitsecs=0                                       ; 终止等待时间
    autostart=false                                      ; 是否自动启动
    autorestart=false                                    ; 是否自动重启
    stdout_logfile=/python/to/yourlog/gunicorn.log       ; 自定义log 日志
    stderr_logfile=/python/to/yourlog/gunicorn.err       ; 自定义错误日志

## 运行

    supervisord -c supervisor.conf                             通过配置文件启动supervisor
    supervisorctl -c supervisor.conf status                    察看supervisor的状态
    supervisorctl -c supervisor.conf reload                    重新载入 配置文件
    supervisorctl -c supervisor.conf start [all]|[appname]     启动指定/所有 supervisor管理的程序进程
    supervisorctl -c supervisor.conf stop [all]|[appname]      关闭指定/所有 supervisor管理的程序进程

## 部署

配置成功后，使用 git 部署程序时， 只要在 post-update 添加

    /path/to/proj/virtualenv/bin/supervisorctl -c /path/to/project/supervisor.conf restart project_name

supervisor的配置没有变动， 不需要reload等
