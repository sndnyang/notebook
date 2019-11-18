Title: Vultr配置flask运行环境
Slug:  Vultr-config-flask-production-environment
Date: 2017-08-28 15:31:35  
Author: sndnyang (sndnyangd@gmail.com)  
Tags: flask, python, PostgreSQL, Redis, Nginx, git, web     
Category: web开发   
Summary: Vultr, flask, python27, SQLAlchemy, PostgreSQL, Redis, Supervisor, Gunicorn, Nginx, DNS, git, virtualenv 配置汇总      

[TOC]

# 总结

花了1天半才配置成~~~

从Openshift迁移到Vultr的 CentOS 7

涉及内容：

1. ss
2. git
3. PostgreSQL
4. Redis
5. Nginx
6. virtualenv+flask+SQLAlchemy
7. Supervisor+Gunicorn+gevent
8. DNS

# Vultr

1个月5美元， 1G内存，1核CPU， 1000G流量， 25G SSD硬盘， 洛杉矶（达拉斯也不错）

# ss配置 

略

# git

[git安装](/config-centOS-install-git.html)

各种浪费时间

1. 自带版本安装后，是 post-update，弄了个 post-receive， 感觉不太好， 装最新版
2. 最新版安装路径不对， prefix用不对
3. 照样还是 post-update.sample， 还是没有 post-receive， 还是没有反应， 用post-update也行，但没有反应。
4. 发现要先 ./hooks/post-update
5. checkout各种失败， 发现要先clone到运行库文件夹， 或从运行环境pull， 但此时文件夹已经装了 virtualenv， 删了重来， 这样弄了两三次， 能checkout了
6. 在5之前，共享库配置好，本地上传失败，删了重新建 git init --bare， 后来发现是文件夹名多带.git的问题，服务器的共享库文件夹有.git就有，没有就没有，不要乱加
7. 共享库上传分支错误，删了重来~~~

# PostgreSQL

[PostgreSQL安装](/config-centOS-install-postgresql.html)

命令没有执行（没发现要；）， 修改用户权限后没加载重启， 浪费了很多时间

## 数据迁移

[PostgreSQL数据迁移](http://blog.zhimind.com/postgresql-migration.html)

第一遍导出 PostgreSQL自定义格式文件， 结果拥有者用户等问题导入失败（应该是，反正就是停在那里不动了）， 因为 openshift用户名是随机的，我在 Vultr上换了新名字。

之后导出无格式文件， 并把 owner及constraint语句去掉就成功了， 因为我之前执行过 flask 程序，里面已经 db.create_all()过， 所以数据表早就创建好了。

# Redis

[Redis安装](/config-centOS-install-Redis%E5%AE%89%E8%A3%85.html)

安装一遍后， 忘记如何重启、 配置文件（找密码）

# Nginx

[Nginx安装](/config-centOS-install-Nginx.html)

不知道文件(被nginx.conf include)的格式， 纠结了半天， 这个重启倒挺顺利， 导证书时

# virtualenv+flask+SQLAlchemy

CentOS 7 自带 python2.7， 自带PIP， 所以很简单， 直接

    pip install virtualenv

先用git clone 或 init创建运行库文件夹production， 再：

    virtualenv production
    或
    cd production
    virtualenv .

flask等第三方库写在 requirements.txt里，激活虚拟环境 

    source production/bin/activate
    或
    source production Scripts/activate  // windows

运行

    pip install -r requirements

[requirements文件](https://github.com/sndnyang/zhimind/blob/master/requirements.txt)

有个 baidu-aip是百度大脑的接口外， 其他几个大概都能用， 不过版本不少不是最新的。

# Supervisor+Gunicorn+gevent

[Supervisor+Gunicorn+gevent](/Supervisor+Gunicorn+gevent.html)

这个也非常费时， 一直没搞清楚哪个启动哪个的顺序关系， 改了配置文件、gunicorn运行文件gun.py却忘了重启，删了重装过几次，遇到连不上、已占用等问题。

# 域名DNS

Godaddy买的域名， Vultr有免费DNS， 于是我混乱过几分钟——DNS都免费，域名为什么这么贵，忘了要先注册域名，以为DNS随便填了。

Godaddy之前主要是CNAME记录， 转到 openshift\github.io\google app engine等处

对Godaddy DNS设置里的 @ 符号没认清， 如果它写成 "*" 号就不会认错了， 结果不知道是要修改A记录，而CNAME又不支持IP，又是一通好找。

实际上就是，用子域名 sub.domain.com里的 sub 写记录， A记录连IP， CNAME则连域名（比如openshift\google app engine都有）， A记录优先级高于CNAME， 比如都有 www的话，发到A记录的IP。

现在的问题是， 主域名 www 这个可以了， 但另一个连 google app engine的data失败了（本来是好的）， 尴尬。

突然还发现了另一问题， 我之前为什么在 google app engine那边设置了DNS？它已经有 域名了， 我在 godaddy上直接设置CNAME就行了~~~



# debug 2 threads

怎么只调用一次

```py
if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
```